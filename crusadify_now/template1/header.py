import reflex as rx
from crusadify_now import style
from crusadify_now.editorState import EditorState

def heroSection() -> rx.Component:
    return rx.flex(
        rx.html(
            EditorState.heroTxt,
            border = rx.cond(
                (EditorState.currentKey) == "heroTxt",
                "1px solid black",
                "none"
            ),      
            on_click=lambda: EditorState.set_content(EditorState.heroTxt, "heroTxt")
        ),        
        rx.html(
            EditorState.heroSubTxt,
            border = rx.cond(
                (EditorState.currentKey) == "heroSubTxt",
                "1px solid black",
                "none"
            ),      
            on_click=EditorState.set_content(EditorState.heroSubTxt, "heroSubTxt")),
        rx.button(
            EditorState.heroBtnTxt, 
            style=style.hero_btn_style, 
            on_click=lambda: rx.redirect(EditorState.storeUrl)
            ),
        flex_direction="column",
        text_align=["center", "center", "left", "left", "left"],
    )

def heroImage(heroImg) -> rx.Component:
    return  rx.image(src=heroImg, max_width=[ "300px","400px","400px","600px","800px"])
    
def header() -> rx.Component:
    return rx.box(
        rx.flex(
            heroSection(),
            heroImage("/template1/beige.png"),
            align="center",
            justify="center",
            spacing="4",
            flex_direction=["column-reverse", "column", "row", "row", "row"],
        ),
        align="center",
        spacing="4",
        font_size="1.5em",
        padding="42px 30px",
        width="100%",
    )
    