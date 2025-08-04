import streamlit as st
from utils import css_load

st.set_page_config(
    page_title="Data Analyst Job Market Analysis",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded")

css_load()



# Title
st.title("A Data Analyst Job Market 2023")

st.page('Streamlit_app\Pages\1_The_Job_Market_Landscape.py', title='The_Job_Market_Landscape')

# Sidebar

with st.sidebar:
    st.image(r'Streamlit_app/streamlit-logo-primary-colormark-darktext.png', use_container_width=False)
    st.write("""### Project by: **Adam Astiti**""")
    st.link_button('Linkedin', 'https://www.linkedin.com/in/adam-astiti-a3787312a/', icon='💼')
    st.link_button('Github', 'https://github.com/adam-astiti', icon='👨‍💻')
    

# Naration
st.markdown("""
    Welcome to my analysis of the data analyst job market! This project uses a dataset of over 700,000 job postings
    to uncover the key trends shaping the industry.

    **My goal is to answer critical questions for aspiring analysts:**
    - What skills are most in-demand?
    - Which locations offer the best salaries?
    - How has the rise of remote work impacted the job landscape?

    Use the navigation in the sidebar to explore the different chapters of this analysis.
    This project was built using Python, SQL, and Streamlit, with the data processed in a custom-built data warehouse.
    """)



