import streamlit as st

def render_header():
    col1, col2, col3 = st.columns([1, 1, 1])

    with col2:
        st.image("assets/logo.png", use_container_width=True)  # You can adjust width as needed

    with col3:
        st.markdown(
            """
            <div class="myapp-nav-buttons" style="display: flex; justify-content: flex-end;">
                <a href="/?page=about">About</a>
                <a href="/?page=feedback">Send Feedback</a>
            </div>
            """,
            unsafe_allow_html=True
        )
