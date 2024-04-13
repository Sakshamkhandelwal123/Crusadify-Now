import reflex as rx

hero_txt_style = dict(
    font_weight="bold",
    font_size="96px",
    color=["pink", "green", "red", "purple", "black"],
    line_height="1",
    max_width="500px",
)

hero_sub_txt_style = dict(
    font_size="26px",
)

hero_btn_style = dict(
    font_size="20px",
    background_color="black",
    font_weight="bold",
    color="white",
    width="250px",
    border_radius="24px",
    padding="20px 40px",
    margin="20px 0",
    cursor="pointer",
    border="1px solid black",
    transition="0.2s",
    _hover=dict(
        background_color="transparent",
        color="black",
    )
)

top_nav_tab_style = dict(
    font_size="20px",
    margin="10px 20px",
    color="black",
    transition="0.2s",
    _hover=dict(
        font_weight="bold",
        font_size="22px",
        margin="8px 16px",
        text_decoration="underline",
    )
)

login_btn_style = dict(
    font_size="20px",
    color="white",
    font_weight="bold",
    border="1px solid black",
    border_radius="24px",
    padding="20px",
    margin="10px 20px",
    cursor="pointer",
    transition="0.2s",
    background_color="black",
    _hover=dict(
        background_color="transparent",
        color="black",
    )
)