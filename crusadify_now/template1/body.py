import reflex as rx
from crusadify_now import style

def bodyFeatureSection(bodyFeatureTxt, bodyFeatureImg, isReverse = False) -> rx.Component:
    return rx.box(
        rx.flex(
            rx.image(src=bodyFeatureImg, max_width=["300px","300px","400px","500px","600px"]),
            rx.text(bodyFeatureTxt, style=style.hero_sub_txt_style, max_width=["500px","500px","400px","500px","600px"]),
            width="100%",
            align="center",
            justify="center",
            spacing="9",
            flex_direction=["column", "column", "row-reverse" if isReverse else "row", "row-reverse" if isReverse else "row", "row-reverse" if isReverse else "row"],
        ),
        width="100%",
        padding="40px 30px",
    )


def body(bodySection1Txt, bodySection2Txt, bodySection3Txt, quote, secondaryColor, tertiaryColor) -> rx.Component:
    return rx.vstack(
        bodyFeatureSection(bodySection1Txt, "/template1/single-can.webp"),
        bodyFeatureSection(bodySection2Txt, "/template1/multiple-cans.webp", True),
        bodyFeatureSection(bodySection3Txt, "/template1/pour-purple.webp"),
         rx.center(
            rx.text('"' + quote + '"', style= style.quote_txt_style, text_decoration_color=secondaryColor),
            width="100%",
            padding="40px 30px",
        ),

        align="center",
        font_size="1.5em",
        background_color=tertiaryColor,
        width="100%",
        padding="40px 0px",
    )
    