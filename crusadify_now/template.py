import reflex as rx
from datetime import datetime
from sqlalchemy import DateTime, JSON, and_
from sqlmodel import Field, Column

class Template(rx.Model, table=True):
    __tablename__ = "templates"

    id: str = Field(primary_key = True, nullable = False, unique = True)
    name: str = Field(nullable=False)
    meta: dict = Field(sa_column=Column(JSON, nullable=False))
    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), default=datetime.now, nullable=False))
    updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), default=datetime.now, nullable=False, onupdate=datetime.now))

def get_template(data: dict):
    try:
        if not data["name"]:
            return {"message": "Please provide name"}, 400
            
        template = find_one_template({"name": data["name"]})
        
        if not template:
            return {"message": "Template does not exist"}, 404
        
        return template, 200
    except Exception as e:
        print(e)
        return {"error": e}
    
def get_all_templates():
    try:
        templates = find_all_templates({})

        return templates, 200
    except Exception as e:
        print(e)
        return {"error": e}

def create_page_template(data: dict):
    try:
        if not data["name"] or not data["meta"]:
            return {"message": "Please provide name and meta"}, 400
            
        template = find_one_template({"name": data["name"]})
        
        if template:
            return {"message": "Template already exists"}, 200
            
        template = create_template({"name": data["name"], "meta": data["meta"]})
        
        return template, 200
    except Exception as e:
        print(e)
        return {"error": e}
        
def update_template(data: dict):
    try:
        if not data["name"]:
            return {"message": "Please provide name"}, 400
            
        template = find_one_template({"name": data["name"]})
        
        if not template:
            return {"message": "Template does not exist"}, 404
            
        template = update_template(data, {"name": data["name"]})
        
        return template, 200
    except Exception as e:
        print(e)
        return {"error": e}

def build_query(model, filters):
    clauses = []
    for field, value in filters.items():
        if hasattr(model, field):
            clauses.append(getattr(model, field) == value)
    return and_(*clauses)

def find_one_template(query):
    query = build_query(Template, query)

    with rx.session() as session:
        template = session.exec(
            Template.select().where(query)
        ).first()

        return template
    
def find_all_templates(query):
    query = build_query(Template, query)

    with rx.session() as session:
        templates = session.exec(
            Template.select().where(query)
        ).all()

        return templates

def create_template(data):
    with rx.session() as session:
        template = Template(**data)
        session.add(template)
        session.commit()

        return template

def update_template(data, query):
    query = build_query(Template, query)

    with rx.session() as session:
        template = session.exec(
            Template.select().where(
                query
            )    
        ).first()

        for field, value in data.items():
            if hasattr(template, field):
                setattr(template, field, value)        
        session.add(template)
        session.commit()