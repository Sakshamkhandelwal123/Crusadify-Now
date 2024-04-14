import reflex as rx
from crusadify_now import style
from crusadify_now.template1.topNav import topNav
from crusadify_now.template1.header import header
from crusadify_now.template1.body import body
from crusadify_now.template1.footer import footer
from crusadify_now.editorState import EditorState
from crusadify_now.components.editor import editor
from crusadify_now.components.editor import quoteTextarea
from crusadify_now.components.editor import image_grid

def floating_edit_button():
    return rx.button(
        rx.image(
            src="/template1/pencil.png", 
            width="16px", 
            ), 
        position= "fixed", 
        bottom= "20px", 
        right= "20px", 
        border= "none", 
        cursor= "pointer",
        boxShadow= "0 10px 25px -5px rgba(1, 1, 1, 0.2)",
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
        position= "fixed", 
        top= "0", 
        right= "0", 
        border= "none", 
        cursor= "pointer",
    )


def template1() -> rx.Component:

    return rx.vstack(
        # rx.hstack(
        #     rx.text("Panel"),
        #     rx.button("Publish", style=style.publish_btn_style),
        #     width="100%",
        #     justify="between",
        #     align="center",
        #     padding="1em",
        # ),
        rx.drawer.root(
            rx.drawer.trigger(floating_edit_button()),
            rx.drawer.portal(
                rx.drawer.content(
                    rx.flex(
                        rx.drawer.close(rx.box("Close")),
                        rx.text("Style", font_weight="bold", font_size="1.5em", padding="1em 0"),
                        rx.cond(
                            ((EditorState.currentKey) == "bodySection1Img") | ((EditorState.currentKey) == "bodySection2Img") | ((EditorState.currentKey) == "bodySection3Img") | ((EditorState.currentKey) == "heroImg"),
                            rx.box(image_grid()),
                            rx.cond(
                                (EditorState.currentKey) == "quote",
                                quoteTextarea(),
                                editor()
                            )
                        ),
                        align_items="start",
                        direction="column",
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
                        body(EditorState.secondaryColor, EditorState.tertiaryColor),
                        footer(),
                        align="center",
                        spacing="0",
                        font_size="1.5em",
                        background_color=EditorState.primaryColor,
                    ),
                    width="100%",
                ),
                width="100%",
                spacing="0",
            ),
            direction="right",
            modal=False,
        ),
        # floating_preview_button(),
        width="100vw",
     )
     