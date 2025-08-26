import requests
from bs4 import BeautifulSoup
import pandas as pd

base_url = "http://books.toscrape.com/catalogue/page-{}.html"

books_data = []

# Loop through first 3 pages (you can increase to all 50)
for page in range(1, 4):
    url = base_url.format(page)
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    books = soup.find_all("article", class_="product_pod")

    for book in books:
        # Title
        title = book.h3.a["title"]

        # Price
        price = book.find("p", class_="price_color").text.strip()

        # Star rating (class attribute has e.g. 'star-rating Three')
        rating_class = book.find("p")["class"]
        rating = rating_class[1] if len(rating_class) > 1 else "N/A"

        # Availability
        availability = book.find("p", class_="instock availability").text.strip()

        books_data.append({
            "Title": title,
            "Price": price,
            "Rating": rating,
            "Availability": availability
        })

# Save dataset
df = pd.DataFrame(books_data)
df.to_csv("books_scraped.csv", index=False)

print("✅ Data saved to books_scraped.csv")
print(df.head())

# -----------------------
# 🎯 Filtering
# -----------------------
print("\n--- Filter Options ---")
print("1. Filter by Rating")
print("2. Filter by Availability")

choice = input("Enter choice (1/2): ")

filtered_df = df.copy()

if choice == "1":
    rating_choice = input("Enter rating (One/Two/Three/Four/Five): ")
    filtered_df = df[df["Rating"].str.lower() == rating_choice.lower()]

elif choice == "2":
    filtered_df = df[df["Availability"].str.contains("In stock")]

else:
    print("⚠️ Invalid choice, showing all books.")

filtered_df.to_csv("books_filtered.csv", index=False)
print("\n✅ Filtered results saved to books_filtered.csv")
print(filtered_df.head())
