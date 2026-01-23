import pandas as pd

def basic_exploration(my_df, name):
    print('=====================================')
    print(name)
    print('=====================================')


    print('\n~~~~~~~~~~~~~~~~~')
    print('Info')
    print('~~~~~~~~~~~~~~~~~')
    print(my_df.info())

    print('\n~~~~~~~~~~~~~~~~~')
    print('Head')
    print('~~~~~~~~~~~~~~~~~')
    print(my_df.head())

    print('\n~~~~~~~~~~~~~~~~~')
    print('Description')
    print('~~~~~~~~~~~~~~~~~')
    print(my_df.describe())

    print('\n~~~~~~~~~~~~~~~~~')
    print('Missing Values')
    print('~~~~~~~~~~~~~~~~~')
    for col in my_df.columns:
        per_missing = my_df[col].isnull().sum() / len(my_df) * 100
        print(f'{col}: {per_missing:.2f}% missing values')

    print('\n~~~~~~~~~~~~~~~~~')
    print('Value Counts')
    print('~~~~~~~~~~~~~~~~~')
    for col in my_df:
        print(my_df[col].value_counts())

# =================================================
# | Author: Robb Northrup
# | Function set for defining spectral type for stars
# =================================================

# Wrapper function called by notebooks
def define_spectype(row):
    # ----- Class -----
    s_class = define_spectype_class_from_teff(row)

    # FIXED: check s_class, not row['st_spectype']
    if s_class == "UNKNOWN":
        s_class = define_spectype_class_from_cmd(row)

    if s_class == "UNKNOWN":
        return "UNKNOWN"

    # ----- Subclass -----
    s_subclass = define_spectype_subclass(row, s_class)

    # ----- Luminosity Class -----
    s_lumclass = define_spectype_lum(row)

    return f"{s_class}{s_subclass}{s_lumclass}"


# Classify stars by temperature for available TEFF data
# Needs to be adjusted to account for magnitude as well
def define_spectype_class_from_teff(row):
    # no teff value?
    if pd.isnull(row['st_teff']):
        return "UNKNOWN"
    
    # else, assign based on temperatures. . .
    elif row['st_teff'] > 30000:
        return "O"
    elif 10000 < row['st_teff'] <= 30000:
        return "B"
    elif 7500 < row['st_teff'] <= 10000:
        return "A"
    elif 6000 < row['st_teff'] <= 7500:
        return "F"
    elif 5200 < row['st_teff'] <= 6000:
        return "G"
    elif 3700 < row['st_teff'] <= 5200:
        return "K"
    elif row['st_teff'] <= 3700:
        return "M"
    

def define_spectype_class_from_cmd(row):
    color = row["bp_rp"]
    M = row["abs_mag"]

    if pd.isnull(color) or pd.isnull(M):
        return "UNKNOWN"

    # Very hot, blue stars
    if color < 0.0: return "O"
    if 0.0 <= color < 0.3: return "B"
    if 0.3 <= color < 0.6: return "A"
    if 0.6 <= color < 0.9: return "F"
    if 0.9 <= color < 1.3: return "G"
    if 1.3 <= color < 1.8: return "K"
    if color >= 1.8: return "M"

    return "UNKNOWN"


def define_spectype_subclass(row, s_class):
    T = row["st_teff"]

    if pd.isnull(T):
        return "_"

    ranges = {
        "O": (30000, 50000),
        "B": (10000, 30000),
        "A": (7500, 10000),
        "F": (6000, 7500),
        "G": (5200, 6000),
        "K": (3700, 5200),
        "M": (2400, 3700)
    }

    Tmin, Tmax = ranges[s_class]

    # Normalize Teff into subclass 0–9
    subclass = int(10 * (Tmax - T) / (Tmax - Tmin))
    return max(0, min(9, subclass))


def define_spectype_lum(row):
    M = row['abs_mag']

    if M < -2:
        return "I"   # supergiant
    elif -2 <= M < 0:
        return "II"  # bright giant
    elif 0 <= M < 2:
        return "III" # giant
    elif 2 <= M < 4:
        return "IV"  # subgiant
    else:
        return "V"   # dwarf