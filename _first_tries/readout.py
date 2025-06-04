import pandas as pd
import pyreadstat

df, meta = pyreadstat.read_sav("Datensatz_Roman.sav")

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

print(df)
