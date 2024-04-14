"""Welcome to Reflex! This file outlines the steps to create a basic app."""

from rxconfig import config
from crusadify_now import style

import reflex as rx

from .shopify_connector import Store, install_app, oauth_callback
from .shopify_page import publish_page
from .user import User, Authentication, login, signup, logout, get_user_details
from .components.header import header
from .components.headerNext import headerNext
from .components.mainSection import mainSection
from .components.footer import footer
from .components.login import login
from .components.signup import signup

docs_url = "https://reflex.dev/docs/getting-started/introduction/"
filename = f"{config.app_name}/{config.app_name}.py"

def index() -> rx.Component:
    return rx.center(
        rx.flex(
          header(),
        headerNext(),
        mainSection(),
         footer(),
        style={"flex-direction":"column","width":"100%"}
        ),
style={"font-size":"16px","font-weight":"400",}
    )

app = rx.App()
app.add_page(index)
app.add_page(login)
app.add_page(signup)
app.api.add_api_route("/install-app", install_app, methods=["GET"])
app.api.add_api_route("/shopify/oauth/callback", oauth_callback, methods=["GET"])
app.api.add_api_route("/get-user-details", get_user_details, methods=["GET"])
app.api.add_api_route("/login", login, methods=["POST"])
app.api.add_api_route("/signup", signup, methods=["POST"])
app.api.add_api_route("/logout", logout, methods=["POST"])
app.api.add_api_route("/publish-page", publish_page, methods=["POST"])