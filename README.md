# LinkedIn Profile Scraper

This Python script automates the extraction of LinkedIn profiles for specific roles (e.g., CTO, Co-Founder, etc.) in companies. It performs Google searches, filters LinkedIn profile URLs, and exports the results into an Excel file.

---

## Features
- Searches for LinkedIn profiles based on company names and predefined roles.
- Filters out duplicates and ensures clean data.
- Outputs results in an Excel file with hyperlinks to the LinkedIn profiles.

---

## Prerequisites

Ensure you have the following installed:
- Python 3.8 or above
- Required Python packages (listed below)

---

## Installation

1. Clone this repository or download the script.
2. Install the required Python packages by running:
   ```bash
   pip install serpapi openpyxl pandas

   ```

---

## Input Data

Prepare a CSV file named `input_companies.csv` with a single column containing the company names you want to search for. For example:

```
Company A
Company B
Company C
```

---

## Usage

1. Place the `input_companies.csv` file in the same directory as the script.
2. Run the script:
   ```bash
   python scraper_new.py
   ```
3. The script will:
   - Read company names from `input_companies.csv`.
   - Perform Google searches for LinkedIn profiles related to those companies and predefined roles (e.g., CTO, Founder).
   - Export the results to an Excel file named `linkedin_profiles_trial.xlsx`.

---

## Output Data

The script generates an Excel file (`linkedin_profiles_trial.xlsx`) with the following columns:
- **Profile Name**: The name of the LinkedIn profile.
- **Company Name**: The name of the company.
- **Role**: The specific role (e.g., CTO, Founder).
- **LinkedIn URL**: A hyperlink to the LinkedIn profile.

---

## Customization

You can customize the roles being searched by editing the `search_terms` list in the script:
```python
search_terms = [
    "CTO",
    "Co-Founder",
    "Founder",
    "CMO",
    "CFO",
    "COO"
]
```
Add or remove roles as needed.

---

## Notes

- The script uses the `googlesearch` library to perform searches and fetch URLs.
- Ensure you have a stable internet connection while running the script.
- Be mindful of Google’s usage policies to avoid being temporarily blocked due to excessive requests.

---

## Known Issues

- **Google Search Limitations**: The script fetches only the top 3 results for each query. This can be adjusted by modifying the `num_results` parameter in the `search()` function.
- **Rate Limiting**: Google may block frequent queries. If this happens, increase the `time.sleep()` interval to slow down the search process.

---

## License

This project is licensed under the MIT License. Feel free to modify and distribute as needed.

---

## Acknowledgments

This script uses the following libraries:
- [googlesearch-python](https://pypi.org/project/googlesearch-python/)
- [pandas](https://pandas.pydata.org/)
- [openpyxl](https://openpyxl.readthedocs.io/)

Thank you for using this script!

