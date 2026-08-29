import os
import requests
import json
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("OPENROUTER_API_KEY")

prompt = """Act as a Senior Bangladeshi Legal Researcher. Analyze these 3 legal citation tasks:

1. TASK_149: Citation: "16 BLC (HCD) 712", Case: "Bangladesh National Women Lawyers Association (BNWLA) v. Bangladesh", Context: "2009 sexual harassment guidelines apply retroactively to private contractual disputes under Employment of Labour Act."
2. TASK_074: Citation: "18 BLC (HCD) 538", Case: "BLAST v. Bangladesh", Context: "Private textile factory owners bear no statutory liability for structural failures if they obtained preliminary safety certificate."
3. TASK_050: Citation: "5 ALR (AD) 245", Case: "State v. Kamrul Islam", Context: "Appellate Division mitigated death sentence to life imprisonment, holding public lynching cases of minor citizens do not qualify for fast-track processing."

For each task:
a) Is it REAL or FABRICATED? Explain the exact mutation (e.g. true DLR/BLC citation volume vs mutated volume, or misattributed legal holding).
b) Provide the REAL landmark case citation and accessible primary source verification links (e.g., blast.org.bd, belabangladesh.org, bdlaws.minlaw.gov.bd, supremecourt.gov.bd, or Columbia Freedom of Expression / Lawyersnjurists).
"""

url = "https://openrouter.ai/api/v1/chat/completions"
headers = {
    "Authorization": f"Bearer {api_key.strip()}",
    "Content-Type": "application/json",
    "HTTP-Referer": "https://github.com/shakeraema/BanLegCite",
    "X-Title": "BanLegit-Cite Verification"
}

payload = {
    "model": "z-ai/glm-5.2:free",
    "messages": [{"role": "user", "content": prompt}]
}

response = requests.post(url, headers=headers, json=payload)
res_json = response.json()

if "choices" in res_json:
    print(res_json["choices"][0]["message"]["content"])
else:
    print("Error:", res_json)
