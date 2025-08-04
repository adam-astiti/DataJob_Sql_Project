import streamlit as st
from utils import css_load

st.set_page_config(
    page_title="Data Analyst Job Market Analysis",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded")

css_load()

# SIDEBAR

with st.sidebar:
    st.image('Streamlit_app\streamlit-logo-primary-colormark-darktext.png', use_container_width=False)
    st.write("""### Project by: **Adam Astiti**""")
    st.link_button('Linkedin', 'https://www.linkedin.com/in/adam-astiti-a3787312a/', icon='💼')
    st.link_button('Github', 'https://github.com/adam-astiti', icon='👨‍💻')


# TITLE
st.title("Chapter 1: The Job Market Lanscape")
st.markdown("First, let's get a high-level overview of the market. Where are the jobs, and is the market growing?")

# Chart
col1, col2 = st.columns(2)

with col1:
    st.image('Data Analysis\Result\Chapter 1 Question 1.png')

with col2:
    st.image('Data Analysis\Result\Chapter 1 Question 3.png')

st.image('Data Analysis\Result\Chapter 1 Question 2.png', use_container_width=True)

# Chart Explanation
with st.expander("Finding 1: (Click Here)"):
        st.header("Finding 1: Data Analyst is the Most In-Demand Role")
        st.write("""
The first key insight from the data is a powerful one: among all data-related roles, "Data Analyst" is the most demanded job title, with nearly 200,000 postings in 2023. It significantly surpasses even "Data Engineer" and "Data Scientist" roles.

This tells us that the ability to interpret data and translate it into business insights is a fundamental and highly sought-after skill in the industry. For anyone starting their career, this chart provides strong validation that "Data Analyst" is not just a viable path, but the most common entry point into the world of data.
        """)

with st.expander("Finding 2: (Click Here)"):
        st.header("Finding 2: The United States Dominates the Global Job Market")
        st.write("""
The United States is, by an overwhelming margin, the largest market for data analysts, with nearly 70,000 vacancies. This is more than five times the number of jobs in the second-place country, France. While there are significant opportunities in European nations like France, the UK, and Germany, as well as growing hubs in Asia like Singapore and India, the US remains the epicenter of the data analytics industry.
        """)


with st.expander("Finding 3: (Click Here)"):
        st.header("Finding 3: The Job Market Has a Clear Seasonal Rhythm")
        st.markdown("""
Now that we know the role is in high demand, the next question is when to look. The data reveals a distinct seasonal trend in hiring throughout the year.

The market kicks off with a massive hiring surge in January, making it the strongest month for job seekers. Following this peak, there's a noticeable dip in the late spring and early summer, with May and June being the slowest months. The market then rebounds for a second, smaller hiring wave in August before gradually tapering off towards the end of the year.

**The key takeaway**: Aspiring analysts should strategically time their job search to align with these peaks, particularly at the beginning of the year, to maximize their opportunities.
        """)


# Finding Summary
st.markdown("# Findings Summary")

st.markdown("""
Our initial exploration reveals a promising landscape: 
1. The "Data Analyst" role is the most in-demand in the data field 
2. Data Analyst Job opportunities are globally distributed, albeit with a heavy concentration in the United States.
2. The market follows a predictable yearly cycle, 

Now that we understand the "what," "when," and "where," the next logical step is to uncover the "how." Chapter 2 will dive into the specific skills and technologies required to land one of these promising roles.
            """)

