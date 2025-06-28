
# 📊 Data Preparation – Milestone 2

This folder contains all resources for **Milestone 2: Data Collection** for the project _“Career Pathways into IT for
Displaced Youth (U.S.)”_.

Our goal is to collect, clean, and document datasets related to our group’s research question:

> _What are the most accessible and employer-relevant career pathways into the IT sector for young displaced individuals
> without prior tech backgrounds in the U.S., and how do alternative education models compare to formal higher education
> in enabling their employment outcomes?_

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

## 📁 Folder Structure

```text
ET6-CDSP-GROUP-04-REPO/
│
├── data/
│   ├── raw/             # Original unmodified datasets
│   ├── cleaned/         # Final cleaned datasets used for exploration/analysis
│   └── processed/       # Optional: model-ready transformed data (if applicable)
│
├── notebooks/
│   ├── cleaning/        # Notebooks used in Milestone 2 for data cleaning
│   ├── exploration/     # EDA notebooks for Milestone 3
│   └── analysis/        # Final analysis notebooks for Milestone 4
│
├── 2_data_preparation/  # This README and supporting milestone documentation
├── data_documentation.md                   ← This document
```

---

## 👥 Team Workflow

Each member:

- Selected one outcome metric
- Collected a relevant dataset
- Created a notebook with all cleaning steps
- Produced a final cleaned `.csv`
- Documented the process in `data_documentation.md`
