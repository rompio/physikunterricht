import pandas as pd
import matplotlib.pyplot as plt
import pyreadstat

# === 1. Daten laden ===
df, meta = pyreadstat.read_sav("Datensatz_Roman.sav")

# === 2. Spalten definieren & umbenennen ===
themen_raw = [
    'Diff_Licht', 'Diff_Töne', 'Diff_Bewegung', 'Diff_Wärme',
    'Diff_Elektrizität', 'Diff_Elektronik', 'Diff_dieWelt',
    'Diff_Radioaktivität', 'Diff_Astrophysik',
    'Diff_Nachrichtentechnik', 'Diff_Computer', 'Diff_Fliegen'
]
themen_kurz = [t.replace("Diff_", "") for t in themen_raw]
umbenennung = dict(zip(themen_raw, themen_kurz))
df = df.rename(columns=umbenennung)

# === 3. Geschlecht umbenennen ===
df["Geschlecht"] = df["Geschlecht"].map({1: "♂", 2: "♀"})

# === 4. Mittelwerte je Thema und Geschlecht ===
means = df.groupby("Geschlecht")[themen_kurz].mean().T
# Reihenfolge der Themen fixieren
means = means.loc[themen_kurz]

# === 5. Plot erstellen ===
fig, ax = plt.subplots(figsize=(8, 6))
ax.set_xlim(-4.5, 4.5)
ax.set_ylim(-1, len(themen_kurz))
ax.set_xticks(range(-4, 5))
ax.set_yticks(range(len(themen_kurz)))
ax.set_yticklabels(themen_kurz)
ax.axvline(0, color="black", lw=1)  # Mittelachse

# Linien zeichnen
for i, thema in enumerate(themen_kurz):
    x_female = means.loc[thema, "♀"]
    x_male = means.loc[thema, "♂"]
    ax.plot([0, -x_female], [i, i], color="magenta", marker="o", label="♀" if i == 0 else "")
    ax.plot([0, x_male], [i, i], color="blue", marker="o", label="♂" if i == 0 else "")

# Kasten (optional)
ax.plot([-4, 4], [-0.5, -0.5], color="gray")
ax.plot([-4, 4], [len(themen_kurz)-0.5, len(themen_kurz)-0.5], color="gray")
ax.plot([-4, -4], [-0.5, len(themen_kurz)-0.5], color="gray")
ax.plot([4, 4], [-0.5, len(themen_kurz)-0.5], color="gray")

ax.set_title("Mittelwerte der Themenbewertung nach Geschlecht")
ax.set_xlabel("Bewertungsskala")
ax.legend(loc="upper center", ncol=2)
plt.tight_layout()
plt.show()
