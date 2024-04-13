import reflex as rx
from dotenv import dotenv_values

load = dotenv_values()

config = rx.Config(
    app_name="crusadify_now",
    db_url=load["DATABASE_URL"]
)