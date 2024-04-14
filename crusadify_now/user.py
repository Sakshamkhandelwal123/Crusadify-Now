import reflex as rx
from sqlmodel import Field
from datetime import datetime
from sqlalchemy import Column, DateTime, and_
from passlib.context import CryptContext
import uuid
import jwt
from dotenv import dotenv_values
import importlib

load = dotenv_values()

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class User(rx.Model, table=True):
  __tablename__ = 'users'

  id: str = Field(primary_key = True, nullable = False, unique = True)
  name: str = Field(nullable = False)
  email: str = Field(nullable = False, unique = True)
  password: str = Field(nullable = False)
  created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), default=datetime.now, nullable=False))
  updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), default=datetime.now, nullable=False, onupdate=datetime.now))

class Authentication(rx.Model, table=True):
  __tablename__ = 'authentications'

  id: str = Field(primary_key = True, nullable = False, unique = True)
  user_id: str = Field(nullable=False)
  token: str = Field(nullable=False)
  created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), default=datetime.now, nullable=False))
  updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), default=datetime.now, nullable=False, onupdate=datetime.now))

def signup(data: dict):
  try:
      email = data["email"]
      password = data["password"]

      user = find_one_user({"email": email})

      if not user:
        hashed_password = pwd_context.hash(password)

        user = create_user({"id": str(uuid.uuid4()), "email": email, "password": hashed_password, "name": data["name"]})

        token = jwt.encode({
          "email": user.email
        }, load["JWT_SECRET"])

        create_token({"id": str(uuid.uuid4()), "user_id": user.id, "token": token.decode("utf8")})

        return {"token": token.decode("utf-8")}, 201
    
      return {"message": "User already exists"}, 200
  except Exception as e:
      print(e)
      return {"error": e}

def login(data: dict):
  try:
      if not data or not data["email"] or not data["password"]:
        return {"message": "Please provide email and password"}, 400
      
      user = find_one_user({"email": data["email"]})

      if not user:
        return {"message": "User not found"}, 404
      
      if pwd_context.verify(data["password"], user.password):
        token = find_one_token({"user_id": user.id})

        if token:
          return {"token": token.token}, 200

        token = jwt.encode({
          "email": user.email
        }, load["JWT_SECRET"])

        create_token({"id": str(uuid.uuid4()), "user_id": user.id, "token": token.decode("utf8")})

        return {"token": token.decode("utf-8")}, 200
      
      return {"message": "Invalid password"}, 401
  except Exception as e:
      print(e)
      return {"error": e}

def logout(data: dict):
    try:
      if not data or not data["userId"]:
        return {"message": "Please provide user id"}, 400
      
      module = importlib.import_module("module")
        
      user = module.find_one_user({"id": data["userId"]})

      if not user:
          return {"message": "User not found"}, 404
      
      token = find_one_token({"user_id": data["userId"]})

      if not token:
        return {"message": "Token not found"}, 404
      
      delete_token({"user_id": data["userId"]})

      return {"message": "Token deleted successfully"}, 200
    except Exception as e:
      print(e)
      return {"error": e}

def get_user_details(data: dict):
    try:
      if not data or not data["token"]:
        return {"message": "Please provide token"}, 400
      
      token = jwt.decode(data["token"], key=load["JWT_SECRET"])

      if not token or not token["email"]:
          return {"message": "Invalid token"}, 401
      
      user = find_one_user({"email": token["email"]})

      if not user:
        return {"message": "User not found"}, 404

      return user, 200
    except Exception as e:
      print(e)
      return {"error": e}

def build_query(model, filters):
    clauses = []
    for field, value in filters.items():
        if hasattr(model, field):
            clauses.append(getattr(model, field) == value)
    return and_(*clauses)

def find_one_user(query):
    query = build_query(User, query)

    with rx.session() as session:
        user = session.exec(
            User.select().where(query)
        ).first()

        return user
    
def find_one_token(query):
    query = build_query(Authentication, query)

    with rx.session() as session:
        token = session.exec(
            Authentication.select().where(query)
        ).first()

        return token

def create_token(data):
    with rx.session() as session:
        token = Authentication(**data)
        session.add(token)
        session.commit()

        return token
    
def delete_token(query):
   query = build_query(Authentication, query)

   with rx.session() as session:
        token = session.exec(
            Authentication.select().where(query)
        ).first()
        session.delete(token)
        session.commit()


def create_user(data):
    with rx.session() as session:
        user = User(**data)
        session.add(user)
        session.commit()
        session.refresh(user)

        return user