# Pesona based prompting 
from openai import OpenAI
from dotenv import load_dotenv

import json

load_dotenv()  # Load environment variables from .env file

client = OpenAI()

System_prompt = """ 
You are an AI assistant named Piyush garg.
You are acting on behalf of Piyush Garg who is 25 year old tech enthusisastic and principle engineer . Your main stack is JS and Python and You are leaning GenAI these days.

Examples :
Q: Hey 
A. Hey, whats up!
(100-150 examples)

"""

response = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {"role": "system", "content": System_prompt},
        {"role": "user", "content": " Hey, There"},
    ]
)

print("Response", response.choices[0].message.content)


