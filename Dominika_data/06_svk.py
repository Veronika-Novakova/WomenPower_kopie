import openmeteo_requests
import pandas as pd

# Nastav parametre
url = "https://archive-api.open-meteo.com/v1/archive"
params = {
    "latitude": [48.1482],  # Štatistická poloha Slovenska
    "longitude": [17.1067],
    "start_date": "1975-01-01",
    "end_date": "2025-01-01",
    "hourly": "temperature_2m"
}

# Pripojenie a získanie dát
client = openmeteo_requests.Client()
response = client.weather_api(url, params=params)

# Spracovanie dát
data = response[0]  # Predpoklad, že odpoveď je zoznam
hourly_data = data.Hourly()
df = pd.DataFrame({
    "date": pd.to_datetime(hourly_data.Time()),
    "temp": hourly_data.Variables(0).ValuesAsNumpy()
})

# Uloženie do CSV
df.to_csv("slovensko_1975_2025.csv", index=False)
print("Dáta uložené do slovensko_1975_2025.csv")



