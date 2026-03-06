import mlflow

from src.data_ingestion import load_data
from src.data_preprocessing import preprocess_data
from src.train_model import train_model
from src.evaluate_model import evaluate_model
import pandas as pd

def engineer_features(df):

    df["rooms_per_household"] = df["total_rooms"] / df["households"]

    df["bedrooms_ratio"] = df["total_bedrooms"] / df["total_rooms"]

    df["population_per_household"] = df["population"] / df["households"]

    return df


mlflow.set_experiment("housing-price-training")


def run_pipeline():

    with mlflow.start_run():

        df = load_data("data/dataset.csv")
        df = engineer_features(df)

        X_train, X_test, y_train, y_test = preprocess_data(df)

        model = train_model(X_train, y_train)

        evaluate_model(model, X_test, y_test)


if __name__ == "__main__":
    run_pipeline()