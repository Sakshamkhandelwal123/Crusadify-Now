import reflex as rx

hero_txt_style = dict(
    font_weight="bold",
    font_size=["64px","72px","72px","96px","96px"],
    color="black",
    line_height="1",
    max_width=["500px","500px","400px","500px","600px"],
    text_align=["center", "center", "left", "left", "left"],
)

hero_sub_txt_style = dict(
    font_size=["18px","20px","22px","24px","26px"],
    text_align=["center", "center", "left", "left", "left"],
)

hero_btn_style = dict(
    font_size="20px",
    background_color="black",
    font_weight="bold",
    color="white",
    width="250px",
    border_radius="24px",
    padding="20px 40px",
    margin=["20px auto","20px auto","20px 0","20px 0","20px 0"],
    cursor="pointer",
    border="1px solid black",
    transition="0.2s",
    _hover=dict(
        background_color="transparent",
        color="black",
    )
)

top_nav_tab_style = dict(
    display=["none","none","block","block","block"],
    font_size=["20px","20px","16px","20px","20px"],
    margin="10px 20px",
    color="black",
    transition="0.2s",
    _hover=dict(
        font_weight="bold",
        font_size=["22px","22px","18px","22px","22px"],
        margin="8px 16px",
        text_decoration="underline",
    )
)

top_nav_btn_style = dict(
    display=["none","none","flex","flex","flex"],
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

footer_txt_style = dict(
    size="4", 
    font_size="72px", 
    text_align="center", 
    width="100%", 
    font_weight="bold", 
    margin="0px 0px 20px 0px", 
    line_height="1"
)

quote_txt_style = dict(
    font_style="italic", 
    text_decoration="underline", 
    max_width="1200px", 
    text_align="center", 
    text_decoration_thickness="10px",
)

publish_btn_style = dict(
    border="1px solid black", 
    background_color="transparent", 
    padding="10px 20px",
    border_radius="24px",
    color="black",
    font_size="18px",
    transition="0.2s",
    _hover=dict(
        background_color="black", 
        color="white"
    )
)