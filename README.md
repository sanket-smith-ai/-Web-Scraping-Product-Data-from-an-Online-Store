## Web Scraping Product Data from an Online Store (Books to Scrape)

## Project Overview

This project is a Python-based web scraping assignment that extracts product data from the public website
[https://books.toscrape.com/](https://books.toscrape.com/).

The scraper collects details about books — including their **Title**, **Price**, and **Availability** from multiple pages and stores them into a structured CSV file named `books.csv`.

## Files Included

| File Name          | Description                                         |
| ------------------ | --------------------------------------------------- |
| `scrape_books.py`  | Main Python script for scraping data.               |
| `books.csv`        | Output file containing scraped book data.           |
| `requirements.txt` | Contains Python libraries with specific versions.   |
| `README.md`        | Documentation explaining setup and project details. |


## System & Library Requirements

* **Python Version:** 3.8 or higher
* **Libraries Used:**

  * `requests`
  * `beautifulsoup4`

 **requirements.txt**

```
requests==2.32.3
beautifulsoup4==4.12.3
```

## Environment Setup

Since the Python environment is **already created**, just **activate it** and **install dependencies**.

### Step 1️⃣: Activate Virtual Environment

**Windows:**

```bash
scraper\Scripts\activate
```

**macOS/Linux:**

```bash
source scraper/bin/activate
```

### Step 2️⃣: Install Required Libraries

```bash
pip install -r requirements.txt
```

 **requirements.txt**

```
requests==2.32.3
beautifulsoup4==4.12.3
```

##  How to Run the Script

Run the scraper using:

```bash
python app.py
```

### What It Does

1. Scrapes book data from the **first 3 pages** of the website.
2. Extracts the following fields:

   * **Title** – Book name
   * **Price** – Price in £
   * **Availability** – Stock status 
3. Saves the data into `books.csv`.
4. If re-run, it appends only new unique entries (no duplicates).

## Sample Output (books.csv)

| Title                | Price  | Availability |
| -------------------- | ------ | ------------ |
| A Light in the Attic | £51.77 | In stock     |
| Tipping the Velvet   | £53.74 | In stock     |
| Soumission           | £50.10 | In stock     |
| Sharp Objects        | £47.82 | In stock     |


## Important Notes

* Do **not** keep `books.csv` open in Excel while running the script — it locks the file.
* The script adds a short delay (`time.sleep(1)`) between requests for polite scraping.
* Uses only allowed libraries — no Selenium, APIs, or browser automation.
* You can scrape more pages by changing the value of `pages_to_scrape` inside the script.

##  Author Information

**Name:** Sanket Hiwarkhede
**Task Title:** Web Scraping Product Data from an Online Store
**Language Used:** Python 3
**Libraries Used:** requests, BeautifulSoup, csv
**Website Scraped:** [https://books.toscrape.com/](https://books.toscrape.com/)

