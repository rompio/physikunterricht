import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import pyreadstat

# Datei laden
df, meta = pyreadstat.read_sav("Datensatz_Roman.sav")

# Liste der Themen
themen = [
    'Diff_Licht', 'Diff_Töne', 'Diff_Bewegung', 'Diff_Wärme',
    'Diff_Elektrizität', 'Diff_Elektronik', 'Diff_dieWelt',
    'Diff_Radioaktivität', 'Diff_Astrophysik',
    'Diff_Nachrichtentechnik', 'Diff_Computer', 'Diff_Fliegen'
]

# Daten umformen für Plot
df_melted = df.melt(id_vars="Geschlecht", value_vars=themen,
                    var_name="Thema", value_name="Bewertung")

# Plot
plt.figure(figsize=(12, 6))
sns.barplot(data=df_melted, x="Thema", y="Bewertung", hue="Geschlecht", ci="sd")
plt.axhline(0, linestyle="--", color="gray")
plt.title("Wahrgenommene Repräsentation von Physikthemen nach Geschlecht")
plt.ylabel("Bewertung (-4 = unterrepräsentiert, +4 = überrepräsentiert)")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.show()
