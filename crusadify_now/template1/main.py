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
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="css/style.css">
    <link rel="apple-touch-icon" sizes="180x180" href="img/apple-touch-icon.png">
    <link rel="icon" type="image/png" sizes="32x32" href="img/favicon-32x32.png">
    <link rel="icon" type="image/png" sizes="16x16" href="img/favicon-16x16.png">
    <link rel="manifest" href="/site.webmanifest">
    <!-- Place this tag in your head or just before your close body tag. -->
    <script async defer src="https://buttons.github.io/buttons.js"></script>
    <title>Let's Fit Gym</title>
    <style>
       
    </style>
</head>

<body>
    <header class="header">
        <div class="left">
            <img src="img/gym.png" alt="Let's Fit Gym Logo" id="logo">
            <div>Let's Fit Gym</div>
        </div>
        <div class="mid">
            <ul class="navbar">
                <li class="items"><a href="#" class="active">{self.heroTxt}</a></li>
                <li class="items"><a href="#">About US</a></li>
                <li class="items"><a href="#">Fitness Calculator</a></li>
                <li class="items"><a href="#">Contact Us</a></li>
            </ul>
        </div>
        <div class="right">
            <button class="btn">Call Us Now</button><button class="btn">Write to Us</button>
        </div>
    </header>
    <main class="main">
        <div class="container">
            <div class="form1">
                <h1>Become Fit !</h1>
                <h2>||| Join the Gym Now |||</h2>
                <form action="/php/enquireform.php">
                    <div class="form-group">
                        <input type="text" name="" id="" placeholder="What's Your Name?">
                    </div>
                    <div class="form-group">
                        <input type="text" name="" id="" placeholder="What's Your Gender?">
                    </div>
                    <div class="form-group">
                        <input type="email" name="" id="" placeholder="Enter your email" required>
                    </div>
                    <div class="form-group">
                        <input type="tel" name="" id="" placeholder="Enter your Phone Number">
                    </div>
                    <div class="form-group">
                        <input type="date" name="" id="" max="2018-12-31" placeholder="What's Your date Of Birth"
                            required>
                    </div>
                    <div class="form-group">
                        <input type="text" name="" id="" placeholder="What's your Locality?">
                    </div>
                    <button class="btn">Submit</button>
                </form>
            </div>
        </div>
        <div class="container2">
            <!-- Place this tag where you want the button to render. -->
            <a class="github-button" href="https://github.com/SubhanRaj/Gym_Website_Project"
                data-color-scheme="no-preference: light; light: light; dark: light;" data-size="large"
                aria-label="Star SubhanRaj/Gym_Website_Project on GitHub">Star</a>
            <!-- Place this tag where you want the button to render. -->
            <a class="github-button" href="https://github.com/SubhanRaj/Gym_Website_Project/fork"
                data-color-scheme="no-preference: light; light: light; dark: light;" data-size="large"
                aria-label="Fork SubhanRaj/Gym_Website_Project on GitHub">Fork</a>
            <!-- Place this tag where you want the button to render. -->
            <a class="github-button" href="https://github.com/SubhanRaj/Gym_Website_Project/generate"
                data-color-scheme="no-preference: light; light: light; dark: light;" data-size="large"
                aria-label="Use this template SubhanRaj/Gym_Website_Project on GitHub">Use this template</a>

        </div>
    </main>
</body>

</html>

"""

    def get_page(self):
        page = requests.get(
            f"{BACKEND_ROUTE}/get-page",
            json={"pageId": self.router.page.raw_path.split("/")[2]},
        ).json()
        self.page = page[0]
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
