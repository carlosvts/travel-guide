"""
    Uses OPENAI API to generate responses 
"""

import os

import dotenv
from openai import OpenAI

dotenv.load_dotenv()

API_KEY = os.environ["OPENAI-API-KEY"]

if not API_KEY:
    raise ValueError("OpenAI API key not found")


class MyOpenAI():
    """
        Connects with openai api and generate responses    
    """

    def __init__(self, api_key=API_KEY) -> None:
        # connecting with openai client
        self.api_key = api_key
        self.client = OpenAI(api_key=self.api_key)

    def get_ai_response(self, prompt="write a test message") -> str:
        response = self.client.responses.create(
            model="gpt-4o",
            input=[
                {"role": "user", "content": prompt}
                ]
        )

        # return response.output_text
        return "teste"
    
if __name__ == "__main__":
    foo = MyOpenAI()

    msg = foo.get_ai_response()

    print(msg)