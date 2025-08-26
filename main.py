import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime

# Major Indian cities
cities = ["delhi", "mumbai", "chennai", "kolkata", "bangalore", "hyderabad"]

base_url = "https://www.timeanddate.com/weather/india/"

data = []

for city in cities:
    url = base_url + city
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    try:
        # Date (today)
        today_date = datetime.now().strftime("%Y-%m-%d")

        # Temperature
        temp = soup.find("div", class_="h2").text.strip()

        # Weather condition
        condition = soup.find("p").text.strip()

        # Default Rain Forecast
        rain_forecast = "N/A"

        # Find rain/precipitation details in table
        table = soup.find("table", class_="table table--left table--inner-borders-rows")
        if table:
            rows = table.find_all("tr")
            for row in rows:
                cells = row.find_all("td")
                if len(cells) == 2:
                    label = cells[0].text.strip()
                    value = cells[1].text.strip()
                    if "Precipitation" in label or "Rain" in label:
                        rain_forecast = value
                        break

        # Append data
        data.append({
            "Date": today_date,
            "City": city.capitalize(),
            "Temperature": temp,
            "Condition": condition,
            "Rain Forecast": rain_forecast
        })

    except Exception as e:
        print(f"⚠️ Could not fetch {city}: {e}")

# Convert to DataFrame
df = pd.DataFrame(data)

# Save to CSV file
df.to_csv("indian_cities_weather.csv", index=False)

print("\n✅ Final Weather Report saved in 'indian_cities_weather.csv'")
print(df)
