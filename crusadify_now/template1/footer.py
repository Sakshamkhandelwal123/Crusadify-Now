import reflex as rx
from crusadify_now import style

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
    