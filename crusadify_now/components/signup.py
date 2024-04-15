from __future__ import annotations
import reflex as rx
from ..baseState import State
import requests
from .helper import BACKEND_ROUTE


class RegistrationState(State):
    """Handle registration form submission and redirect to dashboard page after registration."""

    success: bool = False
    error_message: str = ""
    token: str = ""
    is_loading: bool = False
    isdisabled: bool = True

    def getAllPages(self):

        data = requests.get(
            f"{BACKEND_ROUTE}/get-all-pages", json={"userId": self.user_id}
        ).json()

        if data[1] == 200:
            self.pages = data[0]
            return data

    async def handle_registration(self, form_data):

        if (
            form_data["name"] == "None"
            or form_data["email"] == "None"
            or form_data["password"] == "None"
        ):

            if form_data.email is None:
                self.error_message = "Email cannot be empty"
                yield rx.set_focus("email_id")
                return
            password = form_data["password"]
            if password is None:
                self.error_message = "Password cannot be empty"
                yield rx.set_focus("password")
                return
            if form_data.name is None:
                self.error_message = "Name cannot be empty"
                yield rx.set_focus("name")
                return
        self.is_loading = True
        self.isdisabled = False
        data = requests.post(f"{BACKEND_ROUTE}/signup", json=form_data).json()
        if data[1] == 500:
            self.error_message = "Please fill all details"
        if data[1] == 201:

            user_data = requests.get(
                f"{BACKEND_ROUTE}/get-user-details", json=data[0]
            ).json()
            self.user_id = user_data[0]["id"]
            self.getAllPages()
            yield [rx.redirect("/dashboard"), State.set_crusadify_token(self.user_id)]
        self.is_loading = False

    def resetState(self):
        self.error_message = ""


@rx.page(route="/signup", on_load=RegistrationState.resetState)
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
                        padding_bottom="14px",
                    ),
                    rx.box(
                        rx.text(
                            RegistrationState.error_message,
                            color="red",
                            id="error-message",
                        ),
                        align_items="center",
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
