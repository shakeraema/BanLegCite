import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
api_key = os.getenv("OPENROUTER_API_KEY")

if not api_key:
    print("Error: OPENROUTER_API_KEY not found in .env file")
    exit(1)

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=api_key,
)

prompt = """
You are an expert in Bangladesh Law. We are building a dataset of statutory legal citations.
Please provide 3 landmark, highly-cited sections from the Penal Code, 1860 and 3 from the Code of Criminal Procedure, 1898 (CrPC).
For each section, provide:
1. The exact section number and Act name (e.g., Section 302 of the Penal Code, 1860).
2. The core legal principle/holding of that section in one sentence.
3. A real existing Bangladesh Supreme Court case that frequently cites this section (if possible).
Format clearly.
"""

print("Asking GLM-5.2 for statutory sections and cases...\n")

response = client.chat.completions.create(
    model="z-ai/glm-5.2:free",
    messages=[{"role": "user", "content": prompt}],
    extra_headers={
        "HTTP-Referer": "https://github.com/ZahidHasan7/BanLegit-Cite",
        "X-Title": "BanLegit-Cite Research"
    }
)

print(response.choices[0].message.content)
