import os
import requests
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("AGENTROUTER_API_KEY")

models_to_test = ["glm-5.3", "gpt-5.6-sol", "claude-opus-5", "claude-opus-4-8", "deepseek-v4-flash"]
headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json",
    "User-Agent": "RooCode/3.0.0"
}

url = "https://agentrouter.org/v1/chat/completions"

print("Testing AgentRouter Models with RooCode User-Agent...")
for m in models_to_test:
    payload = {
        "model": m,
        "messages": [{"role": "user", "content": "Respond with 'OK'."}]
    }
    try:
        r = requests.post(url, headers=headers, json=payload, timeout=15)
        res = r.json()
        if "choices" in res:
            print(f"✅ Model {m}: SUCCESS -> {res['choices'][0]['message']['content'].strip()[:60]}")
        else:
            print(f"⚠️ Model {m}: Response -> {res}")
    except Exception as e:
        print(f"❌ Model {m}: Error -> {e}")


