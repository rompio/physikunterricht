import pandas as pd
import pyreadstat
import matplotlib.pyplot as plt

# === 1. Daten laden & vorbereiten ===
df, meta = pyreadstat.read_sav("Datensatz_Roman.sav")

# Relevante Spalten
themen_raw = [
    'Diff_Licht', 'Diff_Töne', 'Diff_Bewegung', 'Diff_Wärme',
    'Diff_Elektrizität', 'Diff_Elektronik', 'Diff_dieWelt',
    'Diff_Radioaktivität', 'Diff_Astrophysik',
    'Diff_Nachrichtentechnik', 'Diff_Computer', 'Diff_Fliegen'
]

themen_kurz = [t.replace("Diff_", "") for t in themen_raw]
umbenennung = dict(zip(themen_raw, themen_kurz))
df = df.rename(columns=umbenennung)

# Geschlecht umwandeln
geschlecht_map = {1: "♂", 2: "♀"}
df["Geschlecht"] = df["Geschlecht"].map(geschlecht_map)

# === 2. Mittelwerte berechnen ===
mittelwerte = df.groupby("Geschlecht")[themen_kurz].mean().T  # Transponieren: Themen als Zeilen

# Plotdaten vorbereiten
mittelwerte["♀"] *= -1  # damit weibliche Balken nach links zeigen

# === 3. Plot ===
plt.figure(figsize=(10, 8))
themen = mittelwerte.index

plt.barh(themen, mittelwerte["♀"], color="lightcoral", label="♀ Mädchen")
plt.barh(themen, mittelwerte["♂"], color="cornflowerblue", label="♂ Jungen")

plt.axvline(0, color="gray")
plt.xlabel("Durchschnittliche Bewertung")
plt.title("Wahrgenommene Repräsentation nach Thema und Geschlecht")
plt.legend(loc="lower right")
plt.tight_layout()
plt.show()
