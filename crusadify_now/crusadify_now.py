"""Welcome to Reflex! This file outlines the steps to create a basic app."""

from rxconfig import config

import reflex as rx
from .components.header import header
from .components.headerNext import headerNext
from .components.mainSection import mainSection
from .components.footer import footer


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

font_family_style = {"--framer-font-family": "Inter, sans-serif"}

app = rx.App(global_style=font_family_style)
app.add_page(index)
