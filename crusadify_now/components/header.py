import reflex as rx

def header()->rx.Component:
    return rx.desktop_only(
           rx.hstack(
              rx.flex(
  rx.image(src="/logo.png", width="80px"),
                  rx.flex(
                      rx.text("Products",style={"padding":"6px"}),
                      rx.text("Resources",style={"padding":"6px"}),
                      rx.text("Company",style={"padding":"6px"}),
                      rx.text("Pricing",style={"padding":"6px"}),
                      rx.text("Partner",style={"padding":"6px"}),
                      rx.text("Community",style={"padding":"6px"}),
                      
                  ),
                  style={"justify-content":"space-between","width":"100%","padding":"34px","align-items":"center"}
              )   
            
        ),
    )
