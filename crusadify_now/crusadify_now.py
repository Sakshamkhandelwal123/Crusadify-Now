"""Welcome to Reflex! This file outlines the steps to create a basic app."""

from rxconfig import config
from crusadify_now import style

import reflex as rx

from .shopify_connector import Store, install_app, oauth_callback
from .user import User, Authentication, signin, register, logout, get_user_details
from .shopify_page import (
    Page,
    get_page,
    get_all_pages,
    create_shopify_page,
    update_page,
    publish_page,
)
from .template import (
    Template,
    get_template,
    get_all_templates,
    create_template,
    update_template,
)
from .components.header import header
from .components.headerNext import headerNext
from .components.mainSection import mainSection
from .components.footer import footer
from .template1.main import template1

from .components.login import login
from .components.signup import signup
from .components.create_new import create_new
from .components.dashboard import dashboard

docs_url = "https://reflex.dev/docs/getting-started/introduction/"
filename = f"{config.app_name}/{config.app_name}.py"


def index() -> rx.Component:
    return rx.center(
        rx.flex(
            header(),
            headerNext(),
            mainSection(),
            footer(),
            style={"flex-direction": "column", "width": "100%"},
        ),
        style={
            "font-size": "16px",
            "font-weight": "400",
        },
    )


app = rx.App()
app.add_page(index)
app.add_page(template1)

app.add_page(login)
app.add_page(signup)
app.add_page(create_new)
app.add_page(dashboard)

# Shopify Routes
app.api.add_api_route("/install-app", install_app, methods=["GET"])
app.api.add_api_route("/shopify/oauth/callback", oauth_callback, methods=["GET"])

# User Routes
app.api.add_api_route("/get-user-details", get_user_details, methods=["GET"])
app.api.add_api_route("/login", signin, methods=["POST"])
app.api.add_api_route("/signup", register, methods=["POST"])
app.api.add_api_route("/logout", logout, methods=["POST"])

# Page Routes
app.api.add_api_route("/get-page", get_page, methods=["GET"])
app.api.add_api_route("/get-all-pages", get_all_pages, methods=["GET"])
app.api.add_api_route("/create-page", create_shopify_page, methods=["POST"])
app.api.add_api_route("/publish-page", publish_page, methods=["POST"])
app.api.add_api_route("/update-page", update_page, methods=["PUT"])

# Template Routes
app.api.add_api_route("/get-template", get_template, methods=["GET"])
app.api.add_api_route("/get-all-templates", get_all_templates, methods=["GET"])
app.api.add_api_route("/create-template", create_template, methods=["POST"])
app.api.add_api_route("/update-template", update_template, methods=["PUT"])
