# 📈 Milestone 3 – Education–Employment Analysis

🎯 Project Overview: Barriers and Pathways into IT for Displaced Youth

## 🎯 Milestone Goal

To analyze how different educational backgrounds (traditional, bootcamp,
nonprofit, online) correlate with employment outcomes in IT, based on structured
LinkedIn profile data.

---

## 🧭 Main Research Question

> **What are the most accessible and employer-relevant career pathways into the
> IT sector for young displaced individuals without prior tech backgrounds in
> the U.S., and how do alternative education models compare to formal higher
> education in enabling their employment outcomes?**

---

## 📊 Research Focus

We focused on answering the following:

- What proportion of professionals have traditional degrees vs. non-traditional
  education?
- Which job roles are most common by education type?
- How well can education, location, and experience predict job type?

---

## 🔍 Our Collaborative Strategy

To address this broad and complex question, our team adopted a **modular
research approach** by dividing the work into **five interconnected
subquestions**. Each team member led one subquestion area, while contributing
to the collective understanding and integration across the dataset.

🔗 In [this document](https://docs.google.com/document/d/1BQfC2MTmwKbvtjebgo5HHW0UqTeh4TTK7OFb4HIMi6o/edit?tab=t.0#heading=h.2ykqoqwnn0re),
we detail our approach to the main research question, breaking it down into five
subquestions. Each section includes the data sources and findings contributed
by individual team members.

This structure helped ensure deeper focus, division of labor, and traceability
across sources, files, and findings. Eventually, insights from all subquestions
were synthesized to produce a cohesive analysis and set of recommendations.

---

## 🧩 Subquestion Structure

### 1. **Barriers and Demographics**

- **Lead:** Khadija  
- **Focus:** Identifying the most common barriers (cost, documentation,
  language), demographic distribution, English proficiency, and geographic
  concentration.  

---

### 2. **Entry-Level IT Opportunities**

- **Lead:** Shaima  
- **Focus:** Mapping accessible IT roles for those without a tech background and
  analyzing job posting requirements, salaries, and accessibility.  

---

### 3. **Education Models and Accessibility**

- **Lead:** Yuri  
- **Focus:** Comparing bootcamps, online training, and formal college pathways,
  including cost, completion rates, and eligibility constraints for displaced
  youth.  

---

### 4. **Employment Outcomes by Pathway**

- **Lead:** Yevheniia  
- **Focus:** Comparing outcomes (employment rates, salary, time to employment)
  for learners across different education pathways and demographic groups.  

---

### 5. **Employer Perceptions and Success Factors**

- **Leads:** Nelson & Simi  
- **Focus:** Understanding how employers evaluate different education
  backgrounds, and identifying program design features (e.g., mentorship,
  internships) that lead to success.  

---

## 🧠 Key Analysis Topics

- **Education Category Distribution** (bar chart)
- **Degree vs. Non-Degree Breakdown** (pie chart)
- **Job Type by Education Path** (stacked bar chart)
- **Exploratory ML Model** – predicting Software Engineer likelihood based on
  profile features

---

## 👥 Team Contributions (Milestone 3 Notebooks & Plots)

**Khadija al Ramlawi**  
_SubQuestion 1 Focus:_ Barriers and Demographics of Displaced Youth  
_Contribution Summary:_  

- Conducted literature review across 7+ refugee and immigration data sources  
- Extracted population, legal status, language, and education indicators  
- Cleaned and integrated multiple reports into one CSV master dataset
  Built `master_displaced_youth_it_pathways.csv`
- Built `SQ1_Barriers_and_Demographics_Analysis.ipynb` notebook for visual and descriptive analysis  
- Created bar and scatter charts illustrating top barriers and state-level trends  
- Provided plain-language summary with uncertainties and data limitations  

📘 Main analysis notebook: `SQ1_Barriers_and_Demographics_Analysis.ipynb`

---

**Shayma Mohamed**  
_SubQuestion 2 Focus:_ Entry-Level IT Opportunities  
_Contribution Summary:_  

- Cleaned and processed raw dataset of 21,961 U.S. IT job postings sourced from Glassdoor, Indeed, and ZipRecruiter  
- Built `SQ2_EntryLevel_IT_Opportunities_Analysis.ipynb` notebook  
- Conducted exploratory analysis to identify the most accessible job categories, share of no-degree/no-experience roles,
  and average salaries  
- Created visualizations highlighting entry-level opportunities by category and state  
- Summarized findings for integration into the main research synthesis  
- Identified key entry-level IT pathways most accessible for displaced youth

📘 Main analysis notebook: `SQ2_EntryLevel_IT_Opportunities_Analysis.ipynb`  

---

**Yuri Spizhovyi**  
_SubQuestion 3 Focus:_ Education vs. Job Role Correlation  
_Contribution Summary:_  

- Cleaned and engineered features in `cleaned_linkedin_profiles.csv`  
- Built `SQ3_Education_Models_and_Accessibility_analysis.ipynb` notebook  
- Performed visual and statistical analysis of job outcomes  
- Developed exploratory ML model (logistic regression) to test prediction of Software Engineer roles  
- Created all visualizations

> 📁 Final plots and charts are stored in `/figures/`.  
> 📘 Main analysis notebook: `SQ3_Education_Models_and_Accessibility_analysis.ipynb`

---

**Yevheniia Rudenko**  
_SubQuestion 4 Focus:_ Employment & Salary Outcomes by Education Pathway
_Contribution Summary:_

- Cleaned and prepared datasets comparing Bootcamps, Online Courses, and Colleges
- Built `SQ4_Employment_Outcomes_By_Education_Pathway_Analysis.ipynb` notebook
- Analyzed pre- and post-education salary data, employment rates, and salary growth
- Created all visualizations highlighting differences and trends
Noted key data limitations and uncertainties in the analysis

📘 Main analysis notebook: `SQ4_Employment_Outcomes_By_Education_Pathway_Analysis.ipynb`

---
**Nelson Fodjo Kamdoum**  
_Support role:_ Drafted visuals for comparing traditional vs. non-traditional outcomes

**Olubusayo Solola (Simi)**  
_Support role:_ Drafted sub-question framing and hypothesis testing

## 📌 Main Finding

**Accessible and employer-relevant IT career pathways for displaced youth without
prior tech backgrounds in the U.S. include entry-level roles such as IT Support,
QA Testing, and Junior Web Development — most commonly accessed via non-traditional
education models such as bootcamps, online platforms, and nonprofit programs.**

---

## ✅ Conclusion

While traditional degrees still correlate with higher salaries, **alternative
training models are proving to be viable, scalable, and accessible pathways for
displaced youth** — especially when designed with inclusion and support in mind.

The most effective IT pathways for displaced youth include:

- **Low-barrier entry-level roles** in IT support, QA, and web development  
- **Non-traditional education**: bootcamps, online learning, nonprofit programs  
- **Supportive program features**: mentorship, micro-credentials, and job placement  
- **Targeting high-immigrant states** like CA, TX, FL, and NY  
- **Cross-sector efforts** to reduce barriers tied to cost, documentation, and language

These findings show that with the right support, displaced youth can successfully
enter the IT sector—even without prior experience or formal education.

## 🔬 Limitations

- Education parsing was keyword-based and may miss non-standard program names
- Location fields were broad (city-level, not standardized)
- Not all profiles listed job history in full; most only included current role

---

## 📁 Folder Structure

```text
4_data_analysis/
│
├── SQ1_Barriers_and_Demographics_Analysis.ipynb   # Main analysis notebook Subquestion 1
├── SQ2_EntryLevel_IT_Opportunities_Analysis.ipynb   # Main analysis notebook Subquestion 2
├── SQ3_Education_Models_and_Accessibility_analysis.ipynb   # Main analysis notebook Subquestion 3
├── SQ4_Employment_Outcomes_By_Education_Pathway_Analysis.ipynb # Main analysis notebook Subquestion 4
├── SQ5_Employer_Perceptions_and_Success_Factors_Factor.ipynb   # Main analysis notebook Subquestion 5
└── README.md                             # ← This file
