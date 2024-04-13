import reflex as rx
from crusadify_now import style
from crusadify_now.template1.topNav import topNav
from crusadify_now.template1.header import header
from crusadify_now.template1.body import body
from crusadify_now.template1.footer import footer

def template1() -> rx.Component:
    # Variables
    primaryColor = "#EE8F4E"
    secondaryColor = "#7ACAA9"
    tertiaryColor = "#F1EBDC"

    logo = "/template1/logo.png"
    heroTxt = "A new kind of soda"
    heroSubTxt = "20+ refreshing flavours, with less sugar"
    heroBtnTxt = "Shop now"
    topNavItems = [{"label": "Home", "href": "/"}, {"label": "About", "href": "/about"}, {"label": "Contact", "href": "/contact"}, {"label": "Shop", "href": "/shop"}, {"label": "Blog", "href": "/blog"}]
    bodySection1Txt= "Seen the word COLD on our cans? \nWell, they're printed with a special thermo-reactive ink which means it changes colour to blue when the tasty beverage inside is NICE AND COLD. \nCheers science, you're a real pal."
    bodySection2Txt= "As well as being labelled 'THE BEST TASTING ONE' Pals are ALL-NATURAL, low in sugar, GLUTEN FREE, VEGAN FRIENDLY AND free from artificial colours, sweeteners, preservatives and ingredients you can’t pronounce. Basically, we’ve shown bad stuff the door and told good stuff to get on over here because the sun’s out, the music’s on and all our pals (with Pals) are here. "
    bodySection3Txt= "Our cans are filled with nothing but the best PREMIUM SPIRITS and REAL FRUIT extracts from prime fruit producing regions – to create one hell of a tasty drink. Like that drink you’d mix yourself if you could just get your hands on a clean glass, a couple of lemons and an award-winning mixologist."
    quote="We have always believed there is more to business than just offering a product or service."
    footerTxt = "Let's be pals!"
    storeUrl = "https://pals.com"

    return rx.vstack(
        topNav(logo, topNavItems, heroBtnTxt, storeUrl),
        header(heroTxt, heroSubTxt, heroBtnTxt, storeUrl),
        body(bodySection1Txt, bodySection2Txt, bodySection3Txt, quote, secondaryColor, tertiaryColor),
        footer(footerTxt, heroBtnTxt, logo, storeUrl),
        align="center",
        spacing="0",
        font_size="1.5em",
        width="100vw",
        background_color=primaryColor,
     )
     