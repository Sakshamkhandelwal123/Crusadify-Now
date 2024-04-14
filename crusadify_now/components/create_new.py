import reflex as rx
from ..baseState import State
import requests


class NewSiteState(State):

    success: bool = False
    error_message: str = ""
    isVisible: bool = False

    async def on_submit(self, form_data):
        print("formdata", form_data)

    def toggle_visibility(self):
        self.isVisible = not self.isVisible


@rx.page(route="/create_new")
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
                    rx.box(
                        rx.text(
                            "Create page",
                            on_click=NewSiteState.toggle_visibility,
                        ),
                        width="30%",
                        border_radius="12px",
                        padding="8px",
                        background_color="#0090FF",
                        color="white",
                        cursor="pointer",
                    ),
                    rx.cond(
                        isVisible,
                        rx.box(
                            rx.text(
                                "Store name",
                                color="hsl(240, 5%, 64.9%)",
                                padding_top="16px",
                                padding_bottom="16px",
                            ),
                            rx.input(
                                placeholder="store name",
                                id="store_name",
                                justify_content="center",
                                margin_top="2px",
                                margin_bottom="4px",
                            ),
                            rx.box(
                                rx.button(
                                    "Connect with Shopify",
                                    cursor="pointer",
                                ),
                                padding_top="24px",
                            ),
                        ),
                    ),
                ),
                style={
                    "margin": "80px",
                    "margin-top": "0px",
                    "width": "50%",
                    "padding": "36px",
                    "border-radius": "12px",
                    "background-color": "rgba(237, 231, 225)",
                },
                on_submit=NewSiteState.on_submit,
            ),
            align_items="center",
        ),
        margin_top="10vh",
        margin_x="auto",
        border_color="gray.300",
        border_radius=10,
    )

    return rx.fragment(create_newSite_form)
