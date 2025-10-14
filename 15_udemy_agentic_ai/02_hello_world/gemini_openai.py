from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

client = OpenAI(
    api_key="AIzaSyBub2Qzn4M1nwAl8f46MsBvyurUxblWDpg",
    base_url="https://generativelanguage.googleapis.com/v1beta/"
)

response = client.chat.completions.create(
    model="gemini-2.5-flash",
    messages=[
        {"role": "user", "content": "Hello, There!"},
    ]
)

print(response.choices[0].message.content)