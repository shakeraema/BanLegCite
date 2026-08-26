import os
from dotenv import load_dotenv
from openai import OpenAI

# 1. Load the API key from your .env file
load_dotenv()
api_key = os.getenv("OPENROUTER_API_KEY")

if not api_key:
    print("Error: OPENROUTER_API_KEY not found in .env file")
    exit(1)

# 2. Initialize the client using OpenRouter's base URL
client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=api_key,
)

import time

print("Sending request to z-ai/glm-5.2:free...\n")

max_retries = 5
for attempt in range(max_retries):
    try:
        response = client.chat.completions.create(
            model="z-ai/glm-5.2:free",
            messages=[
                {
                    "role": "user",
                    "content": "What is the capital of Bangladesh and what is its highest court?"
                }
            ],
            extra_headers={
                "HTTP-Referer": "https://github.com/ZahidHasan7/BanLegit-Cite",
                "X-Title": "BanLegit-Cite Research"
            }
        )
        print("Success! Live Response received from OpenRouter API:")
        print(response.choices[0].message.content)
        break
    except Exception as e:
        print(f"Attempt {attempt+1}: {e}. Retrying in 6 seconds...")
        time.sleep(6)

print(response.choices[0].message.content)
