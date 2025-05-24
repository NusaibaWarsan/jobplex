from .model import model_inference
import re
from urllib.parse import urlparse

def format_answer(answer: str, citations: list[str]) -> str:
    matches = re.findall(r'\[(\d+)\]', answer)
    used_indices = sorted(set(int(m) - 1 for m in matches if m.isdigit()))

    citation_map = {}
    for i in used_indices:
        if i < len(citations):
            url = citations[i]
            citation_map[f'[{i+1}]'] = f'<sup><a href="{url}" target="_blank">[{i+1}]</a></sup>'
    def replace_tag(match):
        tag = match.group()
        return citation_map.get(tag, tag) 

    html_answer = re.sub(r'\[\d+\]', replace_tag, answer)
    return html_answer.strip()

def criteria_response(criteria, job_title, company):
    prompt = f"""
    Your task is to conduct research on {criteria} specifically for {job_title} at {company}.
    Follow these steps:
    Step 1: Conduct a search to gather insights into {criteria} for {job_title} at {company}, focusing on surveys, reviews, or reports.
    Step 2: Identify ratings or metrics that assess {criteria} for {job_title}. If {criteria} are unavailable, provide the overall {criteria} at {company}.
    Step 3: Summarize your findings in exactly 30 words, ensuring to include any ratings or metrics found. 
    Step 4: Use HTML tags to bold important metrics or information (e.g., <b>important information</b>). Do not use any type of first-person narration, and do not state unavailability if information is missing.
    """
    response = model_inference(prompt)
    return response['answer'], response['citations']

def fetch_criteria_data(selected_criteria, job_title, company):
    results = []
    if job_title is None or company is None or not selected_criteria:
        results.append({"Criterion": criterion, "Insight": "No data available"})
        return results
    for criterion in selected_criteria:
        answer, citations = criteria_response(criterion, job_title, company)
        final_answer = format_answer(answer, citations)
        final_answer = final_answer.replace('\n', '')
        results.append({"Criterion": criterion, "Insight": final_answer})

    return results
