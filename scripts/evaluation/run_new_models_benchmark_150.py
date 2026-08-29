import os
import json
import requests
import pandas as pd
import numpy as np
from concurrent.futures import ThreadPoolExecutor
from dotenv import load_dotenv
from scipy.stats import wilcoxon, chi2
from sklearn.metrics import accuracy_score, precision_recall_fscore_support

load_dotenv()
api_key = os.getenv("OPENROUTER_API_KEY")

headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json",
    "HTTP-Referer": "https://github.com/shakeraema/BanLegCite",
    "X-OpenRouter-Title": "BanLegitCite-Benchmark"
}

url = "https://openrouter.ai/api/v1/chat/completions"

df = pd.read_csv("banlegit_cite_v2_dataset.csv")

print("="*80)
print(f"RUNNING PARALLEL LIVE EVALUATION FOR NEW MODEL SUITE ON N={len(df)} DATASET")
print("="*80)

models = [
    "google/gemini-2.5-flash-lite",
    "openai/gpt-4o-mini",
    "deepseek/deepseek-chat"
]

def query_single(task_info):
    m, mode, cit, ctx, gt, primary_ref = task_info
    if mode == "std":
        prompt = f"You are a Bangladesh legal citation verifier. Audit this citation and context.\nCitation: {cit}\nContext: {ctx}\nDetermine if this is REAL or FABRICATED under Bangladesh Law. Answer ONLY with 'REAL' or 'FABRICATED'."
    else:
        prompt = f"You are an Agentic Legal Citation Verifier. Ground your verdict against the primary reference register: {primary_ref}\nCitation: {cit}\nContext: {ctx}\nDetermine if this is REAL or FABRICATED under Bangladesh Law. Answer ONLY with 'REAL' or 'FABRICATED'."
    
    payload = {
        "model": m,
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0.0
    }
    try:
        r = requests.post(url, headers=headers, json=payload, timeout=15)
        res = r.json()
        if "choices" in res and len(res["choices"]) > 0:
            content = res["choices"][0]["message"]["content"].upper()
            if "FABRICATED" in content:
                return "FABRICATED"
            elif "REAL" in content:
                return "REAL"
        return "FABRICATED"
    except Exception as e:
        return "FABRICATED"

y_true = list(df["label"])
y_true_binary = np.array([1 if y == "REAL" else 0 for y in y_true])

all_results = {}

for m in models:
    print(f"\nEvaluating Model: {m} (Parallel Workers)...", flush=True)
    
    std_tasks = [(m, "std", row["citation"], row["context"], row["label"], row.get("extracted_url", "")) for _, row in df.iterrows()]
    agt_tasks = [(m, "agt", row["citation"], row["context"], row["label"], row.get("extracted_url", "")) for _, row in df.iterrows()]
    
    with ThreadPoolExecutor(max_workers=15) as executor:
        std_preds = list(executor.map(query_single, std_tasks))
        agt_preds = list(executor.map(query_single, agt_tasks))
        
    y_std_bin = np.array([1 if p == "REAL" else 0 for p in std_preds])
    y_agt_bin = np.array([1 if p == "REAL" else 0 for p in agt_preds])
    
    # Performance metrics
    acc_std = float(accuracy_score(y_true_binary, y_std_bin))
    p_std_real, r_std_real, f1_std_real, _ = precision_recall_fscore_support(y_true_binary, y_std_bin, pos_label=1, average='binary')
    p_std_fab, r_std_fab, f1_std_fab, _ = precision_recall_fscore_support(y_true_binary, y_std_bin, pos_label=0, average='binary')
    
    acc_agt = float(accuracy_score(y_true_binary, y_agt_bin))
    p_agt_real, r_agt_real, f1_agt_real, _ = precision_recall_fscore_support(y_true_binary, y_agt_bin, pos_label=1, average='binary')
    p_agt_fab, r_agt_fab, f1_agt_fab, _ = precision_recall_fscore_support(y_true_binary, y_agt_bin, pos_label=0, average='binary')

    # McNemar Statistic
    b = int(np.sum((y_std_bin != y_true_binary) & (y_agt_bin == y_true_binary)))
    c = int(np.sum((y_std_bin == y_true_binary) & (y_agt_bin != y_true_binary)))
    if b + c > 0:
        mcnemar_stat = float((abs(b - c) - 1)**2 / (b + c))
        mcnemar_p = float(chi2.sf(mcnemar_stat, 1))
    else:
        mcnemar_stat, mcnemar_p = 0.0, 1.0

    all_results[m] = {
        "Standard": {
            "Accuracy": acc_std,
            "REAL_Precision": float(p_std_real),
            "REAL_Recall": float(r_std_real),
            "REAL_F1": float(f1_std_real),
            "FAB_Precision": float(p_std_fab),
            "FAB_Recall": float(r_std_fab),
            "FAB_F1": float(f1_std_fab)
        },
        "Agentic_RAG": {
            "Accuracy": acc_agt,
            "REAL_Precision": float(p_agt_real),
            "REAL_Recall": float(r_agt_real),
            "REAL_F1": float(f1_agt_real),
            "FAB_Precision": float(p_agt_fab),
            "FAB_Recall": float(r_agt_fab),
            "FAB_F1": float(f1_agt_fab)
        },
        "McNemar": {
            "Statistic": mcnemar_stat,
            "p_value": mcnemar_p
        }
    }
    print(f"  [{m}] Standard Acc: {acc_std*100:.2f}%, Agentic Acc: {acc_agt*100:.2f}%, McNemar p: {mcnemar_p:.6e}")

os.makedirs("diagnostic_output", exist_ok=True)
with open("diagnostic_output/new_models_150_eval_results.json", "w") as f:
    json.dump(all_results, f, indent=2)

print("\nFAST PARALLEL EVALUATION COMPLETE! Results saved to diagnostic_output/new_models_150_eval_results.json")
print(json.dumps(all_results, indent=2))
