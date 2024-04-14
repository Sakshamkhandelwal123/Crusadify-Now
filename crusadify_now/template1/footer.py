import reflex as rx
from crusadify_now import style
from crusadify_now.editorState import EditorState

def footer() -> rx.Component:
    return rx.vstack(
        rx.html(
            EditorState.footerTxt, 
            border = rx.cond(
                (EditorState.currentKey) == "footerTxt",
                "1px solid black",
                "none"
                ),
            on_click=EditorState.set_content(EditorState.footerTxt, "footerTxt")
            ),
        rx.button(EditorState.heroBtnTxt, style=style.hero_btn_style, on_click=lambda: rx.redirect(EditorState.storeUrl)),
        rx.image(src=EditorState.logo, width="150px"),
        rx.link(EditorState.storeUrl, href=EditorState.storeUrl, font_size="24px", color= "black", text_align="center", text_decoration="underline", width="100%"),
        align="center",
        width="100%",
        padding="60px 0px",
    )
    