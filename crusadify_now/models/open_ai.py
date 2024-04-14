import os
from dotenv import load_dotenv
from openai import OpenAI
import json

schema = {
    "primaryColor": "",
    "secondaryColor": "",
    "tertiaryColor": "",
    "heroTxt": "",
    "heroSubTxt": "",
    "bodySection1Txt": "",
    "bodySection2Txt": "",
    "bodySection3Txt": "",
    "quote": "",
    "footerTxt": "",
  }


class OpenAi:
    def __init__(self):
        load_dotenv()
        self.api_key = os.getenv('OPEN_AI_API_KEY')
        self.client = OpenAI(api_key=self.api_key)

    def generate_content(self, tag, description, name=None, shopify_store_details=None):
        # Provide default values if none are provided
        if name is None:
            name = "GenericStore"

        if shopify_store_details is None:
            shopify_store_details = {
                "storeName": f"{tag}",
                "ownerName": f"{name} Doe",
                "productTypes": ["products", "services"]
            }

        print('generating prompt...')
        # Create a system message to define the assistant's behavior
        system_message = "You are a dynamic content generator, skilled in creating structured responses for web content based on provided tags, names, and store details. keep in mind that the colors should be in hex format. the hero text should be engaging and informative. the quote should be inspiring and memorable. the footer text should be a call to action."

        # Create a user prompt to guide the content generation
        user_prompt = {
            "role": "user",
            "content": f"Generate a json for a web page web page using these details: { shopify_store_details} {tag} {name} {description}.  with a header, a body section: with 3 separate sections, and a footer. make sure the content is engaging and informative. also, consider the tag: '{tag}'. make sure the content is structured and visually appealing. fill all the details in the schema: {schema}.  don't include any unnecessary details just fill the details i have asked from you in the schema i have provided."
        }

        print('calling...')

        # Call the OpenAI API to generate the content
        # model types use as needed
        # model="gpt-3.5-turbo",
        # model="gpt-4", 
        completion = self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            response_format={ "type": "json_object" },
            
            messages=[
                {"role": "system", "content": system_message},
                user_prompt
            ]
        )


        print('called...')

        return completion.choices[0].message.content

# Example usage:
if __name__ == "__main__":
    # Initialize the content generator with the OpenAI client
    openai = OpenAi()    
    
    response = openai.generate_content("health", "A store that sells health products", "John", {"storeName": "HealthStore", "ownerName": "John Doe", "productTypes": ["health products", "supplements"]})

    print(response)