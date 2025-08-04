/*I designed and built a data mart using a full ETL process and a star schema. 
As the final step, I created views to provide a simplified and secure access layer for data analysis.*/

--Load data from csv into database

--create databese
CREATE DATABASE data_job_project;

--create table
CREATE TABLE public.dsjob_vacancy_fact (
    job_id INT PRIMARY KEY,
    job_title_short VARCHAR(255),
    job_title TEXT,
    job_via TEXT,
    job_schedule_type TEXT,
    job_work_from_home BOOLEAN,
    job_health_insurance BOOLEAN,
    search_location TEXT,
    job_location TEXT,
    job_posted_date DATE,
    job_no_degree_mention BOOLEAN,
    job_country TEXT,
    company_name TEXT,
    salary_rate VARCHAR(50),
    salary_year_avg NUMERIC,
    salary_hour_avg NUMERIC,
    skills TEXT

);

ALTER TABLE public.dsjob_vacancy_fact OWNER to postgres;

--copy data from csv into table in database
COPY dsjob_vacancy_fact (
    job_id,
    job_title_short,
    job_title,
    job_location,
    job_via,
    job_schedule_type,
    job_work_from_home,
    search_location,
    job_posted_date,
    job_no_degree_mention,
    job_health_insurance,
    job_country,
    salary_rate,
    salary_year_avg,
    salary_hour_avg,
    skills,
    company_name
)
FROM 'D:\Project\Sql\Ready_DS_Job_Dataset.csv'
DELIMITER ';' CSV HEADER;

--Database Normalization

--1.Create new fact and dim tables

CREATE TABLE dim_skills (
    skills_id SERIAL PRIMARY KEY,
    skills VARCHAR(100) UNIQUE
);

CREATE TABLE dim_company (
    company_id SERIAL PRIMARY KEY,
    company TEXT UNIQUE
);

CREATE TABLE dim_job_platform (
    platform_id SERIAL PRIMARY KEY,
    platform TEXT UNIQUE
);

CREATE TABLE public.fact_dsjob_vacancies (
    job_id INT PRIMARY KEY,
    job_title_short VARCHAR(255),
    job_title TEXT,
    job_work_from_home BOOLEAN,
    job_health_insurance BOOLEAN,
    search_location TEXT,
    job_location TEXT,
    job_posted_date DATE,
    job_no_degree_mention BOOLEAN,
    job_country TEXT,
    salary_rate VARCHAR(50),
    salary_year_avg NUMERIC,
    salary_hour_avg NUMERIC,

    company_id INT REFERENCES public.dim_company(company_id),
    platform_id INT REFERENCES public.dim_job_platform(platform_id)
);

CREATE TABLE dim_job_skill (
    job_id INT REFERENCES public.fact_dsjob_vacancies(job_id),
    skills_id INT REFERENCES public.dim_skills(skills_id)
);

--2. insert data into those tables

BEGIN;
--dim_company table
INSERT INTO public.dim_company (company)
SELECT DISTINCT company_name
FROM dsjob_vacancy_fact
WHERE company_name IS NOT NULL
ON CONFLICT (company) DO NOTHING;

--dim_job_platform
INSERT INTO public.dim_job_platform (platform)
SELECT DISTINCT job_via
FROM dsjob_vacancy_fact
WHERE job_via IS NOT NULL
ON CONFLICT (platform) DO NOTHING;

--dim_skills
INSERT INTO public.dim_skills (skills)
SELECT DISTINCT TRIM(unnested_skill)
FROM 
    public.dsjob_vacancy_fact,
    unnest(string_to_array(skills, ',')) AS unnested_skill
WHERE skills IS NOT NULL AND TRIM(unnested_skill) <> ''
ON CONFLICT (skills) DO NOTHING

--fact_table
INSERT INTO public.fact_dsjob_vacancies (
    job_id, job_title_short, job_title, job_work_from_home, job_health_insurance,
    search_location, job_location, job_posted_date, job_no_degree_mention, job_country,
    salary_rate, salary_year_avg, salary_hour_avg,
    company_id, platform_id
)
SELECT
    jvf.job_id, jvf.job_title_short, jvf.job_title, jvf.job_work_from_home, jvf.job_health_insurance,
    jvf.search_location, jvf.job_location, jvf.job_posted_date, jvf.job_no_degree_mention, jvf.job_country,
    jvf.salary_rate, jvf.salary_year_avg, jvf.salary_hour_avg,
    c.company_id, js.platform_id
FROM dsjob_vacancy_fact AS jvf
LEFT JOIN public.dim_company AS c ON jvf.company_name = c.company
LEFT JOIN public.dim_job_platform AS js ON jvf.job_via = js.platform;

select *
from fact_dsjob_vacancies
limit 100

--insert data into bridge table
INSERT INTO public.dim_job_skill (job_id, skills_id)
SELECT
    jvf.job_id,
    s.skills_id
FROM public.dsjob_vacancy_fact AS jvf,
     unnest(string_to_array(jvf.skills, ',')) AS unnested_skill
JOIN public.dim_skills AS s ON TRIM(unnested_skill) = s.skills;

COMMIT;

select * from dim_job_skill

--data cleaning. salary column is devided by hourly salary and yearly salary. we need to make it into one column
--there is a lot of null value in salary. better fill null value with median salary from same job in same country
--if still null then we need to fill with medial salary of all job in same country

--new column to combine salary data
ALTER TABLE fact_dsjob_vacancies
ADD COLUMN annual_salary NUMERIC;

--further clean the data by coalesce to fill null with median salary with same job in same country and median salary for same country
UPDATE fact_dsjob_vacancies
SET annual_salary =
    CASE 
        WHEN salary_rate = 'hour' THEN round(salary_hour_avg * 2080, 2)
        WHEN salary_rate = 'year' THEN round(salary_year_avg, 2) 
        ELSE NULL 
    END;

WITH JobCountryMedian AS (
    SELECT
        job_title_short,
        job_country,
        round(CAST(PERCENTILE_CONT(0.5) WITHIN GROUP (ORDER BY annual_salary) AS NUMERIC), 2) as median_salary_jc
    FROM
        fact_dsjob_vacancies
    WHERE 
        annual_salary IS NOT NULL
    GROUP BY 
        job_title_short,
        job_country
),
CountryMedian AS (
    SELECT
        job_country,
        round(CAST(PERCENTILE_CONT(0.5) WITHIN GROUP (ORDER BY annual_salary) AS NUMERIC), 2) as median_salary_c
    FROM
        fact_dsjob_vacancies
    WHERE
        annual_salary IS NOT NULL
    GROUP BY job_country
)

UPDATE fact_dsjob_vacancies
SET 
    annual_salary = COALESCE(
        fact_dsjob_vacancies.annual_salary, 
        JobCountryMedian.median_salary_jc, 
        CountryMedian.median_salary_c
    )
FROM 
    JobCountryMedian
LEFT JOIN 
    CountryMedian ON JobCountryMedian.job_country = CountryMedian.job_country
WHERE 
    -- connect to fact table based on job and country
    fact_dsjob_vacancies.job_title_short = JobCountryMedian.job_title_short
    AND fact_dsjob_vacancies.job_country = JobCountryMedian.job_country
    -- Just update Null data
    AND fact_dsjob_vacancies.annual_salary IS NULL;

--delete 'via ' string from all job platform data
UPDATE dim_job_platform
SET 
    platform =  REPLACE(dim_job_platform.platform, 'via ', '')



--create view to make data analysis process simpler and just include columns that possibly used in analysis

CREATE VIEW fact_data_job_view AS
SELECT
    f.job_id,
    f.job_title_short,
    f.job_country as country,
    f.job_posted_date,
    f.job_no_degree_mention,
    f.job_health_insurance,
    f.job_work_from_home,
    c.company,
    p.platform,
    f.annual_salary
from fact_dsjob_vacancies as f
join dim_company as c on f.company_id = c.company_id
join dim_job_platform as p on p.platform_id = f.platform_id

/*create another view for skills table. 
because skills table have many to many relationship,
we cant just join it into our main view. it will cause duplicate data, 
so we need create view for skills then join it when necessary in analysis processes*/

CREATE VIEW dim_skills_view AS
SELECT
    j.job_id,
    j.skills_id,
    s.skills
FROM dim_job_skill as j
JOIN dim_skills as s on j.skills_id = s.skills_id


