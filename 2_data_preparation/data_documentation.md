# 📚 Data Documentation (Draft)

This document outlines each dataset collected and cleaned for our project:  
**"Career Pathways into IT for Displaced Youth in the U.S."**

Each dataset corresponds to a research sub-question or outcome metric.  
All files are stored in `/2_data_preparation/cleaned_data/`.

---

## 🔍 Sub-Questions & Team Assignments

### (Please change Sub-Question and Filename with the question assigned to you!!!)

| Sub-Question / Outcome Metric                          | Filename                         | Assigned Member   | Source|
|--------------------------------------------------------|----------------------------------|----------------------------|----------------------------------------------|
| % of job listings requiring no degree                  | `job_titles_no_degree.csv`       | Nelson Fodjo Kamdoum       | [Indeed API](link) or scraped CSV            |
| Bootcamp employment rate (within 6-12 months)          | `bootcamp_employment_rates.csv`  | Khadija al Ramlawi         | [CourseReport](link) or bootcamp survey data |
| Average salary after online training                   | `average_salary_post_training.csv`| Sara Şahin                 | [PayScale or Glassdoor](link)                |
| Median time to employment after training               | `time_to_employment.csv`         | Shayma Mohamed             | [LinkedIn reports](link)                     |
| % receiving employer sponsorship/apprenticeships       | `employer_sponsorships.csv`      | Olubusayo Solola           | [Workforce Dev Study](link)                  |
| % of students with digital literacy challenges         | `digital_literacy_challenges.csv`| Yevheniia Rudenko          | [UNHCR EdTech Report](link)                  |
| Enrollment share in alternative vs. college education  | `training_enrollment_split.csv`  | Niloufar Ahmadi            | [National Education Survey](link)            |
| Job retention after 1 year                             | `job_retention_1yr.csv`          | Yuri Spizhovyi             | [TechHire Data](link)                        |

---

## 🧼 Cleaning Methodologies

Each notebook in `/notebooks/` includes:

- Null handling
- Column renaming & normalization
- Filtering by country and age (18–25)
- Notes on source credibility and dataset bias

---

## 🧩 Notes & Limitations

- Some sources include global data — filtered for U.S. only
- Time-based fields were standardized to `YYYY-MM-DD`
- Survey-based data may include self-reporting bias
