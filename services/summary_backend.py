import time

placeholder_summary = """
### About the company
Intel Corporation is a leading American multinational technology company...

- **Company Name**: Intel Corporation  
- **Founded**: 1968  
- **Headquarters**: Santa Clara, California  
- **CEO**: Lip-Bu Tan  
- **Industry**: Semiconductors  
- **Website**: [intel.com](https://www.intel.com)
"""

placeholder_links = [
    'https://wcsecure.weblink.com.au/clients/seek/headline.aspx?headlineid=3661806',
    'https://www.listcorp.com/asx/sek/seek-limited/news/fy2025-half-year-results-announcement-3152527.html',
    'https://aimgroup.com/2025/02/17/seek-h1-fy2025-results-low-job-ad-volumes-drag-down-revenue-earnings/',
    'https://wcsecure.weblink.com.au/clients/seek/headline.aspx?headlineid=3661805',
    'https://www.staffingindustry.com/news/global-daily-news/seek-h1-revenue-slips-4-amid-lower-job-ad-volumes'
]

def fetch_summary_and_news(company_tags, job_tags):
    time.sleep(2)  # Simulate backend delay
    sample_summary = f"{company_tags} {job_tags} \n {placeholder_summary}"
    return sample_summary, placeholder_links
