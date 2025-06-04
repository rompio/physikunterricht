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

# Explizite Umbenennung (bes. für "die Welt")
umbenennung = {col: col.replace("Diff_", "") for col in themen_raw}
umbenennung["Diff_dieWelt"] = "die Welt"  # explizit Leerzeichen statt "dieWelt"
df = df.rename(columns=umbenennung)

# Liste der neuen, verkürzten Spaltennamen
themen_kurz = list(umbenennung.values())

# === 3. Geschlecht umwandeln (1 = ♂, 2 = ♀) ===
geschlecht_map = {1: "♂", 2: "♀"}
df["Geschlecht"] = df["Geschlecht"].map(geschlecht_map)

# === 4. Daten umformen für Violinplot ===
df_melted = df.melt(id_vars="Geschlecht", value_vars=themen_kurz,
                    var_name="Thema", value_name="Bewertung")

# === 5. Violinplot erstellen ===
plt.figure(figsize=(12, 6))
sns.violinplot(
    data=df_melted,
    x="Thema",
    y="Bewertung",
    hue="Geschlecht",
    split=True,
    inner="quartile",
    # palette={"♀": "red", "♂": "lightblue"} 
)

# === 6. Formatierungen ===
plt.axhline(0, linestyle="--", color="gray")
plt.title("Wahrgenommenes Unterrichtsangebot nach Geschlecht")
plt.ylabel("unterrepräsentiert / überrepräsentiert")
plt.xlabel("Themen im Physikunterricht")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
