"""
    Uses OPENAI API to generate responses 
"""

import os

import dotenv
from openai import OpenAI

dotenv.load_dotenv()

API_KEY = os.environ["OPENROUTER-AI-KEY"]

if not API_KEY:
    raise ValueError("OpenAI API key not found")


class MyOpenAI():
    """
        Connects with openai api and generate responses    
    """

    def __init__(self, api_key=API_KEY) -> None:
        # connecting with openai client
        self.api_key = api_key
        self.client = OpenAI(
            api_key=self.api_key,
            base_url="https://openrouter.ai/api/v1",
            )

    # TODO gerar o prompt, refatorar a lógica content fstrings etc
    def get_ai_response(self, params=list[str | list]) -> str:
    #    self.prompt = params
    #    self._city = self.prompt[0]
    #    self._start_date, self._end_date = self.prompt[1], self.prompt[2]
    #    self._budget = self.prompt[3]

        response = self.client.chat.completions.create(
            model="gpt-4o",
            max_tokens= 300,
            messages=[
                {
                    "role": "user",
                    "content": f"Generate a travel itinerary to paris"
                }
            ]

        )

        # return response.output_text
        return response.choices[0].message.content
    
if __name__ == "__main__":
    foo = MyOpenAI()

    msg = foo.get_ai_response()

    print(msg)