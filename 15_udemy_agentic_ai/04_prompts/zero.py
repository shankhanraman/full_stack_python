#  Zero Sot prompting
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

client = OpenAI(
    api_key="GOOGLE_API_KEY",
    base_url="https://generativelanguage.googleapis.com/v1beta/"
)

# Zero shot prompting : Direclty giving the inst to the model 
System_prompt = "You should only and only answer the coding questions Do not asnwer anything else . Your name is Alexa . If user asks something other than coding , just say sorry "

response = client.chat.completions.create(
    model="gemini-2.5-flash",
    messages=[
        {"role": "user", "content": System_prompt},
        {"role": "user", "content": " Can u tell me a write a python code to translate the sentence to Hindi "},
    ]
)

print(response.choices[0].message.content)
