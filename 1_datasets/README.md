# Datasets

This folder contains all data resources necessary for the analysis, divided into the following subfolders:

## Folder Structure

### `cleaned_data/`

Contains datasets that have been cleaned and pre-processed, making them ready for analysis.
It also includes a guide for understanding the structure and content of the cleaned datasets.

### `raw_data/`

Includes raw, unprocessed data files as well as supporting documentation. This folder provides the foundational
resources, such as original datasets and descriptive metadata, for preprocessing and validation tasks.

---

## Usage Notes

- Detailed descriptions of each dataset can be found in the `data_discription.md` file located in the `raw_data/` folder.
This file contains descriptions of all resources and documents.  
- Always document any modifications to the files and ensure updates are pushed to the repository.

---

## How We Modeled the Domain

To understand and analyze our data, we first organized it into clear categories that represent
real-world concepts in our project.

- **Raw Data:** This is the original, unprocessed information we collected.
Think of it like ingredients in their natural state.  
- **Cleaned Data:** We processed the raw data to fix errors, fill missing pieces, and organize it better — like preparing
those ingredients for cooking.  
- **Documentation:** We also kept detailed notes describing what each dataset contains, so anyone can understand and
use them correctly.  
- **Jupyter Notebooks:** All the notebooks used for cleaning and analyzing data are saved and worked on in the folder:  
  `2_data_preparation` — this helps us keep track of all data processing steps and ensure reproducibility.

### Research Question Breakdown

We divided the main research question into several sub-questions to better address different aspects of the analysis.
This approach helps us focus on specific problems step-by-step and makes the investigation clearer and more manageable.

### Why This Approach?

By separating raw and cleaned data, and keeping the notebooks organized in one place, we make sure that we always have
the original information to refer back to if needed, while also working with ready-to-use, reliable data for analysis.

---

## Possible Flaws in This Approach

- **Data Duplication:** Keeping both raw and cleaned versions may take up extra storage space.  
- **Version Confusion:** If changes to cleaned data aren’t properly documented or synced, it can cause inconsistencies.
- **Limited Automation:** Manual cleaning steps can introduce human error and make it harder to reproduce results exactly.

---

## Visual Overview

Here’s a simple diagram illustrating our data flow:
