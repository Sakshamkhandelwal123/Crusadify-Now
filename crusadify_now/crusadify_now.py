"""Welcome to Reflex! This file outlines the steps to create a basic app."""

from rxconfig import config
from crusadify_now import style

import reflex as rx
from .components.header import header
from .components.headerNext import headerNext
from .components.mainSection import mainSection
from .components.footer import footer
from .template1.main import template1

from .components.login import login
from .components.signup import signup
from .components.create_new import create_new
from .components.dashboard import dashboard
from .components.login import require_login
from .components.all_templates import all_templates

docs_url = "https://reflex.dev/docs/getting-started/introduction/"
filename = f"{config.app_name}/{config.app_name}.py"


@require_login
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
app.add_page(all_templates)
