import streamlit as st
import pandas as pd

def render_criteria_table(criteria_data):
    st.markdown('<div class="criteria-box">', unsafe_allow_html=True)

    if criteria_data:
        df = pd.DataFrame(criteria_data)
        st.dataframe(df, use_container_width=True)
    else:
        st.write("No criteria selected or no data available.")

    st.markdown('</div>', unsafe_allow_html=True)
