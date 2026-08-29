import os
import requests
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("OPENROUTER_API_KEY")

headers = {
    "Authorization": f"Bearer {api_key}"
}

try:
    res = requests.get("https://openrouter.ai/api/v1/models", headers=headers, timeout=10)
    data = res.json().get("data", [])
    ds_models = [m["id"] for m in data if "deepseek" in m["id"].lower()]
    print("Found DeepSeek models on OpenRouter:")
    for d in ds_models:
        print(" -", d)
except Exception as e:
    print("Error fetching models:", e)
