import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

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

# Jeweils sortieren
n = len(themen)

# ♀ sortieren
sorted_f = sorted(zip(themen, mittelwerte["♀"]), key=lambda x: x[1], reverse=True)
themen_f_sorted, y_f_sorted = zip(*sorted_f)
top_f, bottom_f = max(y_f_sorted), min(y_f_sorted)
label_y_f = np.linspace(top_f, bottom_f, n)

# ♂ sortieren
sorted_m = sorted(zip(themen, mittelwerte["♂"]), key=lambda x: x[1], reverse=True)
themen_m_sorted, y_m_sorted = zip(*sorted_m)
top_m, bottom_m = max(y_m_sorted), min(y_m_sorted)
label_y_m = np.linspace(top_m, bottom_m, n)

# Thema → Label-Position Mapping
label_y_f_map = dict(zip(themen_f_sorted, label_y_f))
label_y_m_map = dict(zip(themen_m_sorted, label_y_m))

# Plot
fig, ax = plt.subplots(figsize=(11, 8))
ax.axhline(0, color="black", linewidth=1)
ax.axvline(0, color="black", linewidth=1)

for i, thema in enumerate(themen):
    y_f = mittelwerte["♀"][i]
    y_m = mittelwerte["♂"][i]
    
    # Linien
    ax.plot([-1, 0], [y_f, 0], color="red", alpha=0.7)
    ax.plot([0, 1], [0, y_m], color="blue", alpha=0.7)
    
    # Punkte
    ax.plot(-1, y_f, "o", color="red", zorder=3)
    ax.plot(1, y_m, "o", color="blue", zorder=3)
    
    # Texte auf eigener Seite, bei individuell gestaffeltem Y
    ax.text(-1.15, label_y_f_map[thema], thema, ha="right", va="center", fontsize=9)
    ax.text(1.15, label_y_m_map[thema], thema, ha="left", va="center", fontsize=9)

# Geschlechtssymbole am Rand
ax.text(-1.4, 2.05, "♀", fontsize=16, ha="center", va="center", color="red")
ax.text(1.4, 2.05, "♂", fontsize=16, ha="center", va="center", color="blue")

# Achsenformat
ax.set_xlim(-1.6, 1.6)
ax.set_ylim(-2, 2.2)
ax.set_xticks([])
ax.set_ylabel("unterrepräsentiert / überrepräsentiert")
ax.set_xlabel("Themen im Physikunterricht")
ax.set_title("Wahrgenommenes Unterrichtsangebot nach Geschlecht")
plt.tight_layout()
plt.show()

# Mittelwerte ausgeben
for thema, mw_f, mw_m in mittelwert_tabelle:
    print(f"{thema:20} ♀: {mw_f:>5}   ♂: {mw_m:>5}")
