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
            spacing="4",
        ),
        align="center",
        spacing="4",
        font_size="1.5em",
        padding="42px 30px",
        width="100%",
    )

def body(bodySection1Txt, bodySection2Txt, bodySection3Txt, quote) -> rx.Component:
    return rx.vstack(
        rx.box(
            rx.hstack(
                rx.image(src="/template1/single-can.webp", max_width="600px"),
                rx.text(bodySection1Txt, style=style.hero_sub_txt_style, max_width="600px"),
                width="100%",
                align="center",
                justify="center",
                spacing="9",
            ),
            width="100%",
            padding="40px 30px",
        ),
         rx.box(
            rx.hstack(
                rx.text(bodySection2Txt, style=style.hero_sub_txt_style, max_width="600px"),
                rx.image(src="/template1/multiple-cans.webp", max_width="600px"),
                width="100%",
                align="center",
                justify="center",
                spacing="9",
            ),
            width="100%",
            padding="40px 30px",
        ),
        rx.box(
            rx.hstack(
                rx.image(src="/template1/pour-purple.webp", max_width="600px"),
                rx.text(bodySection3Txt, style=style.hero_sub_txt_style, max_width="600px"),
                width="100%",
                align="center",
                justify="center",
                spacing="9",
            ),
            width="100%",
            padding="40px 30px",
        ),
         rx.center(
            rx.text('"' + quote + '"',  font_style="italic", text_decoration="underline", max_width="1200px", text_align="center", text_decoration_thickness="10px", text_decoration_color="#7ACAA9"),
            width="100%",
            padding="40px 30px",
        ),

        align="center",
        font_size="1.5em",
        background_color="#F1EBDC",
        width="100%",
        padding="40px 0px",
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
    bodySection1Txt= "Seen the word COLD on our cans? \nWell, they're printed with a special thermo-reactive ink which means it changes colour to blue when the tasty beverage inside is NICE AND COLD. \nCheers science, you're a real pal."
    bodySection2Txt= "As well as being labelled 'THE BEST TASTING ONE' Pals are ALL-NATURAL, low in sugar, GLUTEN FREE, VEGAN FRIENDLY AND free from artificial colours, sweeteners, preservatives and ingredients you can’t pronounce. Basically, we’ve shown bad stuff the door and told good stuff to get on over here because the sun’s out, the music’s on and all our pals (with Pals) are here. "
    bodySection3Txt= "Our cans are filled with nothing but the best PREMIUM SPIRITS and REAL FRUIT extracts from prime fruit producing regions – to create one hell of a tasty drink. Like that drink you’d mix yourself if you could just get your hands on a clean glass, a couple of lemons and an award-winning mixologist."
    quote="We have always believed there is more to business than just offering a product or service."
    return rx.vstack(
            topNav("/template1/logo.png", topNavItems, "Shop now"),
            header("A new kind of soda", "20+ refreshing flavours, with less sugar", "Shop now"),
            body(bodySection1Txt, bodySection2Txt, bodySection3Txt, quote),
            footer("Join the crusade!"),
            align="center",
            spacing="0",
            font_size="1.5em",
            width="100vw",
            background_color="#EE8F4E",
     )
    


app = rx.App()
app.add_page(index)
app.add_page(templates)
