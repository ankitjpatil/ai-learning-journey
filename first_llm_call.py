from openai import OpenAI
from dotenv import load_dotenv
import os

# Load your token from .env file
load_dotenv()

# Connect to GitHub Models (free)
client = OpenAI(
    api_key=os.getenv("GITHUB_TOKEN"),
    base_url="https://models.inference.ai.azure.com"
)

# Send your first message to an LLM
response = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {
            "role": "system",
            "content": "You are a helpful assistant for an AI student learning GenAI development in Canada."
        },
        {
            "role": "user",
            "content": "What is the difference between a token and a parameter in an LLM"
        }
    ]
)

# Print the response
print("\n--- LLM Response ---")
print(response.choices[0].message.content)
print("--------------------\n")