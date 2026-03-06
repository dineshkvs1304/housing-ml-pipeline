def validate_data(df):

    if df.isnull().sum().sum() > 0:
        df = df.dropna()

    return df