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


# Classify stars by temperature for available TEFF data
# Needs to be adjusted to account for magnitude as well
def spectype_from_teff(row):
    # spectype already . . .
    if not pd.isnull(row["st_spectype"]):
        return row["st_spectype"][0]
    # else, assign based on temperatures. . .
    elif pd.isnull(row["st_spectype"]) and row['st_teff'] > 30000:
        return "O"
    elif pd.isnull(row["st_spectype"]) and 10000 < row['st_teff'] <= 30000:
        return "B"
    elif pd.isnull(row["st_spectype"]) and 7500 < row['st_teff'] <= 10000:
        return "A"
    elif pd.isnull(row["st_spectype"]) and 6000 < row['st_teff'] <= 7500:
        return "F"
    elif pd.isnull(row["st_spectype"]) and 5200 < row['st_teff'] <= 6000:
        return "G"
    elif pd.isnull(row["st_spectype"]) and 3700 < row['st_teff'] <= 5200:
        return "K"
    elif pd.isnull(row["st_spectype"]) and row['st_teff'] <= 3700:
        return "M"
    # if no temp value and no spectype . . . 
    else:
        return "UNKNOWN"