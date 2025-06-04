import pandas as pd
import pyreadstat
import matplotlib.pyplot as plt
from pandas.plotting import parallel_coordinates

# === 1. Daten laden ===
df, meta = pyreadstat.read_sav("Datensatz_Roman.sav")

# === 2. Umbenennung & Mapping ===
themen_raw = [
    'Diff_Licht', 'Diff_Töne', 'Diff_Bewegung', 'Diff_Wärme',
    'Diff_Elektrizität', 'Diff_Elektronik', 'Diff_dieWelt',
    'Diff_Radioaktivität', 'Diff_Astrophysik',
    'Diff_Nachrichtentechnik', 'Diff_Computer', 'Diff_Fliegen'
]

themen_kurz = [t.replace("Diff_", "") for t in themen_raw]
umbenennung = dict(zip(themen_raw, themen_kurz))
df = df.rename(columns=umbenennung)

geschlecht_map = {1: "♂", 2: "♀"}
df["Geschlecht"] = df["Geschlecht"].map(geschlecht_map)

# === 3. Parallel Coordinates Plot vorbereiten ===
# Achtung: max. 500 Zeilen sinnvoll für Lesbarkeit
df_plot = df[["Geschlecht"] + themen_kurz].dropna().copy()
df_plot = df_plot.sample(n=min(200, len(df_plot)), random_state=1)  # ggf. sample für Übersichtlichkeit

# === 4. Plot ===
plt.figure(figsize=(14, 6))
parallel_coordinates(df_plot, class_column="Geschlecht", colormap="coolwarm", alpha=0.4)
plt.title("Parallel Coordinates Plot: Themenbewertung je Person")
plt.ylabel("Bewertung (-4 bis +4)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
