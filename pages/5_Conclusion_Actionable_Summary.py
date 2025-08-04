import streamlit as st
from utils import css_load

st.set_page_config(
    page_title="Data Analyst Job Market Analysis",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded")

css_load()

# Title
st.title("Conclusion: The Data-Driven Roadmap to a Successful Analyst Career")

# Sidebar

with st.sidebar:
    st.image(r'streamlit-logo-primary-colormark-darktext.png', use_container_width=False)
    st.write("""### Project by: **Adam Astiti**""")
    st.link_button('Linkedin', 'https://www.linkedin.com/in/adam-astiti-a3787312a/', icon='💼')
    st.link_button('Github', 'https://github.com/adam-astiti', icon='👨‍💻')

# Naration
st.markdown("""
After a comprehensive analysis of over 700,000 job postings, our journey through the data has revealed a clear and actionable roadmap for aspiring data analysts. The path from novice to a top-tier, high-earning professional is not a matter of chance, but a strategic combination of acquiring the right skills, understanding the market, and positioning oneself effectively.

This summary synthesizes our key findings into a practical guide for success.

### 1. Master the Foundational Toolkit
- **The data is unequivocal**: a specific set of five skills forms the bedrock of the data analyst profession. These are not optional; they are the price of entry.

- **SQL is Non-Negotiable**: As the most demanded skill by a significant margin, deep proficiency in SQL is the single most important technical competency.

- **Embrace Python & Excel**: Following SQL, Python (for advanced analysis and automation) and Excel (for its ubiquity in business) are the next most critical tools.

- **Learn a BI Platform**: To translate data into insights, you must master a mainstream Business Intelligence tool. The market has clearly standardized on Tableau and Power BI.

**Actionable Advice**: Focus your learning on these five core technologies. Your portfolio must prominently feature projects that demonstrate your expertise in each.

### 2. Specialize to Maximize Your Earnings
While **foundational skills land you the job, specialization gets you the top-tier salary**. Our analysis showed that the highest-paying roles consistently demand skills that go beyond the basics.

- **Target High-Value Technologies**: Gaining experience with big data tools (Spark, Hadoop), cloud platforms (AWS), and advanced BI/Project Management software (Looker, Jira) directly correlates with higher compensation.

- **Think Globally**: While the US dominates in job volume, high salaries are a global phenomenon. Be open to opportunities in international tech hubs across Latin America, Europe, and Asia, where competitive compensation is common.

**Actionable Advice**: Once you are comfortable with the fundamentals, strategically learn a high-demand, specialized skill. This "T-shaped" knowledge (deep in the core, broad in specializations) is the key to unlocking salaries over $85,000.

### 3. Understand the Modern Workplace
The nature of work has changed, but it's crucial to navigate this new landscape with data, not just headlines.

- **On-site is Still the Standard**: With over **93%** of jobs being on-site, a job search limited only to remote roles will be significantly constrained. Be open to traditional roles to maximize your options.

- **Remote Work Offers Parity**: Crucially, our analysis shows no significant pay difference between remote and on-site roles. You do not need to accept a lower salary for the flexibility of working from home. The required skills are also identical.

**Actionable Advice**: View remote work as a powerful alternative, not a replacement for the traditional job market. You can pursue this flexibility without compromising your earning potential, as companies are paying for your skills, not your location.

## Final Summary
The successful data analyst of 2023 is a professional who builds a strong foundation in SQL, Python, and a major BI tool. They then strategically layer on specialized, high-value skills to increase their earning potential and are flexible in their approach to both global and remote work opportunities. By following this data-driven roadmap, any aspiring analyst can effectively navigate the job market and build a rewarding and lucrative career.
    """)
