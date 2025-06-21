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
        self.prompt = params
        self._origin = params[0]
        self._city = params[1]
        self._start_date = params[2]
        self._end_date = params[3]
        self._budget = params[4]
        self._travelers = params[5]
        self._interest = params[6]
        self._custom_note = params[7]

        if self._interest is None:
            self._interest = "Anything"

        if self._custom_note is None:
            self._custom_note = ""

        response = self.client.chat.completions.create(
            model="gpt-4o",
            max_tokens= 600,
            messages=[
                {
                    "role": "user",
                    "content": (
                        f'''

                        Generate a travel itinerary for {self._travelers} people
                        to {self._city}, the travel will start at
                        {self._start_date} and end at {self._end_date}.
                        The budget for this travel is {self._budget} dollars.
                        My places of interests are {self._interest}.
                        Also, {self._custom_note}

                        Your answer should be up to date and as short as possible
                        Your answer will be placed in a terminal, so add some 
                        colors using ANSI escape code
                        to make it prettier and easy to read



                        If your token limit didnt exceeded, generate a ascii art
                        to emphasize this travel
                        '''
                    )
                }
            ]

        )

        # return response.output_text
        return response.choices[0].message.content


if __name__ == "__main__":
    foo = MyOpenAI()

    msg = foo.get_ai_response()

    print(msg)