import streamlit as st
import pandas as pd
import altair as alt
import markdown 

def _get_sentiment_data():
    data = pd.DataFrame({
        'Month': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'],
        'Positive': [60, 65, 70, 68, 75, 80],
        'Neutral': [25, 20, 15, 18, 12, 10],
        'Negative': [15, 15, 15, 14, 13, 10],
    })
    data_long = data.melt(id_vars='Month', var_name='Sentiment', value_name='Percentage')
    return data_long

def render_sentiment_analysis():
    col1, col2 = st.columns(2)

    with col1:
        sentiment_text = """
        **Sentiment Analysis Report:**  

        Over the past 6 months, public sentiment around Intel Corporation has been generally positive, 
        with a spike in positive mentions around their Q2 earnings report. Minor negative dips were observed 
        due to workforce restructuring announcements, but these were temporary.
        """

        sentiment_html = markdown.markdown(sentiment_text.strip())

        st.markdown(
            f"""
            <div class="sentiment-box">
                {sentiment_html}
            </div>
            """,
            unsafe_allow_html=True
        )

    with col2:
        data_long = _get_sentiment_data()

        chart = alt.Chart(data_long).mark_line(point=True).encode(
            x='Month',
            y='Percentage',
            color='Sentiment'
        ).properties(
            title='Sentiment Trend Over Time',
            height=300
        )

        st.altair_chart(chart, use_container_width=True)

def render_sentiment_chart():
    data_long = _get_sentiment_data()

    chart = alt.Chart(data_long).mark_line(point=True).encode(
        x='Month',
        y='Percentage',
        color='Sentiment'
    ).properties(
        title='Sentiment Trend Over Time',
        height=400  # taller chart for full width
    )

    st.altair_chart(chart, use_container_width=True)
