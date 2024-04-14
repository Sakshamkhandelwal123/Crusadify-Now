import reflex as rx
import requests
from .components.helper import BACKEND_ROUTE
from typing import List


class State(rx.State):
    menu_visible = False
    user_id: str = ""
    pages: List[dict] = []

    def toggle_menu(self):
        self.menu_visible = not self.menu_visible

    async def logout(self):
        data = requests.post(
            f"{BACKEND_ROUTE}/logout", json={"userId": self.user_id}
        ).json()
        if data[1] == 200:

            yield [rx.redirect("/login")]
            self.user_id = ""
