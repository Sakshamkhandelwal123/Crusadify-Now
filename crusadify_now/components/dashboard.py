import reflex as rx
from ..baseState import State
from .login import require_login
import requests
from .helper import BACKEND_ROUTE
from typing import List


class DashboardState(State):

    success: bool = False
    error_message: str = ""
    token: str = ""


@rx.page(route="/dashboard")
@require_login
def dashboard():

    return rx.vstack(
        rx.flex(
            # rx.link(
            rx.button(
                "Logout",
                on_click=State.logout,
                cursor="pointer",
            ),
            justify_content="end",
            align_items="center",
            width="100%",
            padding="36px",
        ),
        rx.card(
            rx.flex(
                rx.flex(
                    rx.heading(
                        "My Sites",
                        style={
                            "font-size": "36px",
                            "line-height": "1.2",
                        },
                    ),
                    width=["100%", "100%", "100%", "50%", "50%"],
                ),
                rx.link(
                    rx.button(
                        "Create new site",
                        padding="16px",
                        cursor="pointer",
                    ),
                    href="/create_new",
                ),
                justify="between",
                align_items="center",
                margin_bottom="24px",
            ),
            rx.cond(
                State.pages,
                rx.grid(
                    rx.foreach(
                        State.pages,
                        lambda page: rx.hstack(
                            rx.flex(
                                rx.card(
                                    rx.link(
                                        rx.heading(page["site_name"]),
                                        rx.text(page["tag"]),
                                        href=f"/template1/{page['id']}",
                                    ),
                                    style={
                                        "align-items": "center",
                                        "justify-content": "center",
                                        "transition": "background 0.3s",
                                        "_hover": {
                                            "background": "#E3E4E6",
                                            "cursor": "pointer",
                                        },
                                    },
                                ),
                            ),
                            style={"justify-content": "space-between"},
                            width="100%",
                            flex_direction="row",
                            flex_wrap="wrap",
                        ),
                        spacing="1",
                    ),
                    columns="6",
                    spacing="2",
                ),
                rx.flex(
                    rx.heading(
                        "No pages yet.",
                        padding="36px",
                    ),
                    justify_content="center",
                    align_items="center",
                ),
            ),
            style={
                "padding": "36px",
                "width": "1200px",
                "height": "100%",
            },
        ),
        height="100%",
        align_items="center",
        justify_content="center",
    )
