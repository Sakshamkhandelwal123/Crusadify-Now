import reflex as rx

def footer()->rx.Component:
    return rx.flex(

     
              
  rx.heading("Stay in touch", style={"color":"#674743","font-size":"36px"}),
                  rx.flex(
                      rx.text("Privacy policy",style={"padding":"6px"}),
                      rx.text("Product updates",style={"padding":"6px"}),
                      rx.text("Terms of service",style={"padding":"6px"}),

                      
                  ),
                  style={"justify-content":"space-between","width":"100%","padding":"36px","align-items":"center"}
               
            
    
  )
