# few shot prompting 
#  Zero Sot prompting
from openai import OpenAI
from dotenv import load_dotenv
import json

load_dotenv()  # Load environment variables from .env file

client = OpenAI(
    api_key="AIzaSyBub2Qzn4M1nwAl8f46MsBvyurUxblWDpg",
    base_url="https://generativelanguage.googleapis.com/v1beta/"
)

# Zero shot prompting : Direclty giving the inst to the model 
System_prompt = """ 
You're an expert AI assistant in resolving user queries using chain of thought . 
You work START , PLAN , OUTPUT steps
You need to first PLAN what need s to be done. The PLAN can en multiple steps.
Once you think enough PLAN has been done , finally you can give an OUTPUT
Rules: 
- Strictly Follow the given JSON output format 
- Only run one step at a time.
- The sequence of steps is START (user gives an INPUT), PLAN(That can be multple times) and finally output (which is going to be displayed to the user).

Output JSON format :
{"step":"START" | "PLAN" | "OUTPUT","content":"string" }

EXAMPLE
START:  Hey . can u solve 2+3 * 5/10
PLAN :{"step": "PLAN","content":"Seems like user is interested in math problem" }
PLAN :{"step": "PLAN","content":"looking at the problem , we should solve this using BODMAS rule" }
PLAN :{"step": "PLAN","content":"Yes the BODMAS is corrdct thing to be done here" }
PLAN :{"step": "PLAN","content":"First we multiply 3*5 which is 15" }
PLAN :{"step": "PLAN","content":"Now the new equation is 2+15 /10" }
PLAN :{"step": "PLAN","content":"We must perform divide that is 15 /10 = 1.5" }
PLAN :{"step": "PLAN","content":"Great we have finally solved and finally left with 3.5 as ans" }
PLAN :{"step": "PLAN","content":"Great we have solved and left with 3.5 as answer" }
OUTPUT:{"step": "PLAN","content":"3.5" }

"""
print("/n/n")
message_history = [
    {"role": "system","content": System_prompt}
]

user_query = input("Enter")
message_history.append({"role":"user", "content": user_query})

while True:
    response = client.chat.completions.create(
        model="gemini-2.5-flash",
        response_format={"type":"json_object"},
        messages=message_history
    )

    raw_result = response.choices[0].message.content
    message_history.append({"role": "assistant", "content": raw_result})
    parsed_result = json.loads(raw_result)

    if parsed_result.get("step")=="START":
        print("..",parsed_result.get("content"))
        continue

    if parsed_result.get("step")=="PLAN":
        print("..",parsed_result.get("content"))
        continue

    if parsed_result.get("step")=="OUTPUT":
        print("..",parsed_result.get("content"))
        break

print(response.choices[0].message.content)

print("/n/n")
