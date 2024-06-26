import reflex as rx
from crusadify_now import style
from crusadify_now.template1.topNav import topNav
from crusadify_now.template1.header import header
from crusadify_now.template1.body import body
from crusadify_now.template1.footer import footer
from crusadify_now.baseState import State
from crusadify_now.components.editor import editor
from crusadify_now.components.editor import quoteTextarea
from crusadify_now.components.editor import image_grid
from crusadify_now.components.login import require_login


import reflex as rx
import requests
from ..components.helper import BACKEND_ROUTE
from typing import List
from ..components.create_new import NewSiteState
from ..baseState import State


class TemplateState(State):

    page: dict = {}

    def get_htmlStr(self):

        return f"""
    <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Health Landing Page</title>
    <style>
        body {{
            background-color: {self.primaryColor};
            color: #F4A261;
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
        }}
        header {{
            text-align: center;
            padding: 40px;
        }}
        header img {{
            width: 200px;
        }}
        section {{
            padding: 40px;
            text-align: center;
        }}
        footer {{
            text-align: center;
            background-color: {self.secondaryColor};
            padding: 20px;
        }}
        footer img {{
            width: 100px;
            margin-top: 20px;
        }}
    </style>
</head>
<body>

    <header>
        <h1 style="font-size: 2.5em;">{self.heroTxt}</h1>
        <p style="font-size: 1.2em;">{self.heroSubTxt}</p>
    </header>

    <section>
        <h2 style="font-size: 2em;">{self.bodySection1Txt}</h2>
        <p style="font-size: 1.2em;">{self.bodySection2Txt}</p>
        <p style="font-size: 1.2em;">{self.bodySection3Txt}</p>
    </section>

    <section>
        <blockquote style="font-size: 1.2em;">"{self.quote}"</blockquote>
    </section>

    <footer>
        <p style="font-size: 1.2em;">{self.footerTxt}</p>
    </footer>

</body>
</html>
"""

    def get_page(self):
        page = requests.get(
            f"{BACKEND_ROUTE}/get-page",
            json={"pageId": self.router.page.raw_path.split("/")[2]},
        ).json()
        self.page = page[0]
        print("page",page[0]["meta"].items())
        for key, value in page[0]["meta"].items():
            self.set_initial_state(value, key)

    async def on_publish(self, form_data):
        data = requests.post(
            f"{BACKEND_ROUTE}/publish-page",
            json={
                "userId": self.user_id,
                "pageName": form_data["page_name"],
                "storeName": self.page["store_name"],
                "pageId": self.page["id"],
                "bodyHtml": self.get_htmlStr(),
            },
        ).json()
        return rx.redirect(data["url"])


def floating_edit_button():
    return rx.button(
        rx.image(
            src="/template1/pencil.png",
            width="16px",
        ),
        position="fixed",
        bottom="20px",
        right="20px",
        border="none",
        cursor="pointer",
        boxShadow="0 10px 25px -5px rgba(1, 1, 1, 0.2)",
    )


def floating_preview_button():
    return rx.flex(
        rx.image(
            src="/template1/pencil.png",
            width="16px",
        ),
        rx.image(
            src="/template1/pencil.png",
            width="16px",
        ),
        position="fixed",
        top="0",
        right="0",
        border="none",
        cursor="pointer",
    )


@require_login
@rx.page(route="/template1/[item_id]", on_load=TemplateState.get_page)
def template1() -> rx.Component:

    return rx.vstack(
        rx.hstack(
            rx.form(
                rx.input.root(
                    rx.input(
                        name="page_name",
                        placeholder="Enter your page name...",
                        bg="white",
                        style={"padding": "24px"},
                    ),
                    width="100%",
                    style={"margin-bottom": "24px"},
                ),
                rx.button(
                    "Publish",
                    style=style.publish_btn_style,
                ),
                on_submit=TemplateState.on_publish,
                justify="between",
            ),
            width="100%",
            justify="between",
            align="center",
            padding="1em",
        ),
        rx.drawer.root(
            rx.drawer.trigger(floating_edit_button()),
            rx.drawer.portal(
                rx.drawer.content(
                    rx.scroll_area(
                        rx.flex(
                            rx.drawer.close(rx.box("Close")),
                            rx.text(
                                "Style",
                                font_weight="bold",
                                font_size="1.5em",
                                padding="1em 0",
                            ),
                            rx.cond(
                                ((State.currentKey) == "bodySection1Img")
                                | ((State.currentKey) == "bodySection2Img")
                                | ((State.currentKey) == "bodySection3Img")
                                | ((State.currentKey) == "heroImg"),
                                rx.box(image_grid()),
                                rx.cond(
                                    (State.currentKey) == "quote",
                                    quoteTextarea(),
                                    editor(),
                                ),
                            ),
                            align_items="start",
                            direction="column",
                        )
                    ),
                    top="auto",
                    left="auto",
                    height="100%",
                    width="30em",
                    padding="2em",
                    background_color="white",
                    border="1px solid black",
                )
            ),
            rx.hstack(
                rx.box(
                    rx.vstack(
                        topNav(),
                        header(),
                        body(State.secondaryColor, State.tertiaryColor),
                        footer(),
                        align="center",
                        spacing="0",
                        font_size="1.5em",
                        background_color=State.primaryColor,
                    ),
                    width="100%",
                ),
                width="100%",
                spacing="0",
            ),
            direction="right",
            modal=False,
        ),
        width="100vw",
    )
