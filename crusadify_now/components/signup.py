from __future__ import annotations
import reflex as rx
from ..baseState import State
import requests


class RegistrationState(State):
    """Handle registration form submission and redirect to dashboard page after registration."""

    success: bool = False
    error_message: str = ""

    async def handle_registration(self, form_data):
        print("formdata", form_data)
        data = requests.post(
            f"https://6aae-112-196-47-10.ngrok-free.app/signup", json=form_data
        ).json()
        print("github", data)
        if data[1] == 201:
            yield [rx.redirect("/dashboard"), RegistrationState.set_success(False)]


@rx.page(route="/signup")
def signup() -> rx.Component:

    register_form = rx.box(
        rx.vstack(
            rx.form(
                rx.fragment(
                    rx.heading("Create an account", size="7", margin_bottom="2rem"),
                    rx.text(
                        "Name",
                        color="hsl(240, 5%, 64.9%)",
                        margin_top="2px",
                        margin_bottom="4px",
                    ),
                    rx.input(
                        placeholder="name",
                        id="name",
                        border_color="hsl(240,3.7%,15.9%)",
                        justify_content="center",
                    ),
                    rx.text(
                        "Email Id",
                        color="hsl(240, 5%, 64.9%)",
                        margin_top="2px",
                        margin_bottom="4px",
                    ),
                    rx.input(
                        placeholder="email_id",
                        id="email",
                        border_color="hsl(240,3.7%,15.9%)",
                        justify_content="center",
                    ),
                    rx.text(
                        "Password",
                        color="hsl(240, 5%, 64.9%)",
                        margin_top="2px",
                        margin_bottom="4px",
                    ),
                    rx.input(
                        placeholder="password",
                        id="password",
                        border_color="hsl(240,3.7%,15.9%)",
                        justify_content="center",
                        type="password",
                    ),
                    rx.box(
                        rx.button(
                            "Sign up",
                            type="submit",
                            width="100%",
                        ),
                        padding_top="14px",
                        padding_bottom="24px",
                    ),
                    rx.link("Login here", href="/login"),
                ),
                style={
                    "margin": "80px",
                    "width": "50%",
                    "padding": "36px",
                    "border-radius": "12px",
                    "background-color": "rgba(237, 231, 225)",
                },
                on_submit=RegistrationState.handle_registration,
            ),
            align_items="center",
        ),
        margin_top="10vh",
        margin_x="auto",
        border_color="gray.300",
        border_radius=10,
    )

    return rx.fragment(register_form)
