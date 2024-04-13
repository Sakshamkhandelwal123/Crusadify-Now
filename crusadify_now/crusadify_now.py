"""Welcome to Reflex! This file outlines the steps to create a basic app."""

from rxconfig import config
from crusadify_now import style

import reflex as rx

from .shopify_connector import Store, install_app, oauth_callback, publish_page
from .user import User, login, signup

docs_url = "https://reflex.dev/docs/getting-started/introduction/"
filename = f"{config.app_name}/{config.app_name}.py"

class State(rx.State):
    """The app state."""

def index() -> rx.Component:
    return rx.center(
        rx.theme_panel(),
        rx.vstack(
            rx.heading("Welcome to Reflex!", size="9"),
            rx.text("Get started by editing ", rx.code(filename)),
            rx.button(
                "Check out our docs!",
                on_click=lambda: rx.redirect(docs_url),
                size="4",
            ),
            rx.logo(),
            align="center",
            spacing="7",
            font_size="2em",
        ),
        height="100vh",
    )

app = rx.App()
app.add_page(index)
app.api.add_api_route("/install-app", install_app, methods=["GET"])
app.api.add_api_route("/shopify/oauth/callback", oauth_callback, methods=["GET"])
app.api.add_api_route("/login", login, methods=["POST"])
app.api.add_api_route("/signup", signup, methods=["POST"])
app.api.add_api_route("/publish-page", publish_page, methods=["POST"])