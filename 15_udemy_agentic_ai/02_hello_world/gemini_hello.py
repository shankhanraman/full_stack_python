from google import genai
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Get the API key from environment
api_key = os.getenv("GEMINI_API_KEY")

# Initialize the client
client = genai.GenerativeModel(model="gemini-2.5-flash", api_key=api_key)

# Generate content
response = client.generate_content(
    contents=[{"role": "user", "parts": ["Explain how AI works in a few words"]}]
)

# Print the response
print(response.text)