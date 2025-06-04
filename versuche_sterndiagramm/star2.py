import pandas as pd
import matplotlib.pyplot as plt

# Excel-Datei laden
df = pd.read_excel("Datensatz_Roman.xlsx")
df.columns = df.columns.str.strip()

# Geschlecht umkodieren
df["Geschlecht"] = df["Geschlecht"].map({1: "♂", 2: "♀"})

# Themenliste
themen = ['Licht', 'Töne', 'Bewegung', 'Wärme', 'Elektrizität', 'Elektronik',
          'die Welt', 'Radioaktivität', 'Astrophysik', 'Nachrichtentechnik', 'Computer', 'Fliegen']
df.rename(columns={"dieWelt": "die Welt"}, inplace=True)

# Mittelwerte berechnen
mittelwerte = {"♀": [], "♂": []}
mittelwert_tabelle = []

for thema in themen:
    df_thema = df[[thema, "Geschlecht"]].dropna()
    mw_f = df_thema[df_thema["Geschlecht"] == "♀"][thema].mean()
    mw_m = df_thema[df_thema["Geschlecht"] == "♂"][thema].mean()
    mittelwerte["♀"].append(mw_f)
    mittelwerte["♂"].append(mw_m)
    mittelwert_tabelle.append((thema, round(mw_f, 2), round(mw_m, 2)))

# Plot
fig, ax = plt.subplots(figsize=(11, 8))
ax.axhline(0, color="black", linewidth=1)
ax.axvline(0, color="black", linewidth=1)

for i, thema in enumerate(themen):
    y_female = mittelwerte["♀"][i]
    y_male = mittelwerte["♂"][i]
    ax.plot([-1, 0], [y_female, 0], color="red", alpha=0.7)
    ax.plot([0, 1], [0, y_male], color="blue", alpha=0.7)
    ax.plot(-1, y_female, "o", color="red")
    ax.plot(1, y_male, "o", color="blue")
    ax.text(-1.1, y_female, thema, va="center", ha="right", fontsize=9)
    ax.text(1.1, y_male, thema, va="center", ha="left", fontsize=9)

ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-4.5, 4.5)
ax.set_xticks([])
ax.set_ylabel("unterrepräsentiert / überrepräsentiert")
ax.set_xlabel("Themen im Physikunterricht")
ax.set_title("Wahrgenommenes Unterrichtsangebot nach Geschlecht")
plt.tight_layout()
plt.show()

# Mittelwerte ausgeben
for thema, mw_f, mw_m in mittelwert_tabelle:
    print(f"{thema:20} ♀: {mw_f:>5}   ♂: {mw_m:>5}")
