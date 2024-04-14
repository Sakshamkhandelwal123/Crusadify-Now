import reflex as rx


@rx.page(route="/dashboard")
def dashboard():
    return rx.vstack(
        rx.flex(
            rx.link(
                rx.button(
                    "Logout",
                ),
                href="/login",
                # todo: clear cookie
            ),
            justify_content="end",
            align_items="center",
            width="100%",
            padding="36px",
        ),
        rx.flex(
            rx.card(
                rx.heading(
                    "Shopify Metafields",
                    style={
                        "padding": "12px",
                    },
                ),
                rx.text(
                    "Instant sections will work with all Shopify Metafields, so retailers can easily enhance their online store aesthetics.",
                    style={"padding": "12px"},
                ),
                rx.image(src="/tags.png", style={"padding-top": "24px"}),
                style={
                    "height": "300px",
                    "padding": "20px",
                    "border-radius": "10px",
                    "box-shadow": "0px 4px 6px rgba(0, 0, 0, 0.1)",
                    "background-color": "#E9F6EF",
                },
                width=["100%", "40%", "40%", "30%", "30%"],
            ),
            rx.card(
                rx.heading(
                    "Clean Liquid export",
                    style={
                        "padding": "12px",
                    },
                ),
                rx.text(
                    "Published sections are converted into Liquid code, including the “schema” needed for use with the Shopify editor.",
                    style={"padding": "12px"},
                ),
                style={
                    "height": "300px",
                    "padding": "20px",
                    "border-radius": "10px",
                    "box-shadow": "0px 4px 6px rgba(0, 0, 0, 0.1)",
                    "background-color": "#E8E9F6",
                },
                width=["100%", "40%", "40%", "30%", "30%"],
            ),
            rx.card(
                rx.heading(
                    "Shopify Markets support",
                    style={
                        "padding": "12px",
                    },
                ),
                rx.text(
                    "Sections built with Instant will work seamlessly with all of the Shopify Market features, such as translations.",
                    style={"padding": "12px"},
                ),
                style={
                    "height": "300px",
                    "padding": "20px",
                    "border-radius": "10px",
                    "box-shadow": "0px 4px 6px rgba(0, 0, 0, 0.1)",
                    "background-color": "#E9F6EF",
                },
                width=["100%", "40%", "40%", "30%", "30%"],
            ),
            spacing="3",
            align_items="center",
            flex_wrap="wrap",
            width="100%",
            padding="36px",
            justify="center",
        ),
        rx.card(
            rx.flex(
                rx.flex(
                    rx.heading(
                        "My sites",
                        margin_left="20px",
                        style={
                            "font-size": "36px",
                            "line-height": "1.2",
                        },
                    ),
                    width=["100%", "100%", "100%", "50%", "50%"],
                ),
                rx.button(
                    "Create new site",
                    padding="16px",
                    margin_right="20px",
                ),
                justify="center",
                align_items="center",
            ),
            rx.cond(
                False == True,
                rx.text("Render List"),
                # rx.foreach(
                #     State.pagesList,
                #     lambda page: rx.hstack(
                #         rx.flex(
                #             rx.heading(page["page_name"]),
                #             style={
                #                 "align-items": "center",
                #                 "justify-content": "center",
                #             },
                #         ),
                #         style={"justify-content": "space-between"},
                #         width="100%",
                #     ),
                #     spacing="1",
                # ),
                rx.flex(
                    rx.heading(
                        "No pages yet.",
                        padding="36px",
                    ),
                    justify_content="center",
                    align_items="center",
                ),
            ),
            style={
                "margin-top": "36px",
                "width": "100%",
                "background-color": "#F8FDB7",
            },
        ),
    )