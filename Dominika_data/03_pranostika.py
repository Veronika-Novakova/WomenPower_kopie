import pandas as pd
import glob

# Pranostika
print("Pranostika: Keď sa Dominik potí, Marek je v kožuchu.")

# Načítať všetky CSV krajov
csv_files = glob.glob("pocasie_*.csv")
dataframes = [pd.read_csv(file) for file in csv_files]

# Nastav rozmedzie dátumov pre výpočet (slovenský zápis: od 25. apríla do 4. augusta, každý rok)
start_mmdd = "04-25"
end_mmdd = "08-04"

results = []
for idx, df in enumerate(dataframes):
    df['date'] = pd.to_datetime(df['date'])
    # filtrovanie na každý rok len medzi zadanými mesiacmi/dňami
    mask = df['date'].apply(lambda d: start_mmdd <= d.strftime("%m-%d") <= end_mmdd)
    filtered = df.loc[mask]
    # Najvyššia teplota
    max_row = filtered.loc[filtered['temperature_2m'].idxmax()]
    # Najnižšia teplota
    min_row = filtered.loc[filtered['temperature_2m'].idxmin()]
    results.append({
        "kraj": f"Kraj {idx+1}",
        "max_temp": max_row['temperature_2m'],
        "max_date": max_row['date'],
        "min_temp": min_row['temperature_2m'],
        "min_date": min_row['date']
    })

# Výpis výsledkov
for r in results:
    print(f"{r['kraj']}:")
    print(f"  Najvyššia teplota v období (25.4. - 4.8.): {r['max_temp']:.2f} °C dňa {r['max_date'].strftime('%Y-%m-%d')}")
    print(f"  Najnižšia teplota v období (25.4. - 4.8.): {r['min_temp']:.2f} °C dňa {r['min_date'].strftime('%Y-%m-%d')}")
    print("-"*40)