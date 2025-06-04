import pandas as pd
import pyreadstat
import matplotlib.pyplot as plt

# === Daten laden ===
df, meta = pyreadstat.read_sav("Datensatz_Roman.sav")

# Spalten umbenennen
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

# Mittelwerte berechnen
means = df.groupby("Geschlecht")[themen_kurz].mean()

# === Plot vorbereiten ===
plt.figure(figsize=(8, 6))

for thema in themen_kurz:
    plt.plot(
        [means.loc["♀", thema], means.loc["♂", thema]],
        [thema, thema],
        marker="o", color="black"
    )

plt.axvline(0, color="gray", linestyle="--")
plt.xlim(-4.5, 4.5)
plt.xlabel("Bewertung")
plt.title("Wahrnehmung der Themenrepräsentation im Physikunterricht")
plt.grid(axis="x", linestyle=":")
plt.tight_layout()
plt.show()
