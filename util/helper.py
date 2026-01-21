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