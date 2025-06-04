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

# === 3. Daten umformen für Violinplot ===
df_melted = df.melt(id_vars="Geschlecht", value_vars=themen_kurz,
                    var_name="Thema", value_name="Bewertung")

# === 4. Violinplot ===
plt.figure(figsize=(12, 6))
sns.violinplot(data=df_melted, x="Thema", y="Bewertung", hue="Geschlecht", split=True, inner="quartile")
plt.axhline(0, linestyle="--", color="gray")
plt.title("Violinplot: Wahrnehmung nach Thema & Geschlecht")
plt.ylabel("Bewertung (-4 = unterrepräsentiert, +4 = überrepräsentiert)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
