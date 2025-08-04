# Data Analyst Job Market Analysis (2023)
![streamlit](https://github.com/user-attachments/assets/e036a02a-e882-40fc-b68c-67d22bbd8fc3)

[View the Live Interactive Dashboard Here](https://datajobsqlproject.streamlit.app/)
# Project Overview
This project performs a comprehensive, end-to-end analysis of the data analyst job market using a dataset of over 700,000 job postings from 2023. The goal is to provide a data-driven roadmap for aspiring data analysts by answering critical questions about in-demand skills, salary expectations, and the modern work landscape.

The project showcases a complete data workflow, from initial data preparation and warehousing to in-depth analysis and final presentation in a live, interactive Streamlit dashboard. Check the dashboard here [Streamlit Data Storytelling Dashboard](https://datajobsqlproject.streamlit.app/)

# Data Source
The dataset used for this analysis is too large (150MB+) to be hosted on GitHub. If you are interested in the raw and cleaned datasets, you can access them via the following link:

[Download the Dataset from Google Drive](https://drive.google.com/drive/u/0/folders/1rSHk8MFsiWnKlHMHfdDjwWKCCqGNd-Pz)

# Analysis & Storytelling
This analysis is structured as a story in four chapters, guiding an aspiring data analyst from a high-level market overview to specific, actionable insights for their career. To further check

## Chapter 1: The Job Market Landscape
Before diving into specifics, we first need to survey the entire landscape. Where do data analysts fit in the tech ecosystem, and where are the opportunities?
<table>
<tr>
<td><img width="100%" alt="Chapter 1 Question 1" src="https://github.com/user-attachments/assets/695f2d6d-690c-475d-ba78-4943a8cbfcf4" /></td>
<td><img width="100%" alt="Chapter 1 Question 3" src="https://github.com/user-attachments/assets/aa2aadda-4270-4308-87be-9184d3e4f74d" /></td>
</tr>
</table>

**Key Insight**: The "Data Analyst" role is the most common entry point into the data field, with a strong, seasonal hiring market dominated by the United States.

## Chapter 2: The Analyst's Toolkit
What skills are required for the job, and how do those requirements change as one advances in their career?
<table>
<tr>
<td><img width="100%" alt="Chapter 2 Question 1" src="https://github.com/user-attachments/assets/af65ad5d-121f-47e1-bb8d-48b6d38c4db1" /></td>
<td><img width="100%" alt="Chapter 2 Question 2" src="https://github.com/user-attachments/assets/39c6dd07-7c73-441a-a504-d442f2dabf1a" /></td>
</tr>
</table>

**Key Insight**: SQL is the unshakeable foundation for all analyst roles. To advance to a senior level, expertise in Python becomes significantly more important, and specialized statistical tools like R emerge.

## Chapter 3: Connecting Skills and Location to Salary
What is the financial return on these skills, and where are the most lucrative opportunities?
<table>
<tr>
<td><img width="989" height="490" alt="Chapter 3 Question 1" src="https://github.com/user-attachments/assets/676cc572-22da-4ad5-9604-9cb743934fd5" /></td>
<td><img width="990" height="490" alt="Chapter 3 Question 2" src="https://github.com/user-attachments/assets/af4ccac1-b11d-4761-bce2-7147053e0b66" /></td>
</tr>
</table>

**Key Insight**: While foundational skills get you the job, specialization in high-demand technologies like big data and cloud platforms is what drives top-tier salaries. High salaries are a global phenomenon, not limited to a single country.

## Chapter 4: The Remote Job Landscape
How has the rise of remote work impacted the data analyst field in terms of opportunity and compensation?
<table>
<tr>
<td><img width="100%" alt="Chapter 4 Question 1" src="https://github.com/user-attachments/assets/12074bf3-fc0c-4b4b-ac21-b1d125b4979d" /></td>
<td><img width="100%" alt="Chapter 4 Question 2" src="https://github.com/user-attachments/assets/8d000757-a6bd-4d12-a4a6-bbabe9326ca7" /></td>
</tr>
<tr>
<td colspan="2"><img width="100%" alt="Chapter 4 Question 3" src="https://github.com/user-attachments/assets/81ed0732-ba73-4835-a167-d02d8f358590" /></td>
</tr>
</table>

**Key Insight**: While on-site roles still constitute the vast majority of the market (>93%), remote jobs offer virtually identical average salaries. The core skills required for remote work are the same as for on-site positions, making it a viable alternative without a financial penalty.

# Technical Workflow & Pipeline
1. **Data Preparation (Python & Pandas)**: The raw dataset was first loaded into a Jupyter Notebook for initial pre-processing, data type correction, and cleaning of special characters to ensure a smooth database loading process.

2. **Data Warehousing (PostgreSQL)**: A relational database was designed using a Star Schema. The cleaned data was loaded, and further transformations were performed using SQL, including standardizing salaries and imputing missing values with a multi-level median approach.

3. **Data Analysis (SQL & Python)**: All analytical queries were written in SQL. The results were then visualized using Python's Seaborn library in a separate Jupyter Notebook.

4. **Presentation (Streamlit)**: The final insights and charts were compiled into an interactive, multi-page web application using Streamlit and deployed to the web.

# Repository Structure
- **Home.py**: The main script for the Streamlit homepage and application entry point.

- **pages/**: This directory holds the Python scripts for each individual page of the dashboard, which Streamlit automatically detects for navigation.

- **Data Warehousing/**: Contains all scripts related to the ETL process and database setup.

- **Data Analysis/**: Contains the SQL queries for analysis, the Python notebook for visualization, and the final chart/data results.

# Technologies Used
- **Programming Languages**: Python, SQL (PostgreSQL)

- **Python Libraries**: Pandas, Seaborn, Streamlit

- **Database**: PostgreSQL

- **Web Framework**: Streamlit

- **Version Control**: Git & GitHub
