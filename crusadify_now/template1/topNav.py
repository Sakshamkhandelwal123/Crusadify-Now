import reflex as rx
from crusadify_now import style
from crusadify_now.baseState import State


def topNav() -> rx.Component:
    return rx.box(
        rx.hstack(
            rx.image(
                src=State.logo,
                width=["250px", "250px", "150px", "150px", "150px"],
                margin=["0px auto", "0px auto", "0px", "0px", "0px"],
            ),
            # rx.hstack(
            #     # *[rx.link(item["label"], href=item["href"], style=style.top_nav_tab_style) for item in topNavItems],
            # ),
            rx.button(
                State.heroBtnTxt,
                style=style.top_nav_btn_style,
                on_click=lambda: rx.redirect(State.storeUrl),
            ),
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
