import reflex as rx

def headerNext()->rx.Component:
    return rx.vstack(
            rx.text("JOIN THE"),
            rx.heading("Crusaders", size="9",style={}),
            rx.text("Explore Instant today to start building high-converting landing pages and sections, no-code required. ",style={"padding": "20px 0"}),
            rx.button(
                "Signup",
                on_click=lambda: rx.redirect('/signup'),
                size="4",
                style={"padding":"20px 34px"},
                cursor="pointer"
            ),
            align="center",
             style={"width": "100%","padding":"84px","background-color":"#E1F2FD","background-image":"url(/bg.jpg)","background-repeat":"round","background-size":"cover"}
        )
