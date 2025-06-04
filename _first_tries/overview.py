import pandas as pd
import pyreadstat

# Pfad zur .sav-Datei
df, meta = pyreadstat.read_sav("Datensatz_Roman.sav")

# Optional: Alle Spaltennamen + Labels ausgeben
print(df.columns)
print(meta.column_labels)
