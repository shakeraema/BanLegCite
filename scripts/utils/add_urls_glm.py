import os
import re
from dotenv import load_dotenv
from openai import OpenAI
import time

load_dotenv()
api_key = os.getenv("OPENROUTER_API_KEY")

if not api_key:
    print("Error: OPENROUTER_API_KEY not found")
    exit(1)

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=api_key,
)

file_path = "statutory_anchors.md"
with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# Split the content by "Task S"
tasks = re.split(r'(\*\*Task S\d+\*\*)', content)

new_content = tasks[0]

for i in range(1, len(tasks), 2):
    task_header = tasks[i]
    task_body = tasks[i+1]
    
    # If the task already has a link at the bottom (like S1, S2, S3), skip calling API
    if "http" in task_body:
        new_content += task_header + task_body
        continue
        
    print(f"Processing {task_header}...")
    
    # Extract the citation
    citation_match = re.search(r'\*\*Citation:\*\* (.*)', task_body)
    citation = citation_match.group(1) if citation_match else "Bangladesh Law"
    
    prompt = f"""
    You are a Bangladesh legal expert. I need a single URL to a real, verifiable webpage that discusses or contains information about: "{citation}".
    Please provide a URL from a reliable source like lawyersnjurists.com, bdlaws.minlaw.gov.bd, clcbd.org, or blast.org.bd.
    Return ONLY the URL, nothing else. If you don't know an exact URL, provide the official bdlaws.minlaw.gov.bd URL for that section.
    """
    
    max_retries = 5
    for attempt in range(max_retries):
        try:
            response = client.chat.completions.create(
                model="z-ai/glm-5.2:free",
                messages=[{"role": "user", "content": prompt}],
                extra_headers={
                    "HTTP-Referer": "https://github.com/ZahidHasan7/BanLegit-Cite",
                    "X-Title": "BanLegit-Cite Research"
                }
            )
            url = response.choices[0].message.content.strip()
            break
        except Exception as e:
            print(f"API Error: {e}. Retrying in 5 seconds...")
            time.sleep(5)
            if attempt == max_retries - 1:
                url = "https://bdlaws.minlaw.gov.bd/" # fallback

    
    # Append the URL to the task body
    task_body = task_body.rstrip() + f"\n{url}\n\n"
    new_content += task_header + task_body
    
    time.sleep(1) # Small delay to avoid rate limits

with open(file_path, "w", encoding="utf-8") as f:
    f.write(new_content)

print("Done updating statutory_anchors.md with URLs!")
