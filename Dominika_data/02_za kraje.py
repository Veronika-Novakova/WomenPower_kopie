import pandas as pd
import glob

# Načítať všetky CSV
csv_files = glob.glob("pocasie_*.csv")
dataframes = [pd.read_csv(file) for file in csv_files]

# Over rozpätie rokov v dátach
for idx, df in enumerate(dataframes):
    print(f"Kraj {idx+1}")
    print(f"Rozsah dátumov: {df['date'].min()} - {df['date'].max()}")
    df['year'] = pd.to_datetime(df['date']).dt.year
    print(f"Pokryté roky: {df['year'].min()} - {df['year'].max()}")
    print('-'*30)

# Príklad: spriemerovanie za celé obdobie
for idx, df in enumerate(dataframes):
    avg_temp = df['temperature_2m'].mean()
    print(f"Priemerná teplota za 50 rokov v kraji {idx+1}: {avg_temp:.2f}")