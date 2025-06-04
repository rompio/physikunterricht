import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Daten vorbereiten
df = pd.read_excel("Datensatz_Roman.xlsx")
df.columns = df.columns.str.strip()
df["Geschlecht"] = df["Geschlecht"].map({1: "♂", 2: "♀"})
df.rename(columns={"dieWelt": "die Welt"}, inplace=True)

themen = ['Licht', 'Töne', 'Bewegung', 'Wärme', 'Elektrizität', 'Elektronik',
          'die Welt', 'Radioaktivität', 'Astrophysik', 'Nachrichtentechnik', 'Computer', 'Fliegen']

mittelwerte = {"♀": [], "♂": []}

for thema in themen:
    df_thema = df[[thema, "Geschlecht"]].dropna()
    mittelwerte["♀"].append(df_thema[df_thema["Geschlecht"] == "♀"][thema].mean())
    mittelwerte["♂"].append(df_thema[df_thema["Geschlecht"] == "♂"][thema].mean())

# Plot
fig, ax = plt.subplots(figsize=(11, 8))
ax.axhline(0, color="black", linewidth=1)
ax.axvline(0, color="black", linewidth=1)

# Plot-Strahlen
for i, thema in enumerate(themen):
    y_f = mittelwerte["♀"][i]
    y_m = mittelwerte["♂"][i]

    # Mädchen
    ax.plot([-1, 0], [y_f, 0], color="red", alpha=0.7)
    ax.plot(-1, y_f, "o", color="red")
    angle_f = np.degrees(np.arctan2(y_f, -1))
    ax.text(-1, y_f, thema, fontsize=9,
            rotation=angle_f, rotation_mode='anchor',
            ha='right', va='bottom' if y_f >= 0 else 'top')

    # Jungen
    ax.plot([0, 1], [0, y_m], color="blue", alpha=0.7)
    ax.plot(1, y_m, "o", color="blue")
    angle_m = np.degrees(np.arctan2(y_m, 1))
    ax.text(1, y_m, thema, fontsize=9,
            rotation=angle_m, rotation_mode='anchor',
            ha='left', va='bottom' if y_m >= 0 else 'top')

ax.set_xlim(-1.6, 1.6)
ax.set_ylim(-4.5, 4.5)
ax.set_xticks([])
ax.set_ylabel("unterrepräsentiert / überrepräsentiert")
ax.set_xlabel("Themen im Physikunterricht")
ax.set_title("Wahrgenommenes Unterrichtsangebot nach Geschlecht")
plt.tight_layout()
plt.show()
