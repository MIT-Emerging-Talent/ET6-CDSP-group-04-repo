
# 📊 Milestone 2 – Data Collection & Preparation

This folder contains all Milestone 2 work for the project:  
**“Career Pathways into IT for Displaced Youth in the U.S. (2025)”**

---

## 🎯 Project Research Question

> What are the most accessible and employer-relevant career pathways into the IT sector
> for displaced youth in the U.S. with no prior tech background, and how do alternative
> education models compare to formal degrees in enabling successful employment?

Our team explored this problem by breaking it into measurable sub-questions, each focused on different
aspects of accessibility, training options, barriers, and employment outcomes. The goal is to collect, clean,
and document relevant datasets that can support later analysis of these pathways.

---

## 🧠 Modeling the Domain (Non-Technical Explanation)

To study this complex real-world issue, we broke it down into measurable outcome metrics such as:

- Employment rate after bootcamp or online training
- Average salary after completing non-traditional programs
- Time to first job
- Retention rate after one year
- Digital literacy barriers
- Employer preferences and sponsorship trends

Each team member focused on one of these sub-questions and identified a relevant dataset. All data was cleaned individually
and stored in a consistent format (CSV) to support later analysis.

### ⚠️ Limitations

- Many sources are self-reported (e.g., bootcamp surveys)
- We focused only on U.S.-based data
- Some important factors (e.g., mentorship, trauma) were not available in structured data

---

## 👥 Team Contributions (Milestone 2 Notebooks & Datasets)

**Khadija al Ramlawi**  
_Subquestion Focus:_ Barriers and Demographics  
_Contribution Summary:_  
Investigated cost, documentation, and language barriers to IT training for displaced  
youth. Collected data on population, unemployment, and education status from sources  
like UNHCR and ACS.

---

**Nelson Fodjo Kamdoum**  
_Subquestion Focus:_ Employer Perceptions & Success Factors  
_Contribution Summary:_  
Analyzed employer preferences for training types and success factors (e.g.,  
internships, mentorship) that affect displaced youth employment.

---

**Olubusayo Solola (Simi)**  
_Subquestion Focus:_ Employer Perceptions & Success Factors  
_Contribution Summary:_  
Collaborated with Nelson to analyze employer perspectives and outcomes by  
education type.

---

**Sara Şahin**  
_Subquestion Focus:_ Entry-Level IT Opportunities  
_Contribution Summary:_  
Explored accessible job roles for newcomers with no tech background. Focused on job  
posting requirements and entry-level salary benchmarks.

---

**Shayma Mohamed**  
_Subquestion Focus:_ Entry-Level IT Opportunities  
_Contribution Summary:_  
Collaborated with Sara to define the most common entry-level tech positions and  
what credentials they require.

---

**Yevheniia Rudenko**  
_Subquestion Focus:_ Employment Outcomes by Pathway  
_Contribution Summary:_  
Analyzed employment and salary outcomes based on training type (bootcamp vs.  
college). Focused on post-training job timing and demographic variation.
Output:`cleaned_data/cleaned_IT_Career_Outcomes_USA_Combined_By_EducationType_Demographics.csv`

---

**Yuri Spizhovyi**  
_Subquestion Focus:_ Education Models & Accessibility  
_Contribution Summary:_  
Collected and cleaned a dataset of IT training programs (bootcamps, colleges,  
support orgs). Normalized cost, length, and accessibility into structured data using  
`data_cleaning_us_it_programs.ipynb`. Outputs: `raw_us_it_programs.csv`,  
`cleaned_us_it_programs.csv`.

> 📌 All cleaned datasets are located in `/1_datasets/cleaned_data/`. Cleaning notebooks are stored in `/2_data_preparation/`.

---

## 🧾 Dataset Reproducibility & Structure

- All notebooks are designed to read raw data from `/1_datasets/raw_data/`
- Cleaned `.csv` outputs are saved in `/1_datasets/cleaned_data/`
- No raw file is overwritten. All steps are traceable and reproducible.

---

## 🧠 How We Modeled the Domain (Non-Technical Overview)

We modeled the domain by identifying several key components of an IT career pathway:

- Access to IT training (availability, cost, eligibility)
- Demographic barriers (e.g., English, legal status)
- Types of education models (online, bootcamps, colleges)
- Job market entry points (entry-level roles, salaries)
- Employer perceptions of non-traditional credentials
- Employment outcomes (time to employment, salaries, by pathway)

Each subquestion was assigned to a team member. They collected datasets, created cleaning notebooks, and produced
standardized `.csv` files for reuse and analysis.

## 📁 Folder Structure

```text
ET6-CDSP-GROUP-04-REPO/
│
├── 1_datasets/
│   ├── raw_data/           # Original source files (not modified)
│   ├── cleaned_data/       # Final cleaned datasets
│   └── guide.md            # Guide for dataset use
│
├── 2_data_preparation/
│   ├── README.md           # ← This file
│   ├── guide.md            # How to clean + prepare data
│   ├── data_documentation.md  # Short summaries of each dataset
│   ├── draft_data_description.md # Notes and scratch space
│   └── *.ipynb             # One notebook per team member
```

---

## 👥 Team Workflow

Each member:

- Selected one outcome metric
- Collected a relevant dataset
- Created a notebook with all cleaning steps
- Produced a final cleaned `.csv`
- Documented the process in `data_documentation.md`
