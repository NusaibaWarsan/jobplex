import streamlit as st
import markdown

def render_summary(summary_text: str):
    summary_html = markdown.markdown(summary_text)

    st.markdown(
        f"""
        <div class="summary-box">
            {summary_html}
        </div>
        """,
        unsafe_allow_html=True
    )

def render_latest_news(news_urls: list[str]):
    # links_html = "".join([
    #     f'<li><a href="{url}" target="_blank" rel="noopener noreferrer">{url}</a></li>'
    #     for url in news_urls
    # ])

    news_html = markdown.markdown(news_urls)

    st.markdown(
        f"""
        <div class="latest-news-box">
            <ul>
                {news_html}
            </ul>
        </div>
        """,
        unsafe_allow_html=True
    )

def render_join_company_sentiment(company_sentiment: str):
    ssentiment_html = markdown.markdown(company_sentiment)

    st.markdown(
        f"""
        <div class="sentiment-box">
            {ssentiment_html}
        </div>
        """,
        unsafe_allow_html=True
    )
