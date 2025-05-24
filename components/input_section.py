import streamlit as st
from streamlit_tags import st_tags

CRITERIA_OPTIONS = [
    "Financial Health", "Growth Potential", "Work Culture",
    "Innovation", "ESG", "Leadership", "Stability"
]

def render_input_section():
    col1, col2, col3 = st.columns(3)

    with col1:
        company_tags = st_tags(
            label="Company Name",
            text="Add company...",
            value=[],
            suggestions=[],
            key="company_tags",
            maxtags=1
        )

    with col2:
        job_tags = st_tags(
            label="Job Title",
            text="Add job title...",
            value=[],
            suggestions=[],
            key="job_tags",
            maxtags=1
        )

    with col3:
        st.markdown('<div class="dropdown-align">', unsafe_allow_html=True)
        selected_criteria = st.multiselect(
            "Select Criteria",
            options=CRITERIA_OPTIONS,
            key="criteria_tags"
        )
        st.markdown('</div>', unsafe_allow_html=True)

    return company_tags, job_tags, selected_criteria
