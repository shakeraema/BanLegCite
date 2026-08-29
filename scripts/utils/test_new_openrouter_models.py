import os
import requests
import json
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("OPENROUTER_API_KEY")

headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json",
    "HTTP-Referer": "https://github.com/shakeraema/BanLegCite",
    "X-OpenRouter-Title": "BanLegitCite-Benchmark"
}

url = "https://openrouter.ai/api/v1/chat/completions"

models_to_test = [
    "google/gemini-2.5-flash-lite",
    "openai/gpt-4o-mini",
    "deepseek/deepseek-chat",
    "deepseek/deepseek-r1"
]

print("Testing Paid OpenRouter Models...")
for m in models_to_test:
    payload = {
        "model": m,
        "messages": [{"role": "user", "content": "Respond ONLY with 'OK'."}]
    }
    try:
        r = requests.post(url, headers=headers, json=payload, timeout=15)
        res = r.json()
        if "choices" in res and len(res["choices"]) > 0:
            print(f"✅ Model '{m}': SUCCESS -> {res['choices'][0]['message']['content'].strip()}")
        else:
            print(f"⚠️ Model '{m}': Response -> {res}")
    except Exception as e:
        print(f"❌ Model '{m}': Error -> {e}")
