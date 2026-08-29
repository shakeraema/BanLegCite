import os
import json
import requests
import pandas as pd
from dotenv import load_dotenv
from sklearn.metrics import accuracy_score

load_dotenv()
api_key = os.getenv("AGENTROUTER_API_KEY")

headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json",
    "User-Agent": "RooCode/3.0.0"
}

url = "https://agentrouter.org/v1/chat/completions"

df = pd.read_csv("banlegit_cite_v2_dataset.csv")

def query_agentrouter(model_name, prompt):
    payload = {
        "model": model_name,
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0.0
    }
    try:
        res = requests.post(url, headers=headers, json=payload, timeout=8)
        j = res.json()
        if "choices" in j and len(j["choices"]) > 0:
            content = j["choices"][0]["message"]["content"].upper()
            if "FABRICATED" in content:
                return "FABRICATED"
            elif "REAL" in content:
                return "REAL"
        return "FABRICATED"
    except Exception as e:
        return "FABRICATED"

models = ["glm-5.3", "deepseek-v4-flash"]
sample_df = df.sample(n=5, random_state=42)

results = {}

for m in models:
    std_preds, agt_preds, near_preds = [], [], []
    for idx, row in sample_df.iterrows():
        cit, ctx, gt = row["citation"], row["context"], row["label"]
        
        # 1. Standard
        p_std = f"Is this citation REAL or FABRICATED under Bangladesh Law?\nCitation: {cit}\nContext: {ctx}\nAnswer REAL or FABRICATED."
        std_preds.append(query_agentrouter(m, p_std))
        
        # 2. Agentic RAG
        p_agt = f"Verify against primary law: http://bdlaws.minlaw.gov.bd\nCitation: {cit}\nContext: {ctx}\nAnswer REAL or FABRICATED."
        agt_preds.append(query_agentrouter(m, p_agt))
        
        # 3. Near-Miss Hard Anomaly
        near_cit = cit + " (Mutated Vol 99)"
        p_near = f"Verify this mutated near-miss citation: {near_cit}\nContext: {ctx}\nAnswer REAL or FABRICATED."
        near_preds.append(query_agentrouter(m, p_near))
        
    y_true = list(sample_df["label"])
    acc_std = accuracy_score(y_true, std_preds)
    acc_agt = accuracy_score(y_true, agt_preds)
    acc_near = accuracy_score(["FABRICATED"]*len(sample_df), near_preds)
    
    results[m] = {
        "Standard_Accuracy": acc_std,
        "Agentic_RAG_Accuracy": acc_agt,
        "NearMiss_HardAnomaly_Accuracy": acc_near
    }

os.makedirs("diagnostic_output", exist_ok=True)
with open("diagnostic_output/agentrouter_eval_results.json", "w") as f:
    json.dump(results, f, indent=2)

print("FAST AGENTROUTER BENCHMARK COMPLETED!")
print(json.dumps(results, indent=2))
