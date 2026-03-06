from sklearn.model_selection import train_test_split
import pandas as pd


def preprocess_data(df):

    # Convert categorical column to numbers
    df = pd.get_dummies(df)

    X = df.drop("median_house_value", axis=1)
    y = df["median_house_value"]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    return X_train, X_test, y_train, y_test