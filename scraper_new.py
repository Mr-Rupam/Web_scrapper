from googlesearch import search
import pandas as pd
from urllib import parse
import re
import time
from openpyxl import Workbook
from openpyxl.styles import Font
import csv
# Search terms to query for LinkedIn profiles
search_terms = [
    "CTO",
    "Co-Founder","Founder",'CMO','CFO','COO'
]

# Function to perform Google search and extract LinkedIn profile info
def get_linkedin_profiles(company_name):
    print(f"-------------------------{company_name}-------------------------------")
    profiles = []
    seen_profiles = set()  # Set to track unique profiles

    for term in search_terms:
        query = f"{company_name} linkedin india {term}"

        try:
            search_results = list(search(query, num_results=3))  # Fetch top 3 results
        except Exception as e:
            print(f"Error performing search for {query}: {e}")
            continue

        for result in search_results:
            if "linkedin.com" in result:
                path = parse.urlparse(result).path

                # Check if the URL points to a user profile
                if path.split("/")[1] == "in":
                    profile_name = result.split("/in/")[-1].split("-")

                    # Filter and clean profile names
                    pattern = re.compile(r"^[A-Za-z]+$")
                    filtered_profile_name = [
                        item for item in profile_name if pattern.match(item)
                    ]
                    profile_name = " ".join(filtered_profile_name).title()

                    if profile_name not in seen_profiles:  # Avoid duplicates
                        seen_profiles.add(profile_name)
                        print(profile_name)
                        profiles.append((profile_name, term, result))
                        print(profile_name, result, term)
                        print("\n\n")

    return profiles

# Input and output file paths
input_file = "input_companies.csv"
output_file = "linkedin_profiles_trial.xlsx"

# Read the company names from the input CSV
with open(input_file, "r") as csvfile:
    companies = [row[0] for row in csv.reader(csvfile)]
    total_companies = len(companies)

# Initialize workbook
wb = Workbook()
ws = wb.active
ws.title = "LinkedIn Profiles"
ws.append(["Profile Name", "Company Name", "Role", "LinkedIn URL"])

# Process each company and write data
for i, company in enumerate(companies):
    profiles = get_linkedin_profiles(company)
    for profile in profiles:
        # Add hyperlink with display text "Link"
        cell = ws.cell(row=ws.max_row + 1, column=4)
        cell.value = "Link"  # Display text
        cell.hyperlink = profile[2]  # Hyperlink URL
        cell.font = Font(color="0000FF", underline="single")  # Format as hyperlink
        ws.cell(row=ws.max_row, column=1).value = profile[0]  # Profile Name
        ws.cell(row=ws.max_row, column=2).value = company     # Company Name
        ws.cell(row=ws.max_row, column=3).value = profile[1]  # Role

    # Update progress
    progress = int((i + 1) / total_companies * 40)
    print(f"[{('#' * progress)}{(' ' * (40 - progress))}]", end="\r")
    time.sleep(0.1)

# Save workbook
wb.save(output_file)
print(f"\nLinkedIn profiles saved to {output_file}")

