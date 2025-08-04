import streamlit as st
from utils import css_load

st.set_page_config(
    page_title="Data Analyst Job Market Analysis",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded")

css_load()

# Title
st.title("Chapter 4: The Modern Workplace - Decoding the Remote Job Landscape")

# Sidebar

with st.sidebar:
    st.image(r'streamlit-logo-primary-colormark-darktext.png', use_container_width=False)
    st.write("""### Project by: **Adam Astiti**""")
    st.link_button('Linkedin', 'https://www.linkedin.com/in/adam-astiti-a3787312a/', icon='💼')
    st.link_button('Github', 'https://github.com/adam-astiti', icon='👨‍💻')

# Naration
st.markdown("""
    The previous chapters established a clear formula for success based on skills and location. 
    However, the modern workplace has introduced a powerful new variable: remote work. 
    This final chapter investigates the true impact of this trend. How common are remote roles? 
    Do they affect compensation? And do they require a different set of skills?
    """)

# Chart
col1, col2 = st.columns(2)

with col1:
    st.image('Data Analysis\Result\Chapter 4 Question 1.png')

with col2:
    st.image('Data Analysis\Result\Chapter 4 Question 2.png')

st.image('Data Analysis\Result\Chapter 4 Question 3.png')

# Chart Explanation
with st.expander("Finding 1: (Click Here)"):
        st.header("Finding 1: On-site Roles Still Dominate the Market")
        st.markdown("""
While discussions about remote work are widespread, the data provides a crucial reality check. 
**A staggering 93.2% of data analyst job postings are for on-site positions.**

This indicates that while remote work has certainly become more common, 
the traditional office-based role remains the standard in the industry. 
For job seekers, this means that while remote opportunities exist, limiting a search exclusively to remote roles will significantly narrow the pool of available positions.
        """)

with st.expander("Finding 2: (Click Here)"):
        st.header("Finding 2: Salary Parity - Remote Work Doesn't Mean a Pay Cut")
        st.markdown("""
Perhaps the most surprising insight is the relationship between work location and salary. 
A common assumption is that remote jobs might offer lower pay in exchange for flexibility. The data proves this to be a myth.

**The average salaries for remote and on-site positions are virtually identical.**
This is a powerful finding for job seekers, 
as it demonstrates that they can pursue the flexibility of remote work without having to compromise on their earning potential. 
Companies are valuing the skills of a data analyst equally, regardless of their physical location.
        """)

with st.expander("Finding 3: (Click Here)"):
        st.header("Finding 3: The Core Skills for Remote Work are Universal")
        st.markdown("""
Given the parity in pay, the next logical question is whether remote jobs require a different, more specialized skillset. 
The analysis shows this is not the case.

The most **in-demand skills** for remote jobs are the **same** foundational skills 
required for **on-site** roles: SQL, Excel, and Python form the core, followed closely by BI tools like Tableau and Power BI. 
This reinforces the central theme of our analysis: **these skills are universally critical** to the role of a data analyst, **independent of the work environment**.
        """)


# Finding Summary
st.markdown("# Findings Summary")

st.markdown("""
This chapter clarifies the role of remote work in the data analytics field. 
It is not the majority of the market, but it represents a significant and viable alternative for job seekers. 
Crucially, the decision to work remotely does not come with a financial penalty, 
and the path to succeeding in a remote role requires the very same fundamental skills as an on-site position.

We have now completed our journey through the data, from the high-level landscape to the specifics of skills, 
salary, and work environment. **The final step is to bring all these insights together into a conclusive, actionable summary.**
            """)

