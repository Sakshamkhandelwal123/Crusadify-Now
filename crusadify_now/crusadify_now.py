"""Welcome to Reflex! This file outlines the steps to create a basic app."""

from rxconfig import config
from crusadify_now import style

import reflex as rx

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

def topNav(logo, topNavItems , heroBtnTxt) -> rx.Component:
    return rx.box(
        rx.hstack(
            rx.image(src=logo, width="150px"),
            rx.hstack(
                *[rx.link(item["label"], href=item["href"], style=style.top_nav_tab_style) for item in topNavItems],
            ),
            rx.button(heroBtnTxt, style=style.login_btn_style),
            align="center",
            justify="between",
            width="100%",
        ),
        align="center",
        spacing="4",
        font_size="1.5em",
        padding="10px 0px",
        width="100%",
        background_color="#7ACAA9",
    )

def heroSection(heroTxt, heroSubTxt, heroBtnTxt) -> rx.Component:
    return rx.vstack(
        rx.text(heroTxt, style=style.hero_txt_style),
        rx.text(heroSubTxt, style=style.hero_sub_txt_style),
        rx.button(heroBtnTxt, style=style.hero_btn_style),
    )

def heroImage(heroImg) -> rx.Component:
    return  rx.image(src=heroImg, max_width="800px")
    
def header(heroTxt, heroSubTxt, heroBtnTxt) -> rx.Component:
    return rx.box(
        rx.hstack(
            heroSection(heroTxt, heroSubTxt, heroBtnTxt),
            heroImage("/template1/beige.png"),
            align="center",
            justify="center",
        ),
        align="center",
        spacing="4",
        font_size="1.5em",
        padding="20px 30px",
        width="100%",
        background_color="#7ACAA9",
    )

def body(bodyTxt) -> rx.Component:
    return rx.vstack(
        rx.box(bodyTxt, size="4"),
        align="center",
        spacing="4",
        font_size="1.5em",
    )

def footer(footerTxt) -> rx.Component:
    return rx.hstack(
        rx.box(footerTxt, size="4"),
        align="center",
        spacing="4",
        font_size="1.5em",
    )

def templates() -> rx.Component:
    topNavItems = [{"label": "Home", "href": "/"}, {"label": "About", "href": "/about"}, {"label": "Contact", "href": "/contact"}, {"label": "Shop", "href": "/shop"}, {"label": "Blog", "href": "/blog"}]
    return rx.vstack(
            topNav("/template1/logo.png", topNavItems, "Shop now"),
            header("A new kind of soda.", "20+ refreshing flavours, with less sugar", "Shop now"),
            body("This is the body"),
            footer("Join the crusade!"),
            align="center",
            spacing="0",
            font_size="1.5em",
            width="100vw",
     )
    


app = rx.App()
app.add_page(index)
app.add_page(templates)
