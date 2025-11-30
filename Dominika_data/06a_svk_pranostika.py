# import openmeteo_requests
# import pandas as pd

# client = openmeteo_requests.Client()
# params = {
#     "latitude": [48.1482],
#     "longitude": [17.1067],
#     "start_date": "1975-01-01",
#     "end_date": "2025-11-14",
#     "hourly": "temperature_2m"
# }
# response = client.weather_api("https://archive-api.open-meteo.com/v1/archive", params=params)
# data = response[0]
# hourly_data = data.Hourly()
# df = pd.DataFrame({
#     "time": pd.to_datetime(hourly_data.Time()),
#     "temp": hourly_data.Variables(0).ValuesAsNumpy()
# })
# df.to_csv("slovensko.csv", index=False)

# import pandas as pd
# df = pd.read_csv("slovensko.csv")
# print(df.columns)
# print(df.head(20))

import pandas as pd

df = pd.read_csv("slovensko.csv")
df['time'] = pd.to_datetime(df['time'])
df['year'] = df['time'].dt.year

marek_temps = []
dominik_temps = []
results = []

for year in df['year'].unique():
    marek = df[df['time'].dt.strftime('%Y-%m-%d') == f"{year}-04-25"]
    dominik = df[df['time'].dt.strftime('%Y-%m-%d') == f"{year}-08-04"]
    if not marek.empty and not dominik.empty:
        m_temp = marek['temp'].values[0]
        d_temp = dominik['temp'].values[0]
        results.append({
            "year": year,
            "marek": m_temp,
            "dominik": d_temp,
            "pranostika": d_temp > m_temp
        })
        marek_temps.append(m_temp)
        dominik_temps.append(d_temp)

if marek_temps and dominik_temps:
    avg_marek = sum(marek_temps)/len(marek_temps)
    avg_dominik = sum(dominik_temps)/len(dominik_temps)
else:
    avg_marek = avg_dominik = None

df_out = pd.DataFrame(results)
mean_row = pd.DataFrame([{
    "year": "Priemer",
    "marek": avg_marek,
    "dominik": avg_dominik,
    "pranostika": ""
}])
df_out = pd.concat([df_out, mean_row], ignore_index=True)

df_out.to_csv("slovensko_pranostika.csv", index=False)
print(df_out)

