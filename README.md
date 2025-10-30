##  Web Scraping Product Data from an Online Store (Books to Scrape)

---

## Project Overview

This project is a **Python-based web scraping assignment** that extracts product data from the public website
[https://books.toscrape.com/](https://books.toscrape.com/).

The scraper collects details about books including their **Title**, **Price**, and **Availability** from multiple pages and stores them into a structured CSV file named **`books.csv`**.
---

## System & Library Requirements

* **Python Version:** 3.8 or higher
* **Libraries Used:**

  * `requests`
  * `beautifulsoup4`

📄 **requirements.txt**

```
requests==2.32.3
beautifulsoup4==4.12.3
```

---

## Environment Setup
### Step 1: Create and Activate Virtual Environment

**Windows:**

```bash
python -m venv scraper
scraper\Scripts\activate
```

**macOS/Linux:**

```bash
python3 -m venv scraper
source scraper/bin/activate
```

### Step 2: Install Required Libraries

```bash
pip install -r requirements.txt
```

---

## How to Run the Script

Run the scraper using:

```bash
python app.py
```

### What It Does

* Scrapes book data from the **first 3 pages** of the website.
* Extracts the following fields:

  * **Title** – Book name
  * **Price** – Price in £
  * **Availability** – Stock status
* Saves the data into `books.csv`.
* If re-run, it **appends only new unique entries** (no duplicates).

---

## Sample Output (books.csv)

| Title                | Price  | Availability |
| -------------------- | ------ | ------------ |
| A Light in the Attic | £51.77 | In stock     |
| Tipping the Velvet   | £53.74 | In stock     |
| Soumission           | £50.10 | In stock     |
| Sharp Objects        | £47.82 | In stock     |

---

## Important Notes

* Do **not** keep `books.csv` open in Excel while running the script — it locks the file.
* The script adds a short delay (`time.sleep(1)`) between requests to ensure **polite scraping**.
* Uses only **allowed libraries** — no Selenium, APIs, or browser automation.
* You can scrape more pages by updating the variable **`pages_to_scrape`** inside the script.

---

## Author Information

**Name:** Sanket Hiwarkhede
**Task Title:** Web Scraping Product Data from an Online Store
**Language Used:** Python 3
**Libraries Used:** requests, BeautifulSoup, csv
**Website Scraped:** [https://books.toscrape.com/](https://books.toscrape.com/)

---

Would you like me to add a **short “Approach & Assumptions” section** (2–3 lines) at the end to strengthen your README for the recruiter?
