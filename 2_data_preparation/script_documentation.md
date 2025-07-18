# 🧾 Script Documentation: Data Preparation Tools

This file documents the two core scripts used during the data preparation phase of Milestone 2 and Milestone 3:

- `linkedin_profile_scraper.py`
- `html_parcer.py`

---

## 🕷️ 1. `linkedin_profile_scraper.py`

🎯 Purpose

Automates the scraping of full LinkedIn profile HTML pages using Playwright, simulating human behavior to reduce detection
and collect comprehensive page content.

### 🔧 Key Features

- **Manual Login Pause**: Waits for user to authenticate before scraping begins
- **Search Pagination**: Extracts profile URLs across multiple result pages
- **Simulated Behavior**: Implements human-like scrolling, hovering, and random clicking
- **Randomized Timing**: Adjusts delays based on time of day to avoid pattern detection
- **HTML Saving**: Saves full profile HTML in `/linkedin_html_profiles/`
- **Index Logging**: Outputs `linkedin_profile_index.csv` containing name, URL, and filename

### 📁 Outputs

- `linkedin_html_profiles/*.html` — raw HTML files per profile

---

## 🧪 2. `html_parcer.py`

🎯 Purpose

Parses each saved HTML profile into structured data, extracting educational and professional information for downstream analysis.

### 🔍 Fields Extracted

- `Name`, `Location`
- `Experience_1`: job title, company, start/end years
- `Education_1`: school, degree, field, start/end years

### 🔧 Implementation Details

- Uses BeautifulSoup to parse HTML
- Extracts visible and hidden text spans (`<!---->`-style)
- Applies regex to match dates and standard phrases
- Adds metadata: `Scrape_ID` (UUID), `Scrape_Date`, and original `File` name

### 📁 Output

- `raw_parsed_linkedin_output.csv`: Structured dataset containing parsed profile information

---

## ⚠️ Known Limitations

| Script | Limitation |
|--------|------------|
| `li_profile_scraper.py` | Requires manual login, not stealthy for high-volume scraping |
| `html_parcer.py` | Relies on keyword/regex matching and may miss some details or misclassify fields |

---

> 📦 Together, these two scripts enable the full pipeline from raw profile scraping to structured data extraction
> for analysis in Milestone 3.
