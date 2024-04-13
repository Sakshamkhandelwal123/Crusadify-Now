import reflex as rx

def footer()->rx.Component:
    return rx.flex(        
  rx.heading("Stay in touch", style={"color":"#674743","font-size":"36px", "@media (max-width: 768px)": {
                "justify-content": "center" ,
                "padding-bottom":"20px",
            },
           
            }, width=["100%","100%","50%","50%","50%"],  
             justify_content="start",
             align_items="center",
             display="flex",
             ),
                  rx.flex(
                      rx.text("Privacy policy",style={"padding":"6px"}),
                      rx.text("Product updates",style={"padding":"6px"}),
                      rx.text("Terms of service",style={"padding":"6px"}),   
                       width=["100%","100%","50%","50%","50%"] ,
                                 justify="end",
                                  style={
            "@media (max-width: 768px)": {
                "justify-content": "center",
                "padding-bottom":"36px",
            },

            },
                        align_items="center",
                        
                  ),
                  style={"justify-content":"space-between","width":"100%","padding":"36px","align-items":"center"}, 
                  flex_wrap="wrap",
                 padding="20px 36px"
                 
               
                  
  )
