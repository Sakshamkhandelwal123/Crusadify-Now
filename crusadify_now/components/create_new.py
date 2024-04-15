import reflex as rx
from ..baseState import State
import requests
from .helper import BACKEND_ROUTE
from .login import require_login
from ..editorState import EditorState
from fastapi import Response


class NewSiteState(State):

    success: bool = False
    error_message: str = ""
    isVisible: bool = False
    currentPage: dict = {}

    async def create_page(self, form_data):

        data = requests.post(
            f"{BACKEND_ROUTE}/create-page",
            json={
                "siteName": form_data["site_name"],
                "userId": self.user_id,
                "tag": form_data["tag"],
            },
        ).json()

        self.currentPage = data[0]["page"]
        self.isVisible = not self.isVisible
        return [
            State.set_custom_cookie(data[0]["response"]),
        ]

    def connect_with_shopify(self, form_data):
        data = requests.get(
            f"{BACKEND_ROUTE}/install-app",
            json={
                "storeName": form_data["store_name"],
                "userId": self.user_id,
                "pageId": self.currentPage["id"],
            },
        ).json()

        if (
            data
            and data.__contains__("message")
            and data[0]["message"] == "App already installed"
        ):
            return rx.redirect(f'/template1/{self.currentPage["id"]}')

        return rx.redirect(data["authUrl"])


@rx.page(route="/create_new")
@require_login
def create_new() -> rx.Component:

    isVisible = NewSiteState.isVisible
    create_newSite_form = rx.box(
        rx.vstack(
            rx.form(
                rx.fragment(
                    rx.heading("Create your new site", size="7", margin_bottom="2rem"),
                    rx.text(
                        "Enter your site name",
                        color="hsl(240, 5%, 64.9%)",
                        margin_top="2px",
                        margin_bottom="4px",
                    ),
                    rx.input(
                        placeholder="site name",
                        id="site_name",
                        justify_content="center",
                        margin_top="2px",
                        margin_bottom="4px",
                    ),
                    rx.text(
                        "Select your tag",
                        color="hsl(240, 5%, 64.9%)",
                        padding_top="16px",
                        padding_bottom="16px",
                    ),
                    rx.radio(
                        [
                            "Fashion",
                            "Food & Beverages",
                            "Home & Decor",
                            "Fitness",
                            "Health & Beauty",
                        ],
                        id="tag",
                        size="3",
                        default_value="Fashion",
                        padding_bottom="32px",
                    ),
                    rx.button(
                        "Create page",
                        cursor="pointer",
                    ),
                ),
                style={
                    "margin": "80px",
                    "margin-top": "0px",
                    "width": "50%",
                    "padding": "36px",
                    "border-radius": "12px",
                    "background-color": "rgba(237, 231, 225)",
                    "margin-bottom": "0px",
                },
                on_submit=NewSiteState.create_page,
            ),
            rx.cond(
                isVisible,
                rx.box(
                    rx.form(
                        rx.box(
                            rx.input(
                                placeholder="store name",
                                id="store_name",
                                justify_content="center",
                                margin_top="2px",
                                margin_bottom="4px",
                            ),
                            padding_bottom="12px",
                        ),
                        rx.box(
                            rx.button(
                                "Connect with Shopify",
                                cursor="pointer",
                            ),
                            padding_bottom="36px",
                        ),
                        on_submit=NewSiteState.connect_with_shopify,
                    ),
                ),
            ),
            align_items="center",
        ),
        margin_top="10vh",
        margin_x="auto",
        border_color="gray.300",
        background_color="rgba(237, 231, 225)",
        border_radius=10,
    )

    return rx.fragment(create_newSite_form)
