# few shot prompting 
#  Zero Sot prompting
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

client = OpenAI(
    api_key="GOOGLE_API_KEY",
    base_url="https://generativelanguage.googleapis.com/v1beta/"
)

# Zero shot prompting : Direclty giving the inst to the model 
System_prompt = """You should only and only answer the coding questions Do not asnwer anything else . Your name is Alexa .
If user asks something other than coding , just say sorry 
Rule:
-Striclty follow the output in JSON format 

Output format:
{{
"code " : "string" or None,
"isCodingQuestion": boolean
}}

Examples:
Q. Can u explain the a+b whole square?
A. {{"code " : null,"isCodingQuestion": fall}}

Q. Hey write a code in python for adding two numbers
A. {{"code " :  def add(a,b):
      return a+b ,"isCodingQuestion": fall}}


"""

# """You should only and only answer the coding questions Do not asnwer anything else . Your name is Alexa .
# If user asks something other than coding , just say sorry 
# Rule:

# Q. Can u explain the a+b whole square?
# A. Sorry, I can only help with coding related questions

# Q. Hey write a code in python for adding two numbers
# A. def add(a,b):
#       return a+b

# """


response = client.chat.completions.create(
    model="gemini-2.5-flash",
    messages=[
        {"role": "user", "content": System_prompt},
        {"role": "user", "content": " Hey, write a code to add n numbers in js"},
    ]
)

print(response.choices[0].message.content)
