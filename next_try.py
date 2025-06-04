import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pyreadstat

# Daten laden
df, meta = pyreadstat.read_sav("Datensatz_Roman.sav")

# Themen vereinfachen
themen_raw = [
    'Diff_Licht', 'Diff_Töne', 'Diff_Bewegung', 'Diff_Wärme',
    'Diff_Elektrizität', 'Diff_Elektronik', 'Diff_dieWelt',
    'Diff_Radioaktivität', 'Diff_Astrophysik',
    'Diff_Nachrichtentechnik', 'Diff_Computer', 'Diff_Fliegen'
]
themen_kurz = [t.replace("Diff_", "") for t in themen_raw]
df = df.rename(columns=dict(zip(themen_raw, themen_kurz)))
df["Geschlecht"] = df["Geschlecht"].map({1: "♂", 2: "♀"})

# Mittelwerte pro Thema und Geschlecht
means = df.groupby("Geschlecht")[themen_kurz].mean()

# Winkel berechnen (12 Themen → 360° / 12 = 30° Schritte)
num_vars = len(themen_kurz)
angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
angles += angles[:1]  # Kreis schließen

# Werte vorbereiten
values_female = means.loc["♀"].tolist()
values_male = means.loc["♂"].tolist()
values_female += values_female[:1]
values_male += values_male[:1]

# Plot
fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))

# Achsen einrichten
ax.set_theta_offset(np.pi / 2)
ax.set_theta_direction(-1)

# Themen als Achsentitel
ax.set_thetagrids(np.degrees(angles[:-1]), themen_kurz)

# Skala
ax.set_ylim(0, 4)
ax.set_yticks(range(0, 5))
ax.set_yticklabels([str(i) for i in range(0, 5)])

# Linien zeichnen
ax.plot(angles, values_female, color="magenta", linewidth=2, label="♀ Mädchen")
ax.fill(angles, values_female, color="magenta", alpha=0.25)

ax.plot(angles, values_male, color="blue", linewidth=2, label="♂ Jungen")
ax.fill(angles, values_male, color="blue", alpha=0.25)

# Titel und Legende
plt.title("Themenbewertung nach Geschlecht (0 = keine Zustimmung, 4 = volle Zustimmung)", y=1.08)
ax.legend(loc='upper right', bbox_to_anchor=(1.1, 1.1))

plt.tight_layout()
plt.show()
