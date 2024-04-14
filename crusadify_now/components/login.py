import reflex as rx
from ..baseState import State
import requests

from .helper import BACKEND_ROUTE


class LoginState(State):
    """Handle login form submission and redirect to dashboard."""

    isLoading: bool = False
    error_message: str = ""

    def getAllPages(self):

        data = requests.get(
            f"{BACKEND_ROUTE}/get-all-pages", json={"userId": self.user_id}
        ).json()

        if data[1] == 200:
            self.pages = data[0]
            return data

    async def handle_login(self, form_data):
        self.isLoading = True
        data = requests.post(f"{BACKEND_ROUTE}/login", json=form_data).json()

        if data[1] == 200:
            user_data = requests.get(
                f"{BACKEND_ROUTE}/get-user-details", json=data[0]
            ).json()

            self.user_id = user_data[0]["id"]
            self.getAllPages()
            yield [rx.redirect("/dashboard"), LoginState.set_isLoading(False)]
            self.isLoading = False
            self.error_message = ""
        else:
            self.isLoading = False
            self.error_message = data[0]["message"]

    def redir(self):
        """Redirect to the redirect_to route if logged in, or to the login page if not."""
        if not self.is_hydrated:
            # wait until after hydration to ensure auth_token is known
            return LoginState.redir()  # type: ignore
        page = self.router.page.path

        if not self.user_id != "" and page != "/login":
            self.redirect_to = page
            return rx.redirect("/login")
        elif page == "/login":
            return rx.redirect(self.redirect_to or "/")


@rx.page(route="/login")
def login():

    button_text = rx.cond(LoginState.isLoading, "Logging in............", "Login")
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
                        rx.button(
                            button_text,
                            style={"padding": "24px"},
                            cursor="pointer",
                        ),
                        rx.box(
                            rx.text(
                                LoginState.error_message,
                                color="red",
                                id="error-message",
                            ),
                            justify_content="center",
                            align_items="center",
                        ),
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
        ),
    )


def require_login(page):
    """Decorator to require authentication before rendering a page.

    If the user is not authenticated, then redirect to the login page.

    Args:
        page: The page to wrap.

    Returns:
        The wrapped page component.
    """

    def protected_page():
        return rx.cond(
            State.is_hydrated & State.user_id != "",
            page(),
            rx.center(rx.center(rx.chakra.spinner(on_mount=LoginState.redir))),
        )

    protected_page.__name__ = page.__name__
    return protected_page
