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

def topNav(logo, topNavItems , heroBtnTxt, storeUrl) -> rx.Component:
    return rx.box(
        rx.hstack(
            rx.image(src=logo, width=["250px","250px","150px","150px","150px"], margin=["0px auto","0px auto","0px","0px","0px"]),
            rx.hstack(
                *[rx.link(item["label"], href=item["href"], style=style.top_nav_tab_style) for item in topNavItems],
            ),
            rx.button(heroBtnTxt, style=style.top_nav_btn_style, on_click=lambda: rx.redirect(storeUrl)),
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

def heroSection(heroTxt, heroSubTxt, heroBtnTxt, storeUrl) -> rx.Component:
    return rx.flex(
        rx.text(heroTxt, style=style.hero_txt_style),
        rx.text(heroSubTxt, style=style.hero_sub_txt_style),
        rx.button(heroBtnTxt, style=style.hero_btn_style, on_click=lambda: rx.redirect(storeUrl)),
        flex_direction="column",
    )

def heroImage(heroImg) -> rx.Component:
    return  rx.image(src=heroImg, max_width=[ "300px","400px","400px","600px","800px"])
    
def header(heroTxt, heroSubTxt, heroBtnTxt, storeUrl) -> rx.Component:
    return rx.box(
        rx.flex(
            heroSection(heroTxt, heroSubTxt, heroBtnTxt, storeUrl),
            heroImage("/template1/beige.png"),
            align="center",
            justify="center",
            spacing="4",
            flex_direction=["column-reverse", "column", "row", "row", "row"],
        ),
        align="center",
        spacing="4",
        font_size="1.5em",
        padding="42px 30px",
        width="100%",
    )

def bodyFeatureSection(bodyFeatureTxt, bodyFeatureImg, isReverse = False) -> rx.Component:
    return rx.box(
        rx.flex(
            rx.image(src=bodyFeatureImg, max_width=["300px","300px","400px","500px","600px"]),
            rx.text(bodyFeatureTxt, style=style.hero_sub_txt_style, max_width=["500px","500px","400px","500px","600px"]),
            width="100%",
            align="center",
            justify="center",
            spacing="9",
            flex_direction=["column", "column", "row-reverse" if isReverse else "row", "row-reverse" if isReverse else "row", "row-reverse" if isReverse else "row"],
        ),
        width="100%",
        padding="40px 30px",
    )


def body(bodySection1Txt, bodySection2Txt, bodySection3Txt, quote, secondaryColor, tertiaryColor) -> rx.Component:
    return rx.vstack(
        bodyFeatureSection(bodySection1Txt, "/template1/single-can.webp"),
        bodyFeatureSection(bodySection2Txt, "/template1/multiple-cans.webp", True),
        bodyFeatureSection(bodySection3Txt, "/template1/pour-purple.webp"),
         rx.center(
            rx.text('"' + quote + '"', style= style.quote_txt_style, text_decoration_color=secondaryColor),
            width="100%",
            padding="40px 30px",
        ),

        align="center",
        font_size="1.5em",
        background_color=tertiaryColor,
        width="100%",
        padding="40px 0px",
    )

def footer(footerTxt, heroBtnTxt, logo, storeUrl) -> rx.Component:
    return rx.vstack(
        rx.text(footerTxt, style=style.footer_txt_style),
        rx.button(heroBtnTxt, style=style.hero_btn_style, on_click=lambda: rx.redirect(storeUrl)),
        rx.image(src=logo, width="150px"),
        rx.link(storeUrl, href=storeUrl, font_size="24px", color= "black", text_align="center", text_decoration="underline", width="100%"),
        align="center",
        width="100%",
        padding="60px 0px",
    )

def template1() -> rx.Component:

    # Variables
    primaryColor = "#EE8F4E"
    secondaryColor = "#7ACAA9"
    tertiaryColor = "#F1EBDC"

    logo = "/template1/logo.png"
    heroTxt = "A new kind of soda"
    heroSubTxt = "20+ refreshing flavours, with less sugar"
    heroBtnTxt = "Shop now"
    topNavItems = [{"label": "Home", "href": "/"}, {"label": "About", "href": "/about"}, {"label": "Contact", "href": "/contact"}, {"label": "Shop", "href": "/shop"}, {"label": "Blog", "href": "/blog"}]
    bodySection1Txt= "Seen the word COLD on our cans? \nWell, they're printed with a special thermo-reactive ink which means it changes colour to blue when the tasty beverage inside is NICE AND COLD. \nCheers science, you're a real pal."
    bodySection2Txt= "As well as being labelled 'THE BEST TASTING ONE' Pals are ALL-NATURAL, low in sugar, GLUTEN FREE, VEGAN FRIENDLY AND free from artificial colours, sweeteners, preservatives and ingredients you can’t pronounce. Basically, we’ve shown bad stuff the door and told good stuff to get on over here because the sun’s out, the music’s on and all our pals (with Pals) are here. "
    bodySection3Txt= "Our cans are filled with nothing but the best PREMIUM SPIRITS and REAL FRUIT extracts from prime fruit producing regions – to create one hell of a tasty drink. Like that drink you’d mix yourself if you could just get your hands on a clean glass, a couple of lemons and an award-winning mixologist."
    quote="We have always believed there is more to business than just offering a product or service."
    footerTxt = "Let's be pals!"
    storeUrl = "https://pals.com"

    return rx.vstack(
            topNav(logo, topNavItems, heroBtnTxt, storeUrl),
            header(heroTxt, heroSubTxt, heroBtnTxt, storeUrl),
            body(bodySection1Txt, bodySection2Txt, bodySection3Txt, quote, secondaryColor, tertiaryColor),
            footer(footerTxt, heroBtnTxt, logo, storeUrl),
            align="center",
            spacing="0",
            font_size="1.5em",
            width="100vw",
            background_color=primaryColor,
     )
    


app = rx.App()
app.add_page(index)
app.add_page(template1)
