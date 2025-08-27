## Python-Project-Submission

## Requirements

- Python 3.7+
- Libraries:
  - `requests`
  - `beautifulsoup4`
  - `pandas`

Install dependencies using pip:

```bash
pip install requests beautifulsoup4 pandas
```
---

# WeatherReport.py
# Indian Cities Weather Scraper 🌤️ 

A Python script to fetch current weather data for major Indian cities and save it in a CSV file. The data includes temperature, weather condition, and rain/precipitation forecast.

---

## Features

- Scrapes weather information from [Time and Date](https://www.timeanddate.com/weather/india/) website.
- Supports multiple major Indian cities: Delhi, Mumbai, Chennai, Kolkata, Bangalore, and Hyderabad.
- Extracts:
  - Current temperature
  - Weather condition (e.g., Clear, Cloudy)
  - Rain/Precipitation forecast
- Saves data into a CSV file (`indian_cities_weather.csv`) for easy use in data analysis.

---

# BooksData.py
# Book Data Scraper

This Python project scrapes book information from [Books to Scrape](http://books.toscrape.com/) and saves it into a CSV file for analysis or further use.

---

## Features

- Scrapes multiple pages from the website (first 5 pages by default).
- Collects the following data for each book:
  - **Title**
  - **Price**
  - **Availability**
  - **Rating** (Star rating as a popularity proxy)
  - **Category** (currently set as "General", can be extended)
- Saves the scraped data in a CSV file (`books_data.csv`).

---

# UserInteraction.py
# 📚 Books Scraper & Filter

A Python script to **scrape book data** from [Books to Scrape](http://books.toscrape.com/) and **filter** it by rating or availability. The scraped data is saved in CSV files for easy analysis.

---

## **Features**

- Scrapes the first 3 pages (can be extended to all pages) of book data.
- Extracts the following details for each book:
  - Title
  - Price
  - Star Rating (as a popularity proxy)
  - Availability
- Allows user to filter the dataset:
  - By Rating (One, Two, Three, Four, Five)
  - By Availability (In stock)
- Saves full and filtered datasets to CSV files.

---

# ErrorHandling.py
# 📚 Books Scraper with Error Handling

A Python script to **scrape book data** from [Books to Scrape](http://books.toscrape.com/) with robust **error handling**. The script collects book details and saves them to a CSV file, while gracefully handling network and parsing errors.

---

## **Features**

- Scrapes the first 3 pages (configurable) of book data.
- Extracts the following details for each book:
  - **Title**
  - **Price**
  - **Star Rating** (as a popularity proxy)
  - **Availability**
- Robust error handling:
  - Handles network errors (timeouts, connection errors)
  - Handles parsing errors
  - Ensures program continues to run even if a page fails
- Saves the scraped data to a CSV file.
- Displays the first 10 books for quick verification.

---

