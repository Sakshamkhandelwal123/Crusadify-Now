



import reflex as rx
import requests





class State(rx.State):
   

    menu_visible=False 
    
    def toggle_menu(self):
        self.menu_visible = not self.menu_visible
        

    
 



  