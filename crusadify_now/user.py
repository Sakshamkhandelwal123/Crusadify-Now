import reflex as rx
from sqlmodel import Field
from datetime import datetime, timedelta
from sqlalchemy import Column, DateTime, and_
from passlib.context import CryptContext
import uuid
import jwt
from dotenv import dotenv_values

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

def signup(data):
  email = data.email
  password = data.password

  user = find_one_user({"email": email})

  if not user:
    hashed_password = pwd_context.hash(password)

    user = create_user({"id": str(uuid.uuid4()), "email": email, "password": hashed_password, "name": data.name})

    return {"message": "User created successfully"}
  
  return {"message": "User already exists"}

def login(data):
  if not data or not data.email or not data.password:
    return {"message": "Please provide email and password"}
  
  user = find_one_user({"email": data.email})

  if not user:
    return {"message": "User not found"}
  
  if pwd_context.verify(data.password, user.password):
    token = jwt.encode({
      "email": user.email,
      "exp": datetime.utcnow() + timedelta(minutes=180)
    }, load["SECRET_KEY"])

    rx.Cookie("access_token", token, max_age=180*60)

    return {"token": token.decode("utf-8")}
  
  return {"message": "Invalid password"}

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

def create_user(data):
    with rx.session() as session:
        user = User(**data)
        session.add(user)
        session.commit()

        return user