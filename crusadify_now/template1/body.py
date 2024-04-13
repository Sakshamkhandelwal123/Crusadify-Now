import reflex as rx
from crusadify_now import style
from crusadify_now.editorState import EditorState

def bodyFeatureSection(bodyFeatureTxt, bodyFeatureImg, bodySectionKey, isReverse = False) -> rx.Component:
    return rx.box(
        rx.flex(
            rx.image(src=bodyFeatureImg, max_width=["300px","300px","400px","500px","600px"]),
            rx.html(
                bodyFeatureTxt, 
                style=style.hero_sub_txt_style, 
                max_width=["500px","500px","400px","500px","600px"],
                border = rx.cond(
                    (EditorState.currentKey) == bodySectionKey,
                    "1px solid black",
                    "none"
                ),
                on_click=EditorState.set_content(bodyFeatureTxt, bodySectionKey)
                ),
            width="100%",
            align="center",
            justify="center",
            spacing="9",
            flex_direction=["column", "column", "row-reverse" if isReverse else "row", "row-reverse" if isReverse else "row", "row-reverse" if isReverse else "row"],
        ),
        width="100%",
        padding="40px 30px",
    )


def body(secondaryColor, tertiaryColor) -> rx.Component:
    return rx.vstack(
        bodyFeatureSection(EditorState.bodySection1Txt, "/template1/single-can.webp", "bodySection1Txt"),
        bodyFeatureSection(EditorState.bodySection2Txt, "/template1/multiple-cans.webp","bodySection2Txt", True),
        bodyFeatureSection(EditorState.bodySection3Txt, "/template1/pour-purple.webp", "bodySection3Txt"),
        rx.center(
            rx.text(
                '"' + EditorState.quote + '"',
                border = rx.cond(
                    (EditorState.currentKey) == "quote",
                    "1px solid black",
                    "none"
                ),
                style= style.quote_txt_style, 
                text_decoration_color=secondaryColor, 
                on_click=EditorState.set_content(EditorState.quote, "quote")
            ),
            width="100%",
            padding="40px 30px",
        ),

        align="center",
        font_size="1.5em",
        background_color=tertiaryColor,
        width="100%",
        padding="40px 0px",
    )
    