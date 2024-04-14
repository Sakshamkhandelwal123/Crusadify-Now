import reflex as rx
from crusadify_now.editorState import EditorState

def editor():
    return rx.vstack(
        rx.editor(
            set_contents=EditorState.content,
            set_options=rx.EditorOptions(
            button_list=[
                ["font"],
                 ["fontSize"],
                [ "fontColor"],
                [
                    "bold",
                    "italic",
                    "underline",
                ],
                ["removeFormat"],
                "/",
            ]
            ),
            on_change=EditorState.handle_change,
            placeholder="Select text to edit",
            width="26em",
            height="26em",
        ),
        width="100%",
    )

def quoteTextarea():
    return rx.text_area(
        value = EditorState.quote,
        on_change=EditorState.set_quote,
        width="26em",
    )

def img(url: str):
    return rx.image(src=url, on_click=EditorState.set_bodySectionImg(url), border=rx.cond(EditorState.content == url, "1px solid black", "none"))

def image_grid():
    image_urls = ["/template1/single-can.webp", "/template1/multiple-cans.webp", "/template1/pour-purple.webp", "/template1/beige.png"]

        
    grid = rx.grid(
        rx.foreach(image_urls, img),
        columns="3",
        spacing="4",
    )
    
    return grid
