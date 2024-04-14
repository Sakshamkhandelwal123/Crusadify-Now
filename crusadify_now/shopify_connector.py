import reflex as rx
import random
import string
from sqlalchemy import and_, Column, DateTime
import requests
import urllib.parse
import uuid
from sqlmodel import Field
from datetime import datetime
from dotenv import dotenv_values
from .shopify_page import update_page
import importlib

load = dotenv_values()

class Store(rx.Model, table=True):
    __tablename__ = "stores"
    
    id: str = Field(primary_key = True, nullable = False, unique = True)
    store_name: str = Field(nullable=False, unique = True)
    user_id: str = Field(nullable=False)
    access_token: str = Field(nullable=True)
    is_app_install: bool = Field(nullable=False, default=False)
    state: str = Field(nullable=True)
    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), default=datetime.now, nullable=False))
    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), default=datetime.now, nullable=False, onupdate=datetime.now))

def install_app(data: dict):
    try:
        shopify_api_key = load["SHOPIFY_API_KEY"]
        scopes = "read_products,read_orders,read_analytics,read_orders,read_product_feeds,read_product_listings,read_products,write_content,read_content"

        shop = data["storeName"]
        user_id = data["userId"]
        page_id = data["pageId"]

        if not shop or not user_id or not page_id:
            return {"message": "Please provide store name, user id and page id"}, 400
        
        module = importlib.import_module("module")
        
        user = module.find_one_user({"id": data["userId"]})

        if not user:
            return {"message": "User not found"}, 404

        store_data = find_one_store({"store_name": shop})

        if not store_data:
            create_store({"id": str(uuid.uuid4()), "user_id": user_id, "store_name": shop})

        if store_data and store_data.is_app_install:
            update_page({"store_name": shop}, {"id": page_id})

            return {"message": "App already installed"}, 200

        nonce = ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))
        redirect_uri = "http://localhost:8000/shopify/oauth/callback"
        auth_url = f"https://{shop}.myshopify.com/admin/oauth/authorize?client_id={shopify_api_key}&scope={scopes}&redirect_uri={redirect_uri}&state={nonce}"

        response = {
            "authUrl": auth_url
        }

        update_page({"store_name": shop}, {"id": page_id})

        return response
    except Exception as e:
        print(e)
        return {"error": e}

def oauth_callback(code, shop, state):
    try:
        apiKey = load["SHOPIFY_API_KEY"]
        apiSecret = load["SHOPIFY_API_SECRET"]

        accessTokenUrl = f"https://{shop}/admin/oauth/access_token"
        accessParams = {
            "client_id": apiKey,
            "client_secret": apiSecret,
            "code": code,
        }

        response = requests.post(accessTokenUrl, params=urllib.parse.urlencode(accessParams))
        data = response.json()

        access_token = data["access_token"]
        store_name = shop.split(".")[0]

        store = find_one_store({store_name: store_name})

        if not store:
            return {"message": "Store not found"}
        
        update_store({ "access_token": access_token, "is_app_install": True, "state": state }, {store_name: store_name})
        
        return response.json()
    except Exception as e:
        print(e)
        return {"error": e}

def build_query(model, filters):
    clauses = []
    for field, value in filters.items():
        if hasattr(model, field):
            clauses.append(getattr(model, field) == value)
    return and_(*clauses)

def find_one_store(query):
    query = build_query(Store, query)

    with rx.session() as session:
        store = session.exec(
            Store.select().where(query)
        ).first()

        return store

def create_store(data):
    with rx.session() as session:
        store = Store(**data)
        session.add(store)
        session.commit()

        return store

def update_store(data, query):
    query = build_query(Store, query)

    with rx.session() as session:
        store = session.exec(
            Store.select().where(
                query
            )    
        ).first()

        for field, value in data.items():
            if hasattr(store, field):
                setattr(store, field, value)        
        session.add(store)
        session.commit()