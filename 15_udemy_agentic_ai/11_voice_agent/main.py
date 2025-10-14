import speech_recognition as sr
from openai import OpenAI
from dotenv import load_dotenv
from openai import AsyncOpenAI
from openai.helpers import LocalAudioPlayer
import asyncio

load_dotenv()

client = OpenAI()
async_client = AsyncOpenAI()

async def tts(speech:str):
    async with async_client.audio.speech.with_streaming_response.create(
        model="gpt-4o-mini-tts",
        voice="coral",
        instructions="Always speak in a cheerful manner with full of delight and happy",
        input=speech,
        response_format="pcm",
    )as response:
        await LocalAudioPlayer().play(response)

def main():
    r = sr.Recognizer()

    with sr.Microphone as source:
        r.adjust_for_ambient_noise(source)
        r.pause_threshold = 2

        print("Spek something ...")
        audio = r.listen(source)

        print("Processing audio ...(STT)")
        stt = r.recognize_google(audio)

        print("You said :", stt)

        SYSTEM_PROMPT = f"""
        You are an expert voice agent. You are given transcript of what user has said using voice. You need to output as if you are an voice agent and whatever you
        speak will be converted back to audio using using AI and played bakc to user.


        """

        response =client.chat.completions.create(
            model="gpt4.1",
            messages=[
                {"role":"system","content": SYSTEM_PROMPT},
                {"role":"user","content": stt}
            ]
        )
        print(f"AI response :{response.choices[0].message.content}")
        asyncio.run(tts(speech=response.choices[0].message.content))

main()
