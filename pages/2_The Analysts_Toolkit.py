import streamlit as st
from utils import css_load

st.set_page_config(
    page_title="Data Analyst Job Market Analysis",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded")

css_load()

# Title
st.title("Chapter 2: The Analyst's Toolkit - From Foundational Skills to Senior Expertise")


# Sidebar

with st.sidebar:
    st.image(r'streamlit-logo-primary-colormark-darktext.png', use_container_width=False)
    st.write("""### Project by: **Adam Astiti**""")
    st.link_button('Linkedin', 'https://www.linkedin.com/in/adam-astiti-a3787312a/', icon='💼')
    st.link_button('Github', 'https://github.com/adam-astiti', icon='👨‍💻')

# Naration
st.markdown("""
    After establishing the broad landscape of the data analyst job market, 
    the next crucial step is to understand the specific tools required for the job. 
    What skills form the foundation of an analyst's toolkit, and how does that toolkit evolve as one advances to a senior level?
    """)

# Chart
col1, col2 = st.columns(2)

with col1:
    st.image('Data Analysis\Result\Chapter 2 Question 1.png')

with col2:
    st.image('Data Analysis\Result\Chapter 2 Question 2.png')

# Chart Explanation
with st.expander("Finding 1: (Click Here)"):
        st.header("Finding 1: The Unshakeable Foundation: SQL is King")
        st.markdown("""
For anyone looking to enter the Data Analyst field, the data sends an unambiguous message: **SQL** is the **most critical skill** for a data analyst. With over 90,000 job postings mentioning it, SQL is not just a desirable skill—it's the bedrock upon which the entire profession is built.

Following SQL, the core toolkit is rounded out by **Excel** and **Python**, both essential for data manipulation and analysis. Finally, proficiency in a major **Business Intelligence tool** is a must, with **Tableau** and **Power BI** clearly established as the two industry standards. This chart effectively defines the five "must-have" skills for any aspiring data analyst.
        """)

with st.expander("Finding 2: (Click Here)"):
        st.header("Finding 2: The Path to Seniority: Python's Rise and Specialization")
        st.markdown("""
But what happens when an analyst is ready to take the next step in their career? By filtering for "Senior Data Analyst" roles, we see a fascinating evolution in skill demand.

While **SQL remains the undisputed champion**, the hierarchy of the other skills shifts significantly. **Python** moves up to become the clear **number two skill**, surpassing Excel. This indicates that for senior-level roles, the ability to perform more **complex analysis**, **automation**, and potentially **light machine learning with Python** becomes more valuable than spreadsheet manipulation.

Furthermore, we see **R** emerge as a top 5 skill, replacing Power BI from the general list. This suggests that **senior roles** may require more specialized **statistical programming** for deeper, more complex analytical tasks.
        """)


# Finding Summary
st.markdown("# Findings Summary")

st.markdown("""
Comparing these two views gives us a clear career roadmap:

1. **To get the job**: Master the foundational five **SQL, Excel, Python, Tableau, and Power BI**.

2. **To get the promotion**: Deepen your expertise in **Python** and consider adding a specialized statistical language like **R** to your arsenal.

The journey from a junior to a senior analyst is not just about gaining experience; it's about evolving your technical capabilities to handle more complex and programmatically-driven challenges.

With this understanding of the required skills, **Chapter 3** will explore the most important question: how do these skills translate into salary and financial opportunity?
            """)

