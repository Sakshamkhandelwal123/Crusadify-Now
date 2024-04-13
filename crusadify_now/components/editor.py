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
