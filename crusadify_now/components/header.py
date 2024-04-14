import reflex as rx
from ..baseState import State

def header()->rx.Component:
    menu_visible = State.menu_visible
    print("meeee",menu_visible)
    return rx.box(
        rx.desktop_only(
           rx.hstack(
              rx.flex(
  rx.image(src="/logo.png", width="80px"),
                  rx.flex(
                                                      rx.button("Login",  on_click=lambda: rx.redirect('/login') ,style={"padding":"18px","width":"84px","margin":"12px","font-size":"18px","cursor":"pointer"}),
                                                        rx.button("Logout",style={"padding":"18px","width":"84px","margin":"12px","font-size":"18px"}),

                      
                  ),
                  style={"justify-content":"space-between","width":"100%","padding":"34px","align-items":"center"}
              )   
            
        ),
    ),
    rx.mobile_and_tablet(
rx.flex(
               rx.image(src="/hamburger.jpg", on_click=lambda:State.toggle_menu, style={"cursor": "pointer",},width="50px"),
            rx.image(src="/logo.png", width="80px"),
            justify="between"
),

        rx.cond(
            menu_visible,
rx.box(
            rx.vstack(
                               rx.image(src="/hamburger.jpg", on_click=lambda:State.toggle_menu, style={"cursor": "pointer",},width="50px"),
                                rx.button("Login",style={"padding":"6px","width":"64px","margin":"24px 0px"}),    
                          rx.button("Logout",style={"padding":"6px","width":"64px"}),    


            ),
             style={
            "position": "absolute",
            "top": "0",
            "left": "0",
            "width": "200px",  
            "height": "100%",
            "background-color": "#f0f0f0",
            "padding": "20px",
            "box-shadow": "2px 0 5px rgba(0, 0, 0, 0.2)",
            "z-index": "1000"
        }

        ),

        )
            
    
    )
    )
