# 📈 Milestone 3 – Education–Employment Analysis

This folder contains all analysis and modeling work for Milestone 3 of the project:  
**“Career Pathways into IT for Displaced Youth in the U.S. (2025)”**

---

## 🎯 Milestone Goal

To analyze how different educational backgrounds (traditional, bootcamp, nonprofit, online) correlate with employment
outcomes in IT, based on structured LinkedIn profile data.

---

## 📊 Research Focus

We focused on answering the following:

- What proportion of professionals have traditional degrees vs. non-traditional education?
- Which job roles are most common by education type?
- How well can education, location, and experience predict job type?

---

## 🧠 Key Analysis Topics

- **Education Category Distribution** (bar chart)
- **Degree vs. Non-Degree Breakdown** (pie chart)
- **Job Type by Education Path** (stacked bar chart)
- **Exploratory ML Model** – predicting Software Engineer likelihood based on profile features

---

## 👥 Team Contributions (Milestone 3 Notebooks & Plots)

**Khadija al Ramlawi**  
_Support role:_ Reviewed variable mappings and education tagging logic

**Nelson Fodjo Kamdoum**  
_Support role:_ Drafted visuals for comparing traditional vs. non-traditional outcomes

**Olubusayo Solola (Simi)**  
_Support role:_ Drafted sub-question framing and hypothesis testing

**Sara Şahin**  
_Support role:_ Reviewed career entry paths for QA and Data Analyst roles

**Shayma Mohamed**  
_Support role:_ Assisted in data validation and research question alignment

---

**Yevheniia Rudenko**  
_Subquestion Focus:_ Employment & Salary Outcomes by Education Pathway
_Contribution Summary:_

- Cleaned and prepared datasets comparing Bootcamps, Online Courses, and Colleges
- Built `data_analysis_on_employment_outcomes_by_education_pathway.ipynb` notebook
- Analyzed pre- and post-education salary data, employment rates, and salary growth
- Created all visualizations highlighting differences and trends
Noted key data limitations and uncertainties in the analysis

📘 Main analysis notebook: `data_analysis_on_employment_outcomes_by_education_pathway.ipynb`

---

**Yuri Spizhovyi**  
_Subquestion Focus:_ Education vs. Job Role Correlation  
_Contribution Summary:_  

- Cleaned and engineered features in `cleaned_linkedin_profiles.csv`  
- Built `education_employment_analysis.ipynb` notebook  
- Performed visual and statistical analysis of job outcomes  
- Developed exploratory ML model (logistic regression) to test prediction of Software Engineer roles  
- Created all visualizations

> 📁 Final plots and charts are stored in `/figures/`.  
> 📘 Main analysis notebook: `education_employment_analysis.ipynb`

---

## 🔬 Limitations

- Education parsing was keyword-based and may miss non-standard program names
- Location fields were broad (city-level, not standardized)
- Not all profiles listed job history in full; most only included current role

---

## 📁 Folder Structure

```text
4_data_analysis/
│
├── data_analysis_on_employment_outcomes_by_education_pathway.ipynb  # Main analysis notebook SQ4
├── education_employment_analysis.ipynb   # Main analysis notebook SQ3
└── README.md                             # ← This file
