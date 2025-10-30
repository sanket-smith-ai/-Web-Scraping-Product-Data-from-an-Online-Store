import requests
from bs4 import BeautifulSoup
import csv, os
import time

BASE_URL = "https://books.toscrape.com/catalogue/page-{}.html"

def fetch_page(url):
    """Fetch HTML content of a given URL with correct encoding."""
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        response.encoding = 'utf-8'
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"Failed to fetch {url}: {e}")
        return None

def parse_books(html):
    """Parse book details from a single page."""
    soup = BeautifulSoup(html, 'html.parser')
    books = []

    for article in soup.find_all('article', class_='product_pod'):
        title = article.h3.a['title'].strip()
        price = article.find('p', class_='price_color').text.strip()
        availability = article.find('p', class_='instock availability').text.strip()
        books.append([title, price, availability])
    
    return books

def save_to_csv(data, filename="books.csv"):
    """Append new book data to CSV without overwriting or duplicating existing records."""
    file_exists = os.path.isfile(filename)
    existing_titles = set()

    if file_exists:
        with open(filename, mode='r', encoding='utf-8', newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                existing_titles.add(row['Title'])

    new_data = [row for row in data if row[0] not in existing_titles]

    if not new_data:
        print("⚠️ No new unique records found. Skipping write.")
        return


    with open(filename, mode='a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(["Title", "Price", "Availability"])
        writer.writerows(new_data)

    print(f"✅ Added {len(new_data)} unique new records to '{filename}'.")


def main():
    all_books = []
    pages_to_scrape = 3  # scrape first 3 pages

    for page_num in range(1, pages_to_scrape + 1):
        url = BASE_URL.format(page_num)
        print(f"Scraping page {page_num}: {url}")

        html = fetch_page(url)
        if not html:
            continue

        books = parse_books(html)
        all_books.extend(books)
        time.sleep(1) 

    save_to_csv(all_books)
    print(f"\n✅ Scraping complete! {len(all_books)} books saved to 'books.csv'.")

if __name__ == "__main__":
    main()

