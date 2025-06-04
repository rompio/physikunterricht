import pandas as pd
import matplotlib.pyplot as plt

# === 1. Daten einlesen ===
df = pd.read_excel("Datensatz_Roman.xlsx")
df.columns = df.columns.str.strip()

# === 2. Geschlecht umkodieren (1 = ♂, 2 = ♀) ===
df["Geschlecht"] = df["Geschlecht"].map({1: "♂", 2: "♀"})

# === 3. Themenliste ===
themen = ['Licht', 'Töne', 'Bewegung', 'Wärme', 'Elektrizität', 'Elektronik',
          'dieWelt', 'Radioaktivität', 'Astrophysik', 'Nachrichtentechnik', 'Computer', 'Fliegen']

# === 4. Durchschnittswerte berechnen ===
mittelwerte = {"♀": [], "♂": []}
for thema in themen:
    df_thema = df[[thema, "Geschlecht"]].dropna()
    mittelwerte["♀"].append(df_thema[df_thema["Geschlecht"] == "♀"][thema].mean())
    mittelwerte["♂"].append(df_thema[df_thema["Geschlecht"] == "♂"][thema].mean())

# === 5. Plot vorbereiten ===
fig, ax = plt.subplots(figsize=(10, 8))
ax.axhline(0, color="black", linewidth=1)
ax.axvline(0, color="black", linewidth=1)

# === 6. Themenstrahlen zeichnen ===
for i, thema in enumerate(themen):
    y_female = mittelwerte["♀"][i]
    y_male = mittelwerte["♂"][i]

    # Linien von Mittelpunkt nach links (♀) und rechts (♂)
    ax.plot([-1, 0], [y_female, 0], label=f"{thema} (♀)", color="red", alpha=0.7)
    ax.plot([0, 1], [0, y_male], label=f"{thema} (♂)", color="blue", alpha=0.7)

    # Punkte an den Enden
    ax.plot(-1, y_female, "o", color="red")
    ax.plot(1, y_male, "o", color="blue")

    # Themenbeschriftung
    ax.text(-1.1, y_female, thema, va="center", ha="right", fontsize=9)
    ax.text(1.1, y_male, thema, va="center", ha="left", fontsize=9)

# === 7. Achsen und Layout ===
ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-4.5, 4.5)
ax.set_xticks([])
ax.set_ylabel("Bewertung (-4 = unterrepräsentiert, +4 = überrepräsentiert)")
ax.set_title("Bewertungen nach Thema und Geschlecht (sternförmig)")

plt.tight_layout()
plt.show()
