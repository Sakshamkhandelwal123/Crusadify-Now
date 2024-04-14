import json
import requests
import reflex as rx
from datetime import datetime
from sqlalchemy import and_, DateTime, JSON
from sqlmodel import Field, Column
import importlib

class Page(rx.Model, table=True):
    __tablename__ = "pages"

    id: str = Field(primary_key = True, nullable = False, unique = True)
    user_id: str = Field(nullable=False)
    site_name: str = Field(nullable=False)
    meta: dict = Field(sa_column=Column(JSON, nullable=True, default={}))
    page_name: str = Field(nullable=True)
    page_handle: str = Field(nullable=True)
    store_name: str = Field(nullable=False)
    tag: str = Field(nullable=False)
    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), default=datetime.now, nullable=False))
    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), default=datetime.now, nullable=False, onupdate=datetime.now))

def create_shopify_page(data: dict):
    try:
        if not data or data["siteName"] or data["userId"] or data["tag"]:
            return {"message": "Please provide site name, user id and tag"}, 400
        
        module = importlib.import_module("module")
        
        user = module.find_one_user({"id": data["userId"]})

        if not user:
            return {"message": "User not found"}, 404
        
        page = create_page(
            {
                "id": data["id"], 
                "site_name": data["siteName"], 
                "user_id": data["userId"], 
                "tag": data["tag"]
            }
        )

        return page, 201
    except Exception as e:
        print(e)
        return {"error": e}

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
        return {"error": e}

def publish_page(data: dict):
    try:
        shop = data["storeName"]
        user_id = data["userId"]
        page_id = data["pageId"]

        if not shop or not user_id:
            return {"message": "Please provide store name, page name and user id"}, 400
        
        module = importlib.import_module("module")
        
        user = module.find_one_user({"id": user_id})

        if not user:
            return {"message": "User not found"}, 404

        store_data = module.find_one_store({"store_name": shop, "user_id": user_id})

        if not store_data:
            return {"message": "Store not found"}, 404
        
        page = find_one_page({"id": page_id})

        if not page:
            return {"message": "Page not found"}, 404

        headers = {
            'X-Shopify-Access-Token': store_data.access_token,
            'Content-Type': 'application/json'
        }

        body_html = data["bodyHtml"] #<h2>Warranty</h2>\n<p>Returns accepted if we receive items <strong>30 days after purchase</strong>.</p>

        payload = json.dumps({
            "page": {
                "title": page.page_name,
                "body_html": body_html,
                "metafields": [
                    {
                        "key": "new",
                        "value": "new value",
                        "type": "single_line_text_field",
                        "namespace": "global"
                    }
                ]
            }
        })

        response = requests.post(f"https://{shop}.myshopify.com/admin/api/2024-01/pages.json", headers=headers, data=payload)

        json_response = response.json()

        update_page({"page_handle": json_response.handle})
        return {"response": json_response, "url": f"https://{shop}.myshopify.com/pages/{json_response.handle}"}
    except Exception as e:
        print(e)
        return {"error": e}
    
def get_all_pages(data: dict):
    try:
        if not data["userId"]:
            return {"message": "Please provide user id"}, 400
        
        module = importlib.import_module("module")
        
        user = module.find_one_user({"id": data["userId"]})

        if not user:
            return {"message": "User not found"}, 404
            
        pages = find_all_pages({"user_id": data["userId"]})
        
        return pages, 200
    except Exception as e:
        print(e)
        return {"error": e}
    
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
        return {"error": e}
    
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