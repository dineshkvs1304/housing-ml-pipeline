import pandas as pd

def engineer_features(df):

    df["rooms_per_household"] = df["total_rooms"] / df["households"]

    df["bedrooms_ratio"] = df["total_bedrooms"] / df["total_rooms"]

    df["population_per_household"] = df["population"] / df["households"]

    return df