"""Welcome to Reflex! This file outlines the steps to create a basic app."""

from rxconfig import config

import reflex as rx

docs_url = "https://reflex.dev/docs/getting-started/introduction/"
filename = f"{config.app_name}/{config.app_name}.py"


class State(rx.State):
    """The app state."""


def index() -> rx.Component:
    return rx.center(
        rx.flex(
             rx.hstack(
              rx.flex(
                  rx.text("JOIN THE"),
                  rx.flex(
                      rx.text("JOIN THE",style={"padding":"6px"}),
                      rx.text("JOIN THE",style={"padding":"6px"}),
                      rx.text("JOIN THE",style={"padding":"6px"}),
                      rx.text("JOIN THE",style={"padding":"6px"}),
                      rx.text("JOIN THE",style={"padding":"6px"}),
                      rx.text("JOIN THE",style={"padding":"6px"}),
                      
                  ),
                  style={"justify-content":"space-between","width":"100%","padding":"34px"}
              )   
            
        ),
         rx.vstack(
            rx.text("JOIN THE"),
            rx.heading("Crusaders", size="8"),
            rx.text("Explore Instant today to start building high-converting landing pages and sections, no-code required. ",style={"padding": "10px 0"}),
            rx.button(
                "Signup",
                on_click=lambda: rx.redirect(docs_url),
                size="4",
            ),
            align="center",
             style={"width": "100%","padding":"84px","background-color":"#E1F2FD"}
        ),
        style={"flex-direction":"column","width":"100%"}
        ),

    )


app = rx.App()
app.add_page(index)
