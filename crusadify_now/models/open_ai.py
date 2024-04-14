import os
from dotenv import load_dotenv
from openai import OpenAI

schema = {
  "type": "object",
  "properties": {
    "primaryColor": {"type": "string"},
    "secondaryColor": {"type": "string"},
    "tertiaryColor": {"type": "string"},
    "logo": {"type": "string"},
    "hero": {
      "type": "object",
      "properties": {
        "text": {"type": "string"},
        "subtext": {"type": "string"},
        "image": {"type": "string"}
      }
    },
    "bodySections": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "img": {"type": "string"},
          "text": {"type": "string"}
        }
      }
    },
    "quote": {"type": "string"},
    "storeUrl": {"type": "string"},
    "storeName": {"type": "string"}
  },
  "required": ["primaryColor", "secondaryColor", "tertiaryColor", "logo", "hero", "bodySections", "quote", "storeUrl", "storeName"]
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
        # Create a system message to define the assistant's behavior
        system_message = "You are a dynamic content generator, skilled in creating structured responses for web content based on provided tags, names, and descriptions."

        # Generate the header based on the name and tag
        header = f"Welcome to {name}, the {tag} leader!"

        # Use the description and Shopify details to create the body section
        body_section = f"Explore our unique offerings like {', '.join(shopify_store_details['productTypes'])}. {description}"

        # Construct a footer from Shopify store details
        footer = f"Managed by {shopify_store_details['ownerName']} of {shopify_store_details['storeName']}."

        # Create a user prompt to guide the content generation
        user_prompt = {
            "role": "user",
            "content": f"Generate a json for a web page web page with a header: '{header}', a body section: '{body_section}', and a footer: '{footer}'. you can include relevant images. and make sure the content is engaging and informative. also, consider the tag: '{tag}'. make sure the content is structured and visually appealing. You can make changes to the content as needed. follow this schema to he t, fill all the details in the schema. {schema}"
        }

        print(user_prompt)

        # Call the OpenAI API
        completion = self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": system_message},
                user_prompt
            ]
        )

        return completion.choices[0].message['content']

# Example usage:
if __name__ == "__main__":
    # Initialize the content generator with the OpenAI client
    openai = OpenAi()
    
    response = openai.generate_content("tech", "InnovateTech", "Innovate with us and explore cutting-edge technology solutions.", {"storeName": "InnovateStore", "ownerName": "Alex Doe", "productTypes": ["electronics", "software"]})
    
    print(response)