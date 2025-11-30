
import pandas as pd
import glob

# Pranostika
print("Pranostika: Keď sa Dominik potí, Marek je v kožuchu.")

# Mapovanie poradia na kraj (uprav presne podľa tvojich dát)
mapa_krajov = {1: "BA", 2: "BB", 3: "NR", 4: "TT", 5: "PO", 6: "KE", 7: "TN", 8: "ZA"}

csv_files = sorted(glob.glob("pocasie_*.csv"))  # zoradenie podľa názvu
dataframes = [pd.read_csv(file) for file in csv_files]

start_mmdd = "04-25"
end_mmdd = "08-04"

results = []
for idx, df in enumerate(dataframes):
    kraj = mapa_krajov[idx+1]
    df['date'] = pd.to_datetime(df['date'])
    mask = df['date'].apply(lambda d: start_mmdd <= d.strftime("%m-%d") <= end_mmdd)
    filtered = df.loc[mask]
    max_row = filtered.loc[filtered['temperature_2m'].idxmax()]
    min_row = filtered.loc[filtered['temperature_2m'].idxmin()]
    results.append({
        "kraj": kraj,
        "max_temp": max_row['temperature_2m'],
        "max_date": max_row['date'],
        "min_temp": min_row['temperature_2m'],
        "min_date": min_row['date']
    })

for r in results:
    print(f"{r['kraj']}:")
    print(f"  Najvyššia teplota (25.4. - 4.8.): {r['max_temp']:.2f} °C {r['max_date'].strftime('%Y-%m-%d')}")
    print(f"  Najnižšia teplota (25.4. - 4.8.): {r['min_temp']:.2f} °C {r['min_date'].strftime('%Y-%m-%d')}")
    print("-"*40)