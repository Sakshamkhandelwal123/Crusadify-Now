import anthropic
import os
from dotenv import load_dotenv




class CLAUDE: 
    def __init__(self):
        load_dotenv()
        self.api_key = os.getenv('CLAUDE_API_KEY')
        self.client = anthropic.Anthropic(api_key=self.api_key)

    def send_message(self, messages, model, max_tokens):
        try:
            message = self.client.messages.create(
                model=model,
                max_tokens=max_tokens,
                messages=messages
            )
            return message
        except Exception as e:
            print(f"Error: {e}")
            return None

    def get_response(self, messages, model, max_tokens):
        response = self.send_message(messages, model, max_tokens)
        if response:
            return response.content
        else:
            return "Unable to get a response from the Anthropic API."


if __name__ == "__main__":
    messages = [
        {"role": "user", "content": "What is Python used for?"},
        {"role": "assistant", "content": ""}
    ]
    model = "claude-3-opus-20240229"
    max_tokens = 1024

    claude = CLAUDE()
    response = claude.get_response(messages, model, max_tokens)
    print(response)
