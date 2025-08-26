import requests
from bs4 import BeautifulSoup
import pandas as pd

base_url = "http://books.toscrape.com/catalogue/page-{}.html"

all_books = []

# Scrape first 5 pages (you can increase this)
for page in range(1, 6):
    url = base_url.format(page)
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    # Each book is inside 'article.product_pod'
    books = soup.find_all("article", class_="product_pod")

    for book in books:
        title = book.h3.a["title"]

        # Price
        price = book.find("p", class_="price_color").text

        # Availability
        availability = book.find("p", class_="instock availability").text.strip()

        # Star rating (popularity proxy)
        rating = book.p["class"][1]  # e.g. "One", "Two", "Five"

        # Category (genre) - not directly here, needs parent page scraping
        # For now, assign "General" (or scrape category separately if needed)
        category = "General"

        all_books.append({
            "Title": title,
            "Price": price,
            "Availability": availability,
            "Rating": rating,
            "Category": category
        })

# Convert to DataFrame
df = pd.DataFrame(all_books)

# Save to CSV
df.to_csv("books_data.csv", index=False)

print("✅ Scraping completed. Data saved in books_data.csv")
print(df.head())
