import streamlit as st
import pandas as pd
import altair as alt

@st.cache_data
def load_reviews_data(company_tag):
    if company_tag == "duolingo":
        reviews = "glassdoor_reviews_db/duolingo_reviews.csv"
    elif company_tag == "meta":
        reviews = "glassdoor_reviews_db/meta_reviews.csv"
    elif company_tag == "perplexity":
        reviews = "glassdoor_reviews_db/perplexity_reviews.csv"
    elif company_tag == "intel":
        reviews = "glassdoor_reviews_db/intel_reviews.csv"
    df = pd.read_csv(reviews)
    df["Date"] = pd.to_datetime(df["Date"])
    df["Month"] = df["Date"].dt.to_period("M").astype(str)
    return df

def render_sentiment_chart(company_tag):
    df = load_reviews_data(company_tag[0].lower())

    grouped = df.groupby("Month").agg({
        "Ratings": "mean",
        "Title": "count"
    }).reset_index().rename(columns={"Ratings": "Average Rating", "Title": "Review Count"})

    st.subheader("Average Employee Rating Over Time (Meta)")

    chart = alt.Chart(grouped).mark_line(point=True).encode(
        x=alt.X("Month:T", title="Month"),
        y=alt.Y("Average Rating:Q", title="Average Rating", scale=alt.Scale(domain=[0, 5])),
        tooltip=[
            alt.Tooltip("Month:T", title="Month"),
            alt.Tooltip("Average Rating:Q", title="Avg Rating", format=".2f"),
            alt.Tooltip("Review Count:Q", title="Review Count")
        ]
    ).properties(height=400, width='container')

    st.altair_chart(chart, use_container_width=True)
