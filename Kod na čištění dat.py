import pandas as pd
from pathlib import Path

# --- UPRAV TUTO CESTU NA SVŮJ SOUBOR ---
src = r"C:\Users\veron\Desktop\open-meteo-Ivancice1\open-meteo-Ivancice.csv"
# ---------------------------------------

src_path = Path(src)

# 1) Načteme jako TEXT, přeskočíme 3 řádky (metadata), ať nejsou DtypeWarning
df = pd.read_csv(
    src,
    skiprows=3,           # přeskočí metadata + prázdný řádek
    dtype=str,            # všechno jako text, ať si to pohlídáme sami
    encoding="utf-8-sig"  # vezme BOM, kdyby tam byl
)

# 2) Normalizace názvů sloupců (z tvého CSV očekáváme 4 sloupce)
#    Ale necháme to tolerantní (odstraníme mezery, závorky a jednotky)
def norm(c):
    c = c.strip().lower()
    c = c.replace(" (°c)", "_c").replace(" (mm)", "_mm").replace(" (cm)", "_cm")
    c = c.replace("°", "").replace(" ", "_").replace("(", "").replace(")", "")
    return c

df.columns = [norm(c) for c in df.columns]

# 3) NĚKTERÁ CSV MÍVAJÍ HLAVIČKU OPAKOVANĚ UPROSTŘED SOUBORU.
#    Vyhoď všechny řádky, kde je ve sloupci 'time' text 'time'
if "time" in df.columns:
    before = len(df)
    df = df[df["time"].str.lower() != "time"]
    removed = before - len(df)
    print(f"Odstraněno duplicitních hlaviček: {removed}")
else:
    raise RuntimeError("V souboru chybí sloupec 'time' – zkontroluj skiprows/oddělovač.")

# 4) Převod typů
#    time: ISO 8601 → datetime (povolíme různé ISO varianty)
df["time"] = pd.to_datetime(df["time"], errors="coerce", format="ISO8601")

#    čísla: nejdřív sjednotíme desetinný oddělovač na tečku, pak na numeric
for c in ["temperature_2m_c", "rain_mm", "snowfall_cm"]:
    if c in df.columns:
        df[c] = (
            df[c]
            .fillna("")                       # None → ""
            .str.strip()
            .str.replace(",", ".", regex=False)  # čárku na tečku
        )
        df[c] = pd.to_numeric(df[c], errors="coerce")

# 5) Vyhoď zjevně prázdné řádky (kde není čas)
df = df[~df["time"].isna()].copy()

# 6) Ulož dvě verze
out_base = src_path.with_name(src_path.stem + "_clean")
dot_csv = out_base.with_suffix(".csv")                     # ',' + '.'
eu_csv  = src_path.with_name(src_path.stem + "_semicolon.csv")  # ';' + ','

df.to_csv(dot_csv, index=False)
df.to_csv(eu_csv, index=False, sep=";", decimal=",")

print("Hotovo:")
print(" -", dot_csv)
print(" -", eu_csv)