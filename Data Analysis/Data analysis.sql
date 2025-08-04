/*The Story: "A Data-Driven Roadmap to Becoming a Top-Tier Data Analyst"
This story will guide an aspiring analyst from understanding the general job market to identifying the specific, high-value skills they need to land a top job.

Chapter 1: The Lay of the Land - What Does the Job Market Look Like?
(The goal here is to get a high-level overview.)

1. What are the most common job titles for data job? Are there more "Data Analyst" or "Business Analyst" roles?

2. How has the number of job postings trended over time? Are we seeing growth in the market? (You can analyze this by month).

3. Which countries have the most demand for data analysts? Where are the global hotspots for these roles?*/

SELECT
    job_title_short as job,
    count(*) as job_count 
FROM fact_data_job_view
GROUP BY job_title_short
ORDER BY job_count DESC

SELECT
    TO_CHAR(job_posted_date, 'Month') as month_name,
    EXTRACT(MONTH FROM job_posted_date) AS month,
    count(*) as job_posting_count
FROM fact_data_job_view
GROUP BY month_name, month
ORDER BY month ASC

SELECT
    country,
    count(*) as data_analyst_job
FROM fact_data_job_view
WHERE job_title_short = 'Data Analyst'
GROUP BY country
ORDER BY data_analyst_job DESC
LIMIT 10

/*Chapter 2: The Analyst's Toolkit - What Are the Most In-Demand Skills?
(Here, we dive into the core requirements of the job.)

1. What are the absolute top 5 most demanded skills for a data analyst? 
(This gives us the "must-have" list).

2. How do the skill requirements change for senior-level positions versus standard analyst roles? 
*/

SELECT 
    s.skills,
    count(*) as job_need_this_skill
FROM dim_skills_view as s
RIGHT JOIN fact_data_job_view as j ON j.job_id = s.job_id
WHERE j.job_title_short = 'Data Analyst'
GROUP BY skills
ORDER BY job_need_this_skill DESC
LIMIT 5

SELECT 
    s.skills,
    count(*) as job_need_this_skill
FROM dim_skills_view as s
RIGHT JOIN fact_data_job_view as j ON j.job_id = s.job_id
WHERE j.job_title_short = 'Senior Data Analyst'
GROUP BY skills
ORDER BY job_need_this_skill DESC
LIMIT 5

/*Chapter 3: The Payoff - How Do Skills and Location Impact Salary?
(Now we connect the skills to their monetary value.)

1. Which specific skills are most associated with high salaries? What is the average salary for jobs that require Python, AWS, or Tableau?

2. How do salaries for data analysts vary by country? Which countries offer the most competitive compensation?*/



WITH skill_num AS (
SELECT 
    s.skills,
    count(*) as job_need_this_skill
FROM dim_skills_view as s
RIGHT JOIN fact_data_job_view as j ON j.job_id = s.job_id
WHERE j.job_title_short = 'Data Analyst' AND skills IS NOT NULL
GROUP BY skills
ORDER BY job_need_this_skill DESC),
Quartiles AS (
    SELECT
        PERCENTILE_CONT(0.25) WITHIN GROUP (ORDER BY job_need_this_skill) AS Q1,
        PERCENTILE_CONT(0.75) WITHIN GROUP (ORDER BY job_need_this_skill) AS Q3
    FROM
        skill_num
),
free_outlier_skills AS(
SELECT
    t.*
FROM
    skill_num AS t, Quartiles AS q
WHERE
    t.job_need_this_skill < (q.Q1 - 1.5 * (q.Q3 - q.Q1)) OR
    t.job_need_this_skill > (q.Q3 + 1.5 * (q.Q3 - q.Q1)))

SELECT 
    s.skills,
    round(avg(annual_salary), 2) as average_salary
FROM dim_skills_view as s
RIGHT JOIN fact_data_job_view as j ON j.job_id = s.job_id
WHERE j.job_title_short = 'Data Analyst' AND skills in (SELECT skills from free_outlier_skills)
GROUP BY skills
ORDER BY average_salary DESC
LIMIT 10

WITH country_t AS(
SELECT 
    country,
    count(*) as country_count
FROM fact_data_job_view
GROUP BY country
ORDER BY country_count DESC
),
Quartiles AS (
    SELECT
        PERCENTILE_CONT(0.25) WITHIN GROUP (ORDER BY country_count) AS Q1,
        PERCENTILE_CONT(0.75) WITHIN GROUP (ORDER BY country_count) AS Q3
    FROM
        country_t
),
free_outlier_country AS(
SELECT
    t.*
FROM
    country_t AS t, Quartiles AS q
WHERE
    t.country_count < (q.Q1 - 1.5 * (q.Q3 - q.Q1)) OR
    t.country_count > (q.Q3 + 1.5 * (q.Q3 - q.Q1)))

SELECT
    country,
    ROUND(avg(annual_salary), 2) AS average_salary
FROM fact_data_job_view
WHERE country IN (SELECT country FROM free_outlier_country) AND job_title_short = 'Data Analyst'
GROUP BY country
ORDER BY average_salary DESC
LIMIT 10

/*Chapter 4: The Modern Workplace - The Rise of Remote Work
(We explore the flexibility and location-independence of the role.)

What percentage of data analyst jobs are fully remote?

Do remote jobs pay more or less than on-site positions?

What are the most in-demand skills for remote jobs? Are they different from on-site roles?*/

SELECT 
    ROUND(COUNT(CASE WHEN job_work_from_home IS TRUE THEN 1 END):: NUMERIC/COUNT(*),3) AS remote_percentage,
    1 - ROUND(COUNT(CASE WHEN job_work_from_home IS TRUE THEN 1 END):: NUMERIC/COUNT(*),3) AS onsite_percentage
FROM fact_data_job_view
where job_work_from_home IS NOT NULL AND job_title_short = 'Data Analyst'


SELECT
    CASE WHEN job_work_from_home IS TRUE THEN 'REMOTE'
    ELSE 'ONSITE' END AS remote_or_onsite,
    ROUND(avg(annual_salary), 2) as average_salary
FROM fact_data_job_view
WHERE job_title_short = 'Data Analyst'
GROUP BY job_work_from_home

SELECT 
    s.skills,
    count(*) as job_need_this_skill
FROM dim_skills_view as s
RIGHT JOIN fact_data_job_view as j ON j.job_id = s.job_id
WHERE j.job_title_short = 'Data Analyst' AND job_work_from_home IS TRUE AND Skills IS NOT NULL
GROUP BY skills
ORDER BY job_need_this_skill DESC
LIMIT 7

