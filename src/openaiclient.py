"""
    Uses OPENAI API to generate responses 
"""

import os

import dotenv
from openai import OpenAI

dotenv.load_dotenv("./env")

API_KEY = os.environ["OPENAI-API-KEY"]

# connecting with openai client
client = OpenAI(api_key=API_KEY)

