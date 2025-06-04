import pandas as pd
import pyreadstat

# === 1. .sav-Datei einlesen ===
sav_datei = "Datensatz_Roman.sav"
df, meta = pyreadstat.read_sav(sav_datei)

# === 2. Optional: Spalten umbenennen ===
themen_raw = [
    'Diff_Licht', 'Diff_Töne', 'Diff_Bewegung', 'Diff_Wärme',
    'Diff_Elektrizität', 'Diff_Elektronik', 'Diff_dieWelt',
    'Diff_Radioaktivität', 'Diff_Astrophysik',
    'Diff_Nachrichtentechnik', 'Diff_Computer', 'Diff_Fliegen'
]
themen_kurz = [t.replace("Diff_", "") for t in themen_raw]
umbenennung = dict(zip(themen_raw, themen_kurz))
df = df.rename(columns=umbenennung)

# === 3. Dateien exportieren ===
# Als Excel-Datei
df.to_excel("Datensatz_Roman.xlsx", index=False)

# Als CSV-Datei
df.to_csv("Datensatz_Roman.csv", index=False, sep=";")  # deutsches Excel nutzt oft `;` als Trenner

print("Export abgeschlossen: .xlsx und .csv erstellt.")
