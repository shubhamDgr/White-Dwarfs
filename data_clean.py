import pandas as pd
dz = pd.read_csv("E:/Projects/white_dwarf_mass/data/type_DZ.csv")
daz = pd.read_csv("E:/Projects/white_dwarf_mass/data/type_DAZ.csv")
dbz = pd.read_csv("E:/Projects/white_dwarf_mass/data/type_DBZ.csv")

indices_to_drop_dz = []
for index, column in enumerate(dz.columns):
    if dz[column].isna().all():  # Check if the entire column is NaN
        indices_to_drop_dz.append(index)

dz_cleaned = dz.drop(dz.columns[indices_to_drop_dz], axis=1)
dz_cleaned.to_csv('data/dz_clean.csv', index=False)
def dz_clean():
    dz_clean = pd.read_csv("E:/Projects/white_dwarf_mass/data/dz_clean.csv")
    return dz_clean


indices_to_drop_daz = []
for index, column in enumerate(daz.columns):
    if daz[column].isna().all():  # Check if the entire column is NaN
        indices_to_drop_daz.append(index)

daz_cleaned = daz.drop(daz.columns[indices_to_drop_daz], axis=1)
daz_cleaned.to_csv('data/daz_clean.csv', index=False)
def daz_clean():
    daz_clean = pd.read_csv("E:/Projects/white_dwarf_mass/data/daz_clean.csv")
    return daz_clean

indices_to_drop_dbz = []
for index, column in enumerate(dbz.columns):
    if dbz[column].isna().all():  # Check if the entire column is NaN
        indices_to_drop_dbz.append(index)

dbz_cleaned = dbz.drop(dbz.columns[indices_to_drop_dbz], axis=1)
dbz_cleaned.to_csv('data/dbz_clean.csv', index=False)
def dbz_clean():
    dbz_clean = pd.read_csv("E:/Projects/white_dwarf_mass/data/dbz_clean.csv")
    return dbz_clean