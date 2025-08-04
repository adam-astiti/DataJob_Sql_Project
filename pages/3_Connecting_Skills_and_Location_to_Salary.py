import streamlit as st
from utils import css_load

st.set_page_config(
    page_title="Data Analyst Job Market Analysis",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded")

css_load()

# Title
st.title("Chapter 3: The Payoff - Connecting Skills and Location to Salary")

# Sidebar

with st.sidebar:
    st.image(r'streamlit-logo-primary-colormark-darktext.png', use_container_width=False)
    st.write("""### Project by: **Adam Astiti**""")
    st.link_button('Linkedin', 'https://www.linkedin.com/in/adam-astiti-a3787312a/', icon='💼')
    st.link_button('Github', 'https://github.com/adam-astiti', icon='👨‍💻')

# Naration
st.markdown("""
    In Chapter 2, we built a clear roadmap of the technical skills required to land a data analyst role and advance to a senior position. 
    Now, we address the pivotal question for any professional: What is the financial return on these skills? 
    This chapter explores the economic landscape, revealing which skills command the highest salaries and which countries offer the most lucrative compensation.
    """)

# Chart
col1, col2 = st.columns(2)

with col1:
    st.image('Data Analysis/Result/Chapter 3 Question 1.png')

with col2:
    st.image('Data Analysis/Result/Chapter 3 Question 2.png')

# Chart Explanation
with st.expander("Finding 1: (Click Here)"):
        st.header("Finding 1: Specialization Drives Higher Salaries")
        st.markdown("""
While Chapter 2 identified the most demanded skills, this analysis uncovers the highest-paying skills. 
The results are telling: **specialization** is the key to maximizing earning potential.

While **foundational skills** like Python and Tableau still make the list, proving their high value, the **top-paying skills** are often more **specialized**. 
Technologies related to **big data ecosystems** **(Hadoop, Spark)**, **cloud platforms (AWS)**, and **advanced business intelligence** or **project management tools (Looker, Jira)** are all associated with average salaries exceeding $84,000.

**The story here is clear:** Mastering the basics like SQL and Python gets you in the door. Mastering **specialized**, high-demand tools is what gets you the top-tier salary.
        """)

with st.expander("Finding 2: (Click Here)"):
        st.header("Finding 2: High Salaries are a Global Phenomenon")
        st.markdown("""
After skills, geography is the next major factor influencing salary. While Chapter 1 showed that the United States has the highest volume of jobs, this chart reveals that **high salaries are not exclusive to any single region**.

Interestingly, countries in Latin America like **Costa Rica** and **Chile** lead this particular list, with average salaries pushing past $100,000. This is followed closely by major economic players in Europe and Asia, such as **Germany, India, and Singapore**.

This finding demonstrates that the demand for skilled data professionals has created competitive salary environments across the globe. An analyst's earning potential is not limited by their proximity to the largest job market but can be realized in various international tech hubs.
        """)


# Finding Summary
st.markdown("# Findings Summary")

st.markdown("""
The path to a high salary in data analytics is a combination of what you know and where you work. The data suggests a two-pronged strategy for success:

1. **Build a T-shaped skillset:** Develop a deep expertise in foundational skills (the vertical bar of the "T") and complement it with a broad understanding of high-value, specialized tools (the horizontal bar).

2. **Think Globally:** Be aware that lucrative opportunities exist worldwide, sometimes in unexpected places.

We've now established the skills that are valued and the locations where they are valued most. But a new factor has changed this equation entirely: remote work. **Chapter 4** will investigate how the rise of remote opportunities impacts salary and the importance of physical location.
            """)

