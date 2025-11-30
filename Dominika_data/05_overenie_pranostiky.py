import pandas as pd
import glob

print('Pranostika: Keď sa Dominik potí, Marek je v kožuchu.')

mapa_krajov = {1: "BA", 2: "BB", 3: "NR", 4: "TT", 5: "PO", 6: "KE", 7: "TN", 8: "ZA"}
csv_files = sorted(glob.glob("pocasie_*.csv"))
dataframes = [pd.read_csv(file) for file in csv_files]

for idx, df in enumerate(dataframes):
    kraj = mapa_krajov[idx+1]
    df['date'] = pd.to_datetime(df['date'])
    df['year'] = df['date'].dt.year
    vysledky = []
    roky = df['year'].unique()
    for rok in roky:
        dominik = df[(df['date'] == pd.Timestamp(f"{rok}-08-04"))]
        marek = df[(df['date'] == pd.Timestamp(f"{rok}-04-25"))]
        if not dominik.empty and not marek.empty:
            d_temp = dominik['temperature_2m'].values[0]
            m_temp = marek['temperature_2m'].values[0]
            platnost = d_temp > m_temp
            vysledky.append(platnost)
    if vysledky and all(vysledky):
        pranostika = True
    else:
        pranostika = False
    print(f"{kraj}: Pranostika platí: {pranostika}")