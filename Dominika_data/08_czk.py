import openmeteo_requests
import pandas as pd

# Súradnice pre Česko – Praha
latitude = 50.0755
longitude = 14.4378

url = "https://archive-api.open-meteo.com/v1/archive"
params = {
    "latitude": [latitude],
    "longitude": [longitude],
    "start_date": "1975-01-01",
    "end_date": "2025-11-14",  # max. dnešný dátum podľa obmedzenia API
    "hourly": "temperature_2m"
}

client = openmeteo_requests.Client()
response = client.weather_api(url, params=params)
data = response[0]

hourly_data = data.Hourly()
df = pd.DataFrame({
    "date": pd.to_datetime(hourly_data.Time()),
    "temp": hourly_data.Variables(0).ValuesAsNumpy()
})

df.to_csv("cesko.csv", index=False)
print("Export hotový: cesko.csv")