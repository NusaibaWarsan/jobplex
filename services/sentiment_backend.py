def fetch_sentiment_data(company_tags: list[str], job_tags: list[str]) -> dict:

    # Dummy sentiment data example
    sentiment_summary = {
        "overall_sentiment": "Positive",
        "score": 0.78,
        "positive_mentions": 120,
        "negative_mentions": 30,
        "neutral_mentions": 50
    }
    return sentiment_summary
