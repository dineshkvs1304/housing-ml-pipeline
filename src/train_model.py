import mlflow
import mlflow.sklearn
from sklearn.ensemble import RandomForestRegressor

def train_model(X_train, y_train):

    model = RandomForestRegressor(n_estimators=100, random_state=42)

    model.fit(X_train, y_train)

    mlflow.log_param("model", "RandomForestRegressor")
    mlflow.log_param("n_estimators", 100)

    mlflow.sklearn.log_model(
        model,
        "model",
        registered_model_name="housing_price_model"
    )

    return model