import reflex as rx

def mainSection()->rx.Component:
    return    rx.box(
            rx.flex(
            rx.flex(
            rx.heading("Build with complete freedom",style={"padding":"24px 0px"}),
            rx.text("Are you tired of wrestling with complex code to create the perfect Shopify store? Look no further than Instant – the revolutionary all-visual builder that empowers you to craft stunning, pixel-perfect pages without writing a single line of code."),
            rx.text("With Instant, you can bid farewell to the frustrations of coding and embrace the freedom of visual design. Our intuitive drag-and-drop interface puts the power of creation right at your fingertips, allowing you to effortlessly arrange elements, customize layouts, and bring your vision to life with unparalleled ease."),
            rx.text("Envision Your Dream Store, Realized"),
            rx.text("Instant's all-visual builder is a true game-changer, offering an unparalleled level of control and flexibility. Whether you're looking to create a captivating home page, an immersive product showcase, or a seamless checkout experience, our feature-rich platform has everything you need to make your dream store a reality."),
           width=["100%","100%","100%","50%","50%"],

           style={"flex-direction":"column"}
            ),
           rx.image(src="/template.png",width=["100%","100%","100%","40%","40%"],padding=["40px 0px","40px 0px","40px 0px","0px"]),
            style={"padding":"56px","flex-wrap":"wrap"},
            align_items="center",
                       justify="between",
                    
        ),
        rx.flex( rx.text("Features",style={"padding":"12px","color":"#0199B9","font-weight":"600"}),
                rx.heading("And there’s more! ",style={"padding":"12px",}),
                rx.text("Crusader's feature set is constantly growing, just like the possibilities of what you can achieve.",style={"padding":"12px","font-weight":"bold","text-align":"center"}),
                justify="center",
                align_items="center",
                
                style={"flex-direction":"column"}
                ),

        rx.flex(
    rx.card(

rx.heading("Shopify Metafields",style={"padding":"12px",}),
rx.text("Instant sections will work with all Shopify Metafields, so retailers can easily enhance their online store aesthetics.",style={"padding":"12px"}), 
                 rx.image(src="/tags.png",style={"padding-top":"24px"}),
         
            style={"height":"300px", "padding": "20px", "border-radius": "10px", "box-shadow": "0px 4px 6px rgba(0, 0, 0, 0.1)","background-color":"#E9F6EF"},        
        width=["100%","40%","40%","30%","30%"]
     ),
       rx.card(

rx.heading("Clean Liquid export",style={"padding":"12px",}),
rx.text("Published sections are converted into Liquid code, including the “schema” needed for use with the Shopify editor.",style={"padding":"12px"}), 

         
            style={"height":"300px", "padding": "20px", "border-radius": "10px", "box-shadow": "0px 4px 6px rgba(0, 0, 0, 0.1)","background-color":"#E8E9F6"},        
        width=["100%","40%","40%","30%","30%"]
     ),
  rx.card(

rx.heading("Shopify Markets support",style={"padding":"12px",}),
rx.text("Sections built with Instant will work seamlessly with all of the Shopify Market features, such as translations.",style={"padding":"12px"}), 

            style={"height":"300px", "padding": "20px", "border-radius": "10px", "box-shadow": "0px 4px 6px rgba(0, 0, 0, 0.1)","background-color":"#E9F6EF"},        
        width=["100%","40%","40%","30%","30%"]
     ),
    spacing="3",
    align_items="center",
    flex_wrap="wrap",
    width="100%",
    padding="36px",
    justify="center"
),
   rx.card(
        rx.flex(
        rx.flex(
            rx.heading("Unlock the Power of Conversion Optimization with A/B Testing",style={"padding":"36px","font-size":"36px","line-height":"1.2"}),
rx.text("A/B testing empowers you to make data-driven decisions, eliminating the guesswork and intuition-based approaches that can often lead to suboptimal results. By systematically testing and analyzing various elements, such as headlines, calls-to-action, layouts, or copy, you can identify the winning variations that resonate most effectively with your target audience.",
        style={"padding":"0px 36px"}),
style={"flex-direction":"column",},
width=["100%","100%","100%","50%","50%"]
        ),
         rx.image(src="/shopify.png",width=["100%","100%","100%","50%","50%"], style={"padding":"36px"}),
           justify="between",
         flex_wrap="wrap",  
    ),
         style={"margin-top":"36px","background-color":"#F8FDB7",},

   ),
   
   )