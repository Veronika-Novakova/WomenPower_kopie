import pandas as pd
import glob

# Načítať všetky CSV pre kraje
csv_files = glob.glob("pocasie_*.csv")
dataframes = [pd.read_csv(file) for file in csv_files]

# Príkladový výstup: priemerná hodnota teploty pre každý kraj
for idx, df in enumerate(dataframes):
    print(f"Kraj {idx+1}")
    print(df.head())  # Prvých 10 riadkov na ukážku
    print(f"Priemerná teplota: {df['temperature_2m'].mean():.2f} °C")
    print('-' * 30)