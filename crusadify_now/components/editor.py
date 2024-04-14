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
    image_urls = [
        "/template1/single-can.webp", 
        "/template1/multiple-cans.webp", 
        "/template1/pour-purple.webp", 
        "/template1/beige.png", 
        # Fashion
        "/gen/images/fashion/DALL·E 2024-04-14 11.04.58 - A glamorous fashion theme hero image for a Fashion website. The image should depict a high-fashion photoshoot on a city rooftop at sunset. Feature mod.webp",
        "/gen/images/fashion/DALL·E 2024-04-14 11.05.00 - A minimalist fashion theme hero image for a Fashion website. The image should portray a clean and modern aesthetic with a model posing in a simple yet.webp",
        "/gen/images/fashion/DALL·E 2024-04-14 11.05.01 - A glamorous fashion theme image for the body section of a Fashion website. This image should feature a luxurious fashion boutique interior with models.webp",
        "/gen/images/fashion/DALL·E 2024-04-14 11.05.02 - A minimalist fashion theme image for the body section of a Fashion website. The image should capture a modern design studio atmosphere where a fashion.webp",
        "/gen/images/fashion/DALL·E 2024-04-14 11.05.04 - A glamorous fashion theme image for the body section of a Fashion website. The image should depict a dramatic runway show during a fashion week event.webp",
        "/gen/images/fashion/DALL·E 2024-04-14 11.05.06 - A minimalist fashion theme image for the body section of a Fashion website. This image should depict a fashion photoshoot in an urban setting. Capture.webp",
        "/gen/images/fashion/DALL·E 2024-04-14 11.05.10 - A glamorous fashion theme image for the quote section of a Fashion website. This image should feature a close-up of elegant accessories like high-end .webp",
        "/gen/images/fashion/DALL·E 2024-04-14 11.05.11 - A minimalist fashion theme image for the quote section of a Fashion website. This image should depict a subtle and artistic close-up of a tailored gar.webp",
        # fitness
        "/gen/images/fitness/DALL·E 2024-04-14 11.04.40 - A high-energy fitness theme hero image for a Fitness website. The image should depict an intense workout scene in a gym with multiple individuals enga.webp",
        "/gen/images/fitness/DALL·E 2024-04-14 11.04.41 - A calm and focused fitness theme hero image for a Fitness website. The image should show a serene yoga session at sunrise, featuring several people pr.webp",
        "/gen/images/fitness/DALL·E 2024-04-14 11.04.44 - A high-energy fitness theme image for the body section of a Fitness website. The image should capture a dynamic cycling class in full swing, with part.webp",
        "/gen/images/fitness/DALL·E 2024-04-14 11.04.46 - A calm and focused fitness theme image for the body section of a Fitness website. This image should portray a Pilates class in a serene indoor studio.webp",
        "/gen/images/fitness/DALL·E 2024-04-14 11.04.48 - A calm and focused fitness theme image for the body section of a Fitness website. This image should portray a Pilates class in a serene indoor studio.webp",
        "/gen/images/fitness/DALL·E 2024-04-14 11.04.52 - A high-energy fitness theme image for the body section of a Fitness website. This image should show a group fitness class doing high-intensity interva.webp",
        "/gen/images/fitness/DALL·E 2024-04-14 11.04.54 - A calm and focused fitness theme image for the body section of a Fitness website. This image should depict a meditative stretching session in a peacef.webp",
        "/gen/images/fitness/DALL·E 2024-04-14 11.04.56 - A calm and focused fitness theme image for the body section of a Fitness website. This image should depict a meditative stretching session in a peacef.webp",
        # fnb
        "/gen/images/fnb/DALL·E 2024-04-14 11.05.14 - A rustic food theme hero image for a Food & Beverages website. The image should depict a farm-to-table dining experience, showcasing a wooden table fi.webp",
        "/gen/images/fnb/DALL·E 2024-04-14 11.05.17 - A modern food theme hero image for a Food & Beverages website. The image should feature a stylish, contemporary restaurant setting with an emphasis on.webp",
        "/gen/images/fnb/DALL·E 2024-04-14 11.05.19 - A rustic food theme image for the body section of a Food & Beverages website. The image should capture a cozy kitchen scene with a chef preparing a tr.webp",
        "/gen/images/fnb/DALL·E 2024-04-14 11.05.20 - A modern food theme image for the body section of a Food & Beverages website. The image should depict a high-tech kitchen with a chef using advanced c.webp",
        "/gen/images/fnb/DALL·E 2024-04-14 11.05.22 - A rustic food theme image for the body section of a Food & Beverages website. The image should depict an outdoor barbecue scene with a group of people.webp",
        "/gen/images/fnb/DALL·E 2024-04-14 11.05.23 - A modern food theme image for the body section of a Food & Beverages website. The image should capture an upscale cocktail bar scene with a skilled ba.webp",
        #health
        "/gen/images/health/DALL·E 2024-04-14 11.04.20 - A dark-themed hero image for a Health & Beauty website. The image should convey a serene and sophisticated atmosphere, featuring abstract representati.webp",
        "/gen/images/health/DALL·E 2024-04-14 11.04.22 - A jolly-themed hero image for a Health & Beauty website. This image should feature bright, cheerful visuals related to wellness and beauty, like color.webp",
        "/gen/images/health/DALL·E 2024-04-14 11.04.24 - A dark-themed image for the body section of a Health & Beauty website. The image should depict a tranquil spa setting with a focus on relaxation and l.webp",
        "/gen/images/health/DALL·E 2024-04-14 11.04.27 - A dark-themed image for the body section of a Health & Beauty website. The image should depict a tranquil spa setting with a focus on relaxation and l.webp",
        "/gen/images/health/DALL·E 2024-04-14 11.04.29 - A jolly-themed image for the body section of a Health & Beauty website. This image should capture the essence of a lively and vibrant spa experience. .webp",
        "/gen/images/health/DALL·E 2024-04-14 11.04.31 - A dark-themed image for the body section of a Health & Beauty website. The image should feature a sophisticated beauty salon environment with an empha.webp",
        "/gen/images/health/DALL·E 2024-04-14 11.04.32 - A jolly-themed image for the body section of a Health & Beauty website. The scene should depict a cheerful makeup tutorial session. Include a makeup a.webp",
        "/gen/images/health/DALL·E 2024-04-14 11.04.34 - A dark-themed image for the quote section of a Health & Beauty website. This image should feature an elegant, minimalistic design with a focus on a se.webp",
        "/gen/images/health/DALL·E 2024-04-14 11.04.36 - A jolly-themed image for the quote section of a Health & Beauty website. The image should depict a cheerful and uplifting beauty spa scene. Visual ele.webp",
        #home and decor
        "/gen/images/home and decor/DALL·E 2024-04-14 11.05.26 - A cozy home theme hero image for a Home & Decor website. The image should depict a warm, inviting living room with a crackling fireplace, plush sofas,.webp",
        "/gen/images/home and decor/DALL·E 2024-04-14 11.05.27 - A modern home theme hero image for a Home & Decor website. The image should feature a sleek, contemporary living room with large windows overlooking a.webp",
        "/gen/images/home and decor/DALL·E 2024-04-14 11.05.29 - A cozy home theme image for the body section of a Home & Decor website. The image should depict a quaint reading nook with a comfortable armchair, a k.webp",
        "/gen/images/home and decor/DALL·E 2024-04-14 11.05.30 - A modern home theme image for the body section of a Home & Decor website. The image should showcase an elegant home office with a striking contrast of.webp",
        "/gen/images/home and decor/DALL·E 2024-04-14 11.05.33 - A cozy home theme image for the body section of a Home & Decor website. The image should depict a charming kitchen with rustic decor, featuring an ant.webp",
        "/gen/images/home and decor/DALL·E 2024-04-14 11.05.35 - A modern home theme image for the body section of a Home & Decor website. This image should capture a luxurious bathroom setting with a minimalist des.webp",
        ]

        
    grid = rx.grid(
        rx.foreach(image_urls, img),
        columns="3",
        spacing="4",
    )
    
    return grid
