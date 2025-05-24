import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("PERPLEXITY_API_KEY")
API_URL = "https://api.perplexity.ai/chat/completions"

def model_inference(user_prompt):
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    data = {
        "model": "sonar-pro",
        "messages": [
            {"role": "system", "content": "You are a helpful assistant that helps job seekers research on their selected companies."},
            {"role": "user", "content": user_prompt},
        ]
    }

    response = requests.post(API_URL, headers=headers, json=data)

    if response.ok:
        result = response.json()
        answer = result['choices'][0]['message']['content']
        citations = result.get('citations', [])

        return {
            "answer": answer,
            "citations": citations
        }
    else:
        raise Exception(f"API request failed: {response.status_code} - {response.text}")