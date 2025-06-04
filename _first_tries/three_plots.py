import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
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

# Kürzere Namen ohne "Diff_"
themen_kurz = [t.replace("Diff_", "") for t in themen_raw]
umbenennung = dict(zip(themen_raw, themen_kurz))
df = df.rename(columns=umbenennung)

# Geschlecht umwandeln (z. B. 1 = ♂, 2 = ♀)
geschlecht_map = {1: "♂", 2: "♀"}
df["Geschlecht"] = df["Geschlecht"].map(geschlecht_map)

# === 3. Daten umformen für Plot ===
df_melted = df.melt(id_vars="Geschlecht", value_vars=themen_kurz,
                    var_name="Thema", value_name="Bewertung")

# === 4. Balkendiagramm (Mittelwert ± SD) ===
plt.figure(figsize=(12, 5))
sns.barplot(data=df_melted, x="Thema", y="Bewertung", hue="Geschlecht", ci="sd")
plt.axhline(0, linestyle="--", color="gray")
plt.title("Balkendiagramm: Wahrgenommene Repräsentation nach Geschlecht")
plt.ylabel("Mittelwert der Bewertung")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# === 5. Boxplot (Verteilung) ===
plt.figure(figsize=(12, 5))
sns.boxplot(data=df_melted, x="Thema", y="Bewertung", hue="Geschlecht")
plt.axhline(0, linestyle="--", color="gray")
plt.title("Boxplot: Verteilung der Einschätzungen")
plt.ylabel("Bewertung (-4 bis +4)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# === 6. Heatmap (Mittelwerte je Thema & Geschlecht) ===
pivot = df_melted.groupby(["Thema", "Geschlecht"]).mean().reset_index()
heat = pivot.pivot(index="Thema", columns="Geschlecht", values="Bewertung")

plt.figure(figsize=(6, 8))
sns.heatmap(heat, annot=True, center=0, cmap="coolwarm", fmt=".2f")
plt.title("Heatmap: Durchschnittliche Bewertung je Thema & Geschlecht")
plt.tight_layout()
plt.show()
