from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file
client = OpenAI()

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {
            "role": "system",
            "content": "You are expert in Maths and only ans maths related questions.",
        },
        {"role": "user", "content": "Hello, There! can you help me solve the a+b whole square?"},
    ]
)
print(response.choices[0].message.content)