#Agentic (Tool calling)
from openai import OpenAI
from dotenv import load_dotenv
import json
import requests
from pydantic import BaseModel,Field
from typing import Optional
import os 

from openai import AsyncOpenAI
from openai.helpers import LocalAudioPlayer
import asyncio
import speech_recognition as sr

async_client = AsyncOpenAI()


load_dotenv()  # Load environment variables from .env file

async def tts(speech:str):
    async with async_client.audio.speech.with_streaming_response.create(
        model="gpt-4o-mini-tts",
        voice="coral",
        instructions="Always speak in a cheerful manner with full of delight and happy",
        input=speech,
        response_format="pcm",
    )as response:
        await LocalAudioPlayer().play(response)

r = sr.Recognizer()

with sr.Microphone as source:
    r.adjust_for_ambient_noise(source)
    


def get_weather(city: str):
    url = f"https://wttr.in/{city.lower()}?format=%C+%t"
    response = requests.get(url)
    if response.status_code == 200:
        return f"The weather in {city} is {response.text}"
    
    return "Something went wrong"

def run_command(cmd:str):
    result = os.system(cmd)
    return result

available_tools ={
    "get_weather" : get_weather,
    "run_command" : run_command
}
client = OpenAI()

# Zero shot prompting : Direclty giving the inst to the model 
System_prompt = """ 
You're an expert AI assistant in resolving user queries using chain of thought . 
You work START , PLAN , OUTPUT steps
You need to first PLAN what need s to be done. The PLAN can en multiple steps.
Once you think enough PLAN has been done , finally you can give an OUTPUT
You can also cll a tool if required from the list of available tools.
for every tool call wait for the observe step which is output from the called tool. 

Rules: 
- Strictly Follow the given JSON output format 
- Only run one step at a time.
- The sequence of steps is START (user gives an INPUT), PLAN(That can be multple times) and finally output (which is going to be displayed to the user).

Output JSON format :
{"step":"START" | "PLAN" | "OUTPUT" | "TOOL","content":"string", "tool":"string", "input":"string" }

Available Tools:
-get_weather(city:str): Takes city name as an input string and returns the weather info about the city.
-run_command(cmd:str): Takes a system linux command as string and executes  the user's system and return the output from the command.


EXAMPLE 1
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

EXAMPLE 2:
START:  What is the weather of delhi ?
PLAN :{"step": "PLAN","content":"Seems like user is interested in getting weather of Delhi in India" }
PLAN :{"step": "PLAN","content":"looking at the problem , we should solve this using BODMAS rule" }
PLAN :{"step": "PLAN","content":"Lets see if we have any availabel tool from the list of availabel tools" }
PLAN :{"step": "PLAN","content":"Great , we have get_weather tool available for this query " }
PLAN :{"step": "TOOL","tool":"get_weather" ,"input":"delhi" }
PLAN :{"step": "OBSERVE","tool":"get_weather" ,"output":"The temp of delhi is cloudy with 20º C" }
PLAN :{"step": "PLAN","content":"Great I got the weather info about delhi " }
OUTPUT:{"step": "OUTPUT","content":"The cuurent wweather in delhi is  20º C The temp of delhi with some cloudy " }

"""
print("/n/n")

class MyOutputFormat(BaseModel):
    step: str = Field(..., description="The ID of the step.Example: PLAN, OUTPUT, TOOL")
    content: Optional[str] = Field(None , description="The optional string content for the step")
    tool: Optional[str] = Field(None , description="The ID of the tool to call")
    input: Optional[str] = Field(None , description= "The input params of the tool")

message_history = [
    {"role": "system","content": System_prompt}
]

while True:
    user_query = input("Enter")
    message_history.append({"role":"user", "content": user_query})

    while True:
        response = client.chat.completions.parse(
            model="gpt-4o",
            response_format=MyOutputFormat,
            messages=message_history
        )

        raw_result = response.choices[0].message.content
        message_history.append({"role": "assistant", "content": raw_result})
        
        parsed_result = response.choices[0].message.parsed

        if parsed_result.step=="START":
            print("..",parsed_result.content)
            continue

        if parsed_result.step=="TOOL":
            tool_to_call=parsed_result.tool
            tool_input = parsed_result.input
            print(f".. {tool_to_call}({tool_input})")
            
            tool_response = available_tools[tool_to_call](tool_input)
            print(f"..:{tool_to_call}({tool_input})= {tool_response}")
            message_history.append({"role":"developer","content":json.dumps(
                {"step":"OBSERVE","tool":tool_to_call,"input":tool_input,"output":tool_response}
            )})
            continue

        if parsed_result.step=="PLAN":
            print("..",parsed_result.content)
            continue

        if parsed_result.step=="OUTPUT":
            print("..",parsed_result.content)
            break

    print(response.choices[0].message.content)

    print("/n/n")
