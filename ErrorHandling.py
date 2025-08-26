import requests
from bs4 import BeautifulSoup
import pandas as pd

base_url = "http://books.toscrape.com/catalogue/page-{}.html"
books = []

def fetch_books(page):
    """
    Fetch books from one page with error handling
    """
    try:
        url = base_url.format(page)
        response = requests.get(url, timeout=10)
        response.raise_for_status()
    except requests.exceptions.Timeout:
        print(f"⏳ Timeout while fetching page {page}")
        return []
    except requests.exceptions.RequestException as e:
        print(f"⚠️ Network error on page {page}: {e}")
        return []

    try:
        soup = BeautifulSoup(response.text, "html.parser")
        items = soup.find_all("article", class_="product_pod")
        page_books = []

        for item in items:
            title = item.h3.a["title"]
            price = item.find("p", class_="price_color").text.strip()
            rating = item.p["class"][1]  # e.g., "Three", "Five"
            availability = item.find("p", class_="instock availability").text.strip()

            page_books.append({
                "Title": title,
                "Price": price,
                "Rating": rating,
                "Availability": availability
            })

        return page_books

    except Exception as e:
        print(f"⚠️ Parsing error on page {page}: {e}")
        return []


# Collect from first 3 pages
for page in range(1, 4):
    print(f"🔎 Fetching page {page}...")
    books.extend(fetch_books(page))

# Save results
try:
    df = pd.DataFrame(books)
    df.to_csv("books_with_error_handling.csv", index=False)
    print("✅ Books data saved to books_with_error_handling.csv")
    print(df.head(10))  # show first 10 books
except Exception as e:
    print(f"⚠️ Error saving file: {e}")
