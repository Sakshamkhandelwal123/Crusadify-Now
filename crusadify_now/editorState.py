import reflex as rx
import requests

class EditorState(rx.State):

    primaryColor = "#EE8F4E"
    secondaryColor = "#7ACAA9"
    tertiaryColor = "#F1EBDC"

    logo = "/template1/logo.png"
    heroTxt = '<span style="font-size: 72px"><strong>A new kind of soda</strong></span>'
    heroSubTxt = '<span style="font-size: 26px">20+ refreshing flavours, with less sugar</span>'
    heroBtnTxt = "Shop now"
    heroImg = "/template1/beige.png"
    topNavItems = [{"label": "Home", "href": "/"}, {"label": "About", "href": "/about"}, {"label": "Contact", "href": "/contact"}, {"label": "Shop", "href": "/shop"}, {"label": "Blog", "href": "/blog"}]
    bodySection1Txt= '<span style="font-size: 26px">Seen the word COLD on our cans? \nWell, they’re printed with a special thermo-reactive ink which means it changes colour to blue when the tasty beverage inside is NICE AND COLD. \nCheers science, you’re a real pal.</span>'
    bodySection1Img = "/template1/single-can.webp"
    bodySection2Txt= '<span style="font-size: 26px">As well as being labelled ’THE BEST TASTING ONE’ Pals are ALL-NATURAL, low in sugar, GLUTEN FREE, VEGAN FRIENDLY AND free from artificial colours, sweeteners, preservatives and ingredients you can’t pronounce. Basically, we’ve shown bad stuff the door and told good stuff to get on over here because the sun’s out, the music’s on and all our pals (with Pals) are here.</span>'
    bodySection2Img = "/template1/multiple-cans.webp"
    bodySection3Txt= '<span style="font-size: 26px">Our cans are filled with nothing but the best PREMIUM SPIRITS and REAL FRUIT extracts from prime fruit producing regions – to create one hell of a tasty drink. Like that drink you’d mix yourself if you could just get your hands on a clean glass, a couple of lemons and an award-winning mixologist.</span>'
    bodySection3Img = "/template1/pour-purple.webp"
    quote="We have always believed there is more to business than just offering a product or service."
    footerTxt = '<span style="font-size: 72px"><strong>Let’s be pals!</strong></span>'
    storeUrl = "https://pals.com"

    currentKey = ""

    content: str = ""

    def handle_change(self, content: str):
        """Handle the editor value change."""
        self.content = content
        setattr(self, self.currentKey, self.content)
        print (self.content)

    def set_content(self, content: str, key: str):
        """Handle the editor value change."""
        self.content = content
        self.currentKey = key
        setattr(self, key, self.content)
        print (self.currentKey, self.content)

    def set_quote(self, quote: str):
        """Handle the editor value change."""
        self.quote = quote

    def set_bodySectionImg(self, img: str):
        """Handle the editor value change."""
        self.content = img
        setattr(self, self.currentKey, self.content)
    