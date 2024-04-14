import reflex as rx
from ..baseState import State
import requests


class LoginState(State):
    """Handle login form submission and redirect to dashboard."""

    success: bool = False
    error_message: str = ""
    rx.Cookie(name="c6-custom-name")

    async def handle_login(self, form_data):
        data = requests.post(
            f"https://6aae-112-196-47-10.ngrok-free.app/login", json=form_data
        ).json()
        print("github", data)
        if data[1] == 200:
            # rx.Cookie(data[0]["token"], max_age=180 * 60)
            # self.set_auth_data("Shalini")

            # rx.LocalStorage("shalini")
            yield [rx.redirect("/dashboard"), LoginState.set_success(False)]


@rx.page(route="/login")
def login():
    return rx.center(
        rx.vstack(
            rx.form(
                rx.vstack(
                    rx.flex(
                        rx.input.root(
                            rx.input(
                                name="email",
                                placeholder="Enter your email id...",
                                bg="white",
                                style={"padding": "24px"},
                            ),
                            width="100%",
                            style={"margin-bottom": "24px"},
                        ),
                        rx.input.root(
                            rx.input(
                                name="password",
                                placeholder="Enter your password...",
                                bg="white",
                                style={"padding": "24px"},
                            ),
                            width="100%",
                            style={"margin-bottom": "24px"},
                        ),
                        rx.button("Login", style={"padding": "24px"}, cursor="pointer"),
                        rx.link(
                            "Signup here",
                            href="/signup",
                            style={"padding-top": "24px"},
                            cursor="pointer",
                        ),
                        style={"flex-direction": "column", "width": "100%"},
                    )
                ),
                on_submit=LoginState.handle_login,
                reset_on_submit=True,
                width="100%",
            ),
            style={
                "margin": "80px",
                "width": "50%",
                "padding": "36px",
                "border-radius": "12px",
                "background-color": "rgba(237, 231, 225)",
            },
        )
    )
