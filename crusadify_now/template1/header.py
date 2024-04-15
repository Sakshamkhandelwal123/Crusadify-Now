import reflex as rx
from crusadify_now import style

# from crusadify_now.editorState import EditorState
from ..baseState import State


def heroSection() -> rx.Component:
    return rx.flex(
        rx.html(
            State.heroTxt,
            border=rx.cond((State.currentKey) == "heroTxt", "1px solid black", "none"),
            on_click=lambda: State.set_content(State.heroTxt, "heroTxt"),
        ),
        rx.html(
            State.heroSubTxt,
            border=rx.cond(
                (State.currentKey) == "heroSubTxt", "1px solid black", "none"
            ),
            on_click=State.set_content(State.heroSubTxt, "heroSubTxt"),
        ),
        rx.button(
            State.heroBtnTxt,
            style=style.hero_btn_style,
            on_click=lambda: rx.redirect(State.storeUrl),
        ),
        flex_direction="column",
        text_align=["center", "center", "left", "left", "left"],
    )


def heroImage() -> rx.Component:
    return rx.image(
        src=State.heroImg,
        max_width=["300px", "400px", "400px", "600px", "800px"],
        on_click=State.set_content(State.heroImg, "heroImg"),
        border=rx.cond(State.currentKey == "heroImg", "1px solid black", "none"),
    )


def header() -> rx.Component:
    return rx.box(
        rx.flex(
            heroSection(),
            heroImage(),
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
