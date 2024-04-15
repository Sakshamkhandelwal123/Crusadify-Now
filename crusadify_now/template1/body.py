import reflex as rx
from crusadify_now import style
from crusadify_now.baseState import State


def bodyFeatureSection(
    bodyFeatureTxt, bodyFeatureImg, bodySectionKey, isReverse=False
) -> rx.Component:
    return rx.box(
        rx.flex(
            rx.image(
                src=bodyFeatureImg,
                max_width=["300px", "300px", "400px", "500px", "600px"],
                on_click=State.set_content(bodyFeatureImg, bodySectionKey + "Img"),
                border=rx.cond(
                    State.currentKey == bodySectionKey + "Img",
                    "1px solid black",
                    "none",
                ),
            ),
            rx.html(
                bodyFeatureTxt,
                style=style.hero_sub_txt_style,
                max_width=["500px", "500px", "400px", "500px", "600px"],
                border=rx.cond(
                    (State.currentKey) == bodySectionKey, "1px solid black", "none"
                ),
                on_click=State.set_content(bodyFeatureTxt, bodySectionKey + "Txt"),
            ),
            width="100%",
            align="center",
            justify="center",
            spacing="9",
            flex_direction=[
                "column",
                "column",
                "row-reverse" if isReverse else "row",
                "row-reverse" if isReverse else "row",
                "row-reverse" if isReverse else "row",
            ],
        ),
        width="100%",
        padding="40px 30px",
    )


def body(secondaryColor, tertiaryColor) -> rx.Component:
    return rx.vstack(
        bodyFeatureSection(
            State.bodySection1Txt, State.bodySection1Img, "bodySection1"
        ),
        bodyFeatureSection(
            State.bodySection2Txt, State.bodySection2Img, "bodySection2", True
        ),
        bodyFeatureSection(
            State.bodySection3Txt, State.bodySection3Img, "bodySection3"
        ),
        rx.center(
            rx.text(
                '"' + State.quote + '"',
                border=rx.cond(
                    (State.currentKey) == "quote", "1px solid black", "none"
                ),
                style=style.quote_txt_style,
                text_decoration_color=secondaryColor,
                on_click=State.set_content(State.quote, "quote"),
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
