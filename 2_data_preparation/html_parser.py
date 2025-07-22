import os
import re
import pandas as pd
from bs4 import BeautifulSoup
from datetime import datetime
import uuid

# === SETUP PATHS ===
html_dir = ""
output_csv = "raw_parsed_linkedin_output.csv"


# === EXTRACTOR FUNCTIONS ===
def extract_education_details(matches):
    school = degree = field = start = end = "N/A"
    for text in matches:
        lower = text.lower()
        if any(
            k in lower for k in ["university", "college", "institute", "universidad"]
        ):
            school = text
        elif "degree" in lower or "bachelor" in lower or "master" in lower:
            degree = text
        elif any(
            k in lower
            for k in [
                "science",
                "engineering",
                "computer",
                "networking",
                "telecommunications",
            ]
        ):
            field = text
        elif " - " in text and re.search(r"\d{4}", text):
            dates = re.findall(
                r"(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Sept|Oct|Nov|Dec)?\s*\d{4}",
                text,
            )
            years = re.findall(r"\d{4}", " ".join(dates))
            if len(years) >= 1:
                start = years[0]
            if len(years) >= 2:
                end = years[1]
        elif re.match(r"^\d{4}$", text):
            start = text
    return school, degree, field, start, end


def extract_experience_details(matches):
    position = company = start = end = "N/A"

    for i, text in enumerate(matches):
        if re.search(
            r"\bEngineer\b|\bDeveloper\b|\bManager\b|\bAnalyst\b|\bQA\b", text
        ):
            position = text
        elif "full-time" in text.lower() and i > 0:
            company = matches[i - 1]
        elif " - " in text and re.search(r"\d{4}", text):
            dates = re.findall(
                r"(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Sept|Oct|Nov|Dec)\s+\d{4}",
                text,
            )
            if len(dates) >= 1:
                start = re.search(r"\d{4}", dates[0]).group()
            if len(dates) >= 2:
                end = re.search(r"\d{4}", dates[1]).group()
            elif "present" in text.lower():
                end = "Present"
    return position, company, start, end


# === MAIN PARSER LOOP ===
profile_data = []

for filename in os.listdir(html_dir):
    if not filename.endswith(".html"):
        continue

    file_path = os.path.join(html_dir, filename)
    with open(file_path, encoding="utf-8") as f:
        raw_html = f.read()

    soup = BeautifulSoup(raw_html, "html.parser")
    matches = re.findall(r"<!---->(.*?)<!---->", raw_html)
    filtered_matches = [text.strip() for text in matches if text.strip()]

    # === DEBUG ===
    print(f"\n=== {filename} ===")
    for i, match in enumerate(filtered_matches):
        print(f"{i}: {match}")

    # === BASIC FIELDS ===
    name = soup.find("h1").get_text(strip=True) if soup.find("h1") else "N/A"
    location_el = soup.select_one(
        "span.text-body-small.inline.t-black--light.break-words"
    )
    location = location_el.get_text(strip=True) if location_el else "N/A"

    # === APPLY EXTRACTORS ===
    edu_school, edu_degree, edu_field, edu_start, edu_end = extract_education_details(
        filtered_matches
    )
    exp_position, exp_company, exp_start, exp_end = extract_experience_details(
        filtered_matches
    )

    profile_data.append(
        {
            "File": filename,
            "Scrape_ID": str(uuid.uuid4()),
            "Scrape_Date": datetime.today().strftime("%Y-%m-%d"),
            "Name": name,
            "Location": location,
            "Experience_1": exp_position,
            "Company_1": exp_company,
            "Date_1_start": exp_start,
            "Date_1_end": exp_end,
            "Education_1": edu_school,
            "Degree": edu_degree,
            "Field": edu_field,
            "Education_Start": edu_start,
            "Education_End": edu_end,
        }
    )

# === SAVE TO CSV ===
df = pd.DataFrame(profile_data)
df.to_csv(output_csv, index=False)
print(f"\n✅ Parsed data saved to: {output_csv}")
