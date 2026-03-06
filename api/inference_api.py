from fastapi import FastAPI
import pandas as pd
import pickle

from api.schema import HousingInput
from src.utils.logger import logger

# Initialize FastAPI
app = FastAPI(title="Housing Price Prediction API")

# Load trained model
with open("model.pkl", "rb") as f:
    model = pickle.load(f)


# Health check endpoint
@app.get("/health")
def health_check():
    return {"status": "API is running"}


# Prediction endpoint
@app.post("/predict")
def predict(data: HousingInput):

    try:
        logger.info("Prediction request received")

        # Convert input to dataframe
        input_df = pd.DataFrame([data.dict()])

        # Make prediction
        prediction = model.predict(input_df)

        logger.info(f"Prediction result: {prediction[0]}")

        return {
            "predicted_price": float(prediction[0])
        }

    except Exception as e:

        logger.error(f"Prediction error: {str(e)}")

        return {
            "error": str(e)
        }