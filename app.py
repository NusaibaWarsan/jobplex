import streamlit as st
from components.header import render_header
from components.input_section import render_input_section
from components.sentiment import render_sentiment_chart
from components.criteria import render_criteria_table
from components.summary import render_summary, render_latest_news
from services.summary_backend import fetch_summary_and_news
from services.criteria_backend import fetch_criteria_data
from services.sentiment_backend import fetch_sentiment_data

st.set_page_config(layout="wide")

with open("assets/style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Page routing
page = st.query_params.get("page", ["main"])[0]

# Initialize session state
if "summary_text" not in st.session_state:
    st.session_state.summary_text = ""
if "latest_news" not in st.session_state:
    st.session_state.latest_news = []

# Header + Inputs
render_header()

# Submit Button
top_right = st.columns([1, 17, 1])[2]

company_tags, job_tags, selected_criteria = render_input_section()

with top_right:
    if st.button("Submit", key="submit_button"):
        ## backend code goes into these functions
        st.session_state.summary_text, st.session_state.latest_news = fetch_summary_and_news(company_tags, job_tags)
        st.session_state.criteria_data = fetch_criteria_data(selected_criteria)
        st.session_state.sentiment_data = fetch_sentiment_data(company_tags, job_tags)

# Main Page Content
with st.container():
    if page == "main":
        if st.session_state.summary_text:
            left_col, right_col = st.columns(2)

            with left_col:
                render_summary(st.session_state.summary_text)
                render_latest_news(st.session_state.latest_news)
                st.markdown("###")

            with right_col:
                render_criteria_table(selected_criteria)

            render_sentiment_chart()

    elif page == "about":
        st.write("## About")
        st.write("This app analyzes public data to help you assess a company’s job offer or reputation.")

    elif page == "feedback":
        st.write("## Feedback")
        st.write("Let us know how we can improve!")

    else:
        st.error("Page not found.")
