import mlflow
from sklearn.metrics import mean_squared_error

def evaluate_model(model, X_test, y_test):

    predictions = model.predict(X_test)

    mse = mean_squared_error(y_test, predictions)

    # log metric
    mlflow.log_metric("mse", mse)

    print("Model evaluation MSE:", mse)