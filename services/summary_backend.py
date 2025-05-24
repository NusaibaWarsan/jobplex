import time
from .model import model_inference

# placeholder_summary = """
# ## Summary

# - **Summary:** Intel Corporation is a global leader in semiconductor manufacturing and technology innovation, with a significant presence in research, development, and design for the electronics and computing industries[5].
# - **CEO:** Lip-Bu Tan[2]
# - **Industry:** Semiconductors / Technology[5]

# ## Finance

# - Intel reported $12.7 billion in revenue for Q1 2025, which remained flat compared to the same period last year, with a loss of $0.19 per share on a standard basis but a profit of $0.13 per share on an adjusted basis[1][4].
# - The company is forecasting lower revenue for Q2 2025, between $11.2 billion and $12.4 billion, and expects to break even on an adjusted earnings basis, which disappointed market analysts and caused the stock to drop over 5% in after-hours trading[1][5].
# - Intel's foundry division, which makes chips for other companies, performed well with revenue of $4.7 billion, exceeding expectations, though the company noted some revenue might have been inflated by customers buying ahead of potential tariffs[5].

# ## Layoffs

# - Intel Corporation is currently implementing significant workforce reductions, with plans to lay off approximately 20% of its global workforce (around 21,000–22,000 employees) as reported in April 2025, as part of a restructuring effort led by new CEO Lip-Bu Tan to streamline management and refocus on engineering[1][3][4].
# - These cuts follow previous layoffs, including 15,000 positions eliminated in August 2024, and are expected to be officially announced alongside Intel's Q1 2025 earnings call[1][5].

# ## Organizational Changes

# - Intel Corporation has undergone significant leadership changes, with Lip-Bu Tan appointed as CEO in March 2025 after Pat Gelsinger's resignation, and the company recently announced plans for additional workforce reductions following earlier layoffs that affected at least 1,117 employees in Folsom since January 2023[2][3][5].
# - Tan has emphasized making Intel an engineering-focused company while removing organizational complexity, with plans to complete most of the previously announced 15% workforce reduction (approximately 15,000 roles) by the end of 2024 as part of a $10 billion cost-saving initiative[1][3][4].

# ## Bonuses

# - Intel has reduced annual bonuses for employees in Israel to 0.8 months' salary for 2024, down significantly from the previous 2.5–3 months' salary bonuses, though the company did provide a separate $5,000 grant to Israeli employees following the onset of war[1].
# - Intel Corporation pays an average annual employee bonus of $7,742 in the US, with bonus amounts ranging from $2,998 to $19,774 depending on position[2].
# - For executive positions, Intel offers substantial performance-based compensation, with one recent executive offer including an Annual Performance Bonus (APB) with a target payout of 200% of base salary (equivalent to $2,000,000 for fiscal year 2025)[4].
# """

# placeholder_links = [
#     'https://wcsecure.weblink.com.au/clients/seek/headline.aspx?headlineid=3661806',
#     'https://www.listcorp.com/asx/sek/seek-limited/news/fy2025-half-year-results-announcement-3152527.html',
#     'https://aimgroup.com/2025/02/17/seek-h1-fy2025-results-low-job-ad-volumes-drag-down-revenue-earnings/',
#     'https://wcsecure.weblink.com.au/clients/seek/headline.aspx?headlineid=3661805',
#     'https://www.staffingindustry.com/news/global-daily-news/seek-h1-revenue-slips-4-amid-lower-job-ad-volumes'
# ]

# def fetch_summary_and_news(company_tags, job_tags):
#     time.sleep(2)  # Simulate backend delay
#     sample_summary = f"{company_tags} {job_tags} \n {placeholder_summary}"
#     return sample_summary, placeholder_links

def _get_summary(company_tag):
    summary_user_prompt = f"""
    Fill in the bullet points regarding the company '{company_tag}':
    - Summary:
    - CEO:
    - Industry:

    For the summary, ensure your response is short and simple with a maximum of 2 sentences. Just provide the bullet points in your response without additional text. Use the latest news and information available.
    """
    response = model_inference(summary_user_prompt)
    return response['answer']

def _get_financials(company_tag):
    finance_user_prompt = f"""
    What are the financial details of {company_tag}? Give your response in 2 bullet points. Ensure that the response is simplified and in easy to understand in layman terms.
    """
    response = model_inference(finance_user_prompt)
    return response['answer']

def _get_layoffs(company_tag):
    layoff_user_prompt = f"""
    Are there any news of layoffs recently in {company_tag}? Keep your response in maximum of 2 sentences.
    """
    response = model_inference(layoff_user_prompt)
    return response['answer']

def _get_organization_changes(company_tag):
    organization_change_user_prompt = f"""
    Are there any recent organization changes or any scandals in {company_tag}? Keep your response short and in maximum of 2 sentences.
    """
    response = model_inference(organization_change_user_prompt)
    return response['answer']

def _get_bonus(company_tag):
    bonus_user_prompt = f"""
    What are the recent rewards or bonus given to employees in {company_tag}? Keep your response simplified in 2 bullet points.
    """
    response = model_inference(bonus_user_prompt)
    return response['answer']

def get_summary_section(company_tag):
    summary = _get_summary(company_tag)
    financials = _get_financials(company_tag)
    layoffs = _get_layoffs(company_tag)
    organization_changes = _get_organization_changes(company_tag)
    bonus = _get_bonus(company_tag)

    format_summary_prompt = f"""
    Format below responses into a neat markdown format:
    Summary: {summary}
    Finance: {financials}
    Layoffs: {layoffs}
    Organization Changes: {organization_changes}
    Bonus: {bonus}

    I just want the formatted markdown response without any additional text or explanation. Do not format it into a table. Just add relevant markdown headings and bullet points to make it look neat and readable.
    """
    response = model_inference(format_summary_prompt)
    return response['answer']

def get_news(company_tag):
    news_user_prompt = f"""
    Search and display the top 3 latest news articles about {company_tag}. Provide the title and a short summary in one sentence of each article. Ensure your response is in the format below:
    1. [Title of the article](URL to article)
    - Summary of the article

    Do not include citations in you response.
    """
    response = model_inference(news_user_prompt)
    return response['answer']

def get_join_company_sentiment(company_tag, job_tag):
    join_company_user_prompt = f"""
    Is it a good time to join {company_tag} as a {job_tag}? Provide your response in 2 short and concise sentences.
    """
    response = model_inference(join_company_user_prompt)
    return response['answer']