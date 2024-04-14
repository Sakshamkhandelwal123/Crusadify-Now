import json
import uuid
import requests
import reflex as rx
from datetime import datetime
from sqlmodel import Field, Column
from sqlalchemy import and_, DateTime, JSON

from .models.open_ai import OpenAi

class Page(rx.Model, table=True):
    __tablename__ = "pages"

    id: str = Field(primary_key = True, nullable = False, unique = True)
    user_id: str = Field(nullable=False)
    site_name: str = Field(nullable=False)
    meta: dict = Field(sa_column=Column(JSON, nullable=True, default={}))
    page_name: str = Field(nullable=True)
    page_handle: str = Field(nullable=True)
    store_name: str = Field(nullable=True)
    tag: str = Field(nullable=False)
    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), default=datetime.now, nullable=False))
    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), default=datetime.now, nullable=False, onupdate=datetime.now))

def create_shopify_page(data: dict):
    try:
        if not data or not data["siteName"] or not data["userId"] or not data["tag"]:
            return {"message": "Please provide site name, user id and tag"}, 400
        
        from .user import find_one_user
        
        user = find_one_user({"id": data["userId"]})

        if not user:
            return {"message": "User not found"}, 404
        
        page = create_page(
            {
                "id": str(uuid.uuid4()), 
                "site_name": data["siteName"], 
                "user_id": data["userId"], 
                "tag": data["tag"]
            }
        )

        openai = OpenAi()    
    
        response = openai.generate_content(data["tag"], "", user.name, {})

        update_page({"meta": json.loads(response)}, {"id": page.id})
        return {"page": page, "response": json.loads(response)}, 201
    except Exception as e:
        print(e)
        return {"error": e}, 500

def update_page(data: dict):
    try:
        if not data["pageId"]:
            return {"message": "Please provide page id"}, 400
        
        page = find_one_page({"id": data["pageId"]})

        if not page:
            return {"message": "Page not found"}, 404
        
        page = update_page(data, {"id": data["pageId"]})

        return page, 200
    except Exception as e:
        print(e)
        return {"error": e}, 500

def publish_page(data: dict):
    try:
        shop = data["storeName"]
        page_name = data["pageName"]
        user_id = data["userId"]
        page_id = data["pageId"]

        if not shop or not page_name or not user_id or not page_id:
            return {"message": "Please provide store name, page id and user id"}, 400
        
        from .user import find_one_user
        from .shopify_connector import find_one_store
        
        user = find_one_user({"id": data["userId"]})

        if not user:
            return {"message": "User not found"}, 404

        store_data = find_one_store({"store_name": shop, "user_id": user_id})

        if not store_data:
            return {"message": "Store not found"}, 404
        
        page = find_one_page({"id": page_id})

        if not page:
            return {"message": "Page not found"}, 404

        headers = {
            'X-Shopify-Access-Token': store_data.access_token,
            'Content-Type': 'application/json'
        }

        body_html = data["bodyHtml"]

        payload = json.dumps({
            "page": {
                "title": page_name,
                "body_html": body_html,
            }
        })

        response = requests.post(f"https://{shop}.myshopify.com/admin/api/2024-01/pages.json", headers=headers, data=payload)

        json_response = response.json()

        update_page({"page_handle": json_response['page']['handle'], "page_name": page_name}, {"id": page_id})
        return {"response": json_response, "url": f"https://{shop}.myshopify.com/pages/{json_response.handle}"}
    except Exception as e:
        print(e)
        return {"error": e}, 500
    
def get_all_pages(data: dict):
    try:
        if not data["userId"]:
            return {"message": "Please provide user id"}, 400
        
        from .user import find_one_user
        
        user = find_one_user({"id": data["userId"]})

        if not user:
            return {"message": "User not found"}, 404
            
        pages = find_all_pages({"user_id": data["userId"]})
        
        return pages, 200
    except Exception as e:
        print(e)
        return {"error": e}, 500
    
def get_page(data: dict):
    try:
        if not data["pageId"]:
            return {"message": "Please provide page id"}, 400
            
        page = find_one_page({"id": data["pageId"]})
        
        if not page:
            return {"message": "Page not found"}, 404
            
        return page, 200
    except Exception as e:
        print(e)
        return {"error": e}, 500
    
def build_query(model, filters):
    clauses = []
    for field, value in filters.items():
        if hasattr(model, field):
            clauses.append(getattr(model, field) == value)
    return and_(*clauses)

def find_one_page(query):
    query = build_query(Page, query)

    with rx.session() as session:
        page = session.exec(
            Page.select().where(query)
        ).first()

        return page

def find_all_pages(query):
    query = build_query(Page, query)

    with rx.session() as session:
        pages = session.exec(
            Page.select().where(query)
        ).all()

        return pages

def create_page(data):
    with rx.session() as session:
        page = Page(**data)
        session.add(page)
        session.commit()
        session.refresh(page)

        return page

def update_page(data, query):
    query = build_query(Page, query)

    with rx.session() as session:
        page = session.exec(
            Page.select().where(
                query
            )    
        ).first()

        for field, value in data.items():
            if hasattr(page, field):
                setattr(page, field, value)        
        session.add(page)
        session.commit()