from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI()

response = client.chat.completions.create(
    model="gpt-4-vision-preview",
    messages=[
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": "Generate a caption for this image in about 50 words"
                },
                {
                    "type": "image_url",
                    "image_url": {
                        "url": "https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.istockphoto.com%2Fstock-photos%2Fnature-and-landscapes&psig=AOvVaw10X16xOe8c_sFkc3GAs0Tp&ust=1760232142280000&source=images&cd=vfe&opi=89978449&ved=0CBIQjRxqFwoTCKD0ge39mpADFQAAAAAdAAAAABAE"
                    }
                }
            ]
        }
    ]
)