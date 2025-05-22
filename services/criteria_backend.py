def fetch_criteria_data(selected_criteria):
    """
    Dummy fetch function for criteria insights based on selected criteria.
    Returns a list of dicts with Criterion and Insight.
    """
    DUMMY_CRITERIA_DATA = {
        "Turnover Rate": "Moderate turnover (~12%) in last 12 months",
        "Diversity and Inclusion": "Strong DEI policy with measurable outcomes",
        "Leadership Style": "Collaborative leadership with open-door policy",
        "Work-Life Balance": "Flexible hours with strong remote support",
        "Employee Satisfaction": "Rated 4.2/5 on average by employees",
        "Career Growth Opportunities": "Defined promotion tracks and mentorship"
    }

    results = []
    for criterion in selected_criteria:
        insight = DUMMY_CRITERIA_DATA.get(
            criterion,
            "No data available yet. Please research this manually."
        )
        results.append({"Criterion": criterion, "Insight": insight})

    return results
