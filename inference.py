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

summary_prompt="Fill in the bullet points regarding the company 'Intel Corporation':\n\n-Summary: \n- Company Name: \n- Founded: \n- Headquarters: \n- CEO: \n- Industry: \n\n If the information to the bullet points is not available, respond with 'N/A' for that bullet point."
summary_response = model_inference(summary_prompt)
print("Summary Response:\n", summary_response['answer'])

finance_prompt = "What are the financial details of Intel Corporation? Give your response in 3 bullet points. Ensure that the response is short and in easy layman terms"
finance_response = model_inference(finance_prompt)
print("Finance Response:\n", finance_response['answer'])

layoff_prompt = "Are there any news of layoffs recently in Intel Corporation? Keep your response in maximum of 2 sentences."
layoff_response = model_inference(layoff_prompt)
print("Layoff Response:\n", layoff_response['answer'])

organization_change_prompt = "Are there any recent organization changes or any scandals in Intel Corporation? Keep your response in maximum of 2 sentences."
organization_change_response = model_inference(organization_change_prompt)
print("Organization Change Response:\n", organization_change_response['answer'])

bonus_prompt = "What are the recent rewards or bonus given to employees in Intel Corporation? Keep your response in 3 bullet points."
bonus_response = model_inference(bonus_prompt)
print("Bonus Response:\n", bonus_response['answer'])

# TODO: if its a good time to join the company and latest news
