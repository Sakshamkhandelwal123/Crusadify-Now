import reflex as rx
from crusadify_now import style
from crusadify_now.baseState import State


def footer() -> rx.Component:
    return rx.vstack(
        rx.html(
            State.footerTxt,
            border=rx.cond(
                (State.currentKey) == "footerTxt", "1px solid black", "none"
            ),
            on_click=State.set_content(State.footerTxt, "footerTxt"),
        ),
        rx.button(
            State.heroBtnTxt,
            style=style.hero_btn_style,
            on_click=lambda: rx.redirect(State.storeUrl),
        ),
        rx.image(src=State.logo, width="150px"),
        rx.link(
            State.storeUrl,
            href=State.storeUrl,
            font_size="24px",
            color="black",
            text_align="center",
            text_decoration="underline",
            width="100%",
        ),
        align="center",
        width="100%",
        padding="60px 0px",
    )
