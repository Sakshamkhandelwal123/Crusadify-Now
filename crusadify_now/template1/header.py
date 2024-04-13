import reflex as rx
from crusadify_now import style

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
    