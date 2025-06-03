import pyreadstat

df, meta = pyreadstat.read_sav("Datensatz_Roman.sav")
print(df.head())
