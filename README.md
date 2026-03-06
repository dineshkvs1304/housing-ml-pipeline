# Housing Price Prediction API

## Overview

This project demonstrates an end-to-end machine learning workflow for predicting housing prices using a structured dataset. The goal of the project was to build a small but realistic machine learning system where a trained model can be accessed through an API and used to generate predictions based on new input data.

The model is trained on the California Housing dataset and exposed through a FastAPI service. Users can send feature values to the API and receive a predicted housing price in response.

The project focuses on showing how machine learning models move from training to deployment in a clean and organized way.

---

## Project Architecture

The workflow of the system follows a simple machine learning pipeline:

Data → Preprocessing → Model Training → Model Serialization → API Deployment → Prediction

1. **Data Processing**  
   The dataset is loaded and prepared using custom preprocessing logic. Numerical and categorical features are handled separately to ensure the model receives properly formatted inputs.

2. **Model Training**  
   A Random Forest regression model is trained on the processed dataset. The training process includes splitting the data, fitting the model, and evaluating performance.

3. **Experiment Tracking**  
   MLflow is used during training to log model parameters and evaluation metrics. This allows experiments to be tracked and compared easily.

4. **Model Serialization**  
   Once the model is trained, the entire pipeline (including preprocessing steps) is saved as a serialized file called `model.pkl`.

5. **Prediction API**  
   A FastAPI application loads the trained model and exposes an endpoint that allows users to submit input features and receive predicted housing prices.

---

## Tech Stack

- Python  
- FastAPI  
- Scikit-learn  
- Pandas  
- MLflow  
- Docker  

---

## Project Structure

```
housing-ml-pipeline
│
├── api
│   ├── inference_api.py
│   └── schema.py
│
├── src
│   ├── data
│   ├── features
│   ├── models
│   └── utils
│
├── data
│   └── housing.csv
│
├── model.pkl
├── Dockerfile
├── requirements.txt
└── README.md
```

---

## Running the Project Locally

Clone the repository:

```
git clone https://github.com/yourusername/housing-ml-pipeline.git
```

Move into the project folder:

```
cd housing-ml-pipeline
```

Install the required dependencies:

```
pip install -r requirements.txt
```

Start the FastAPI server:

```
uvicorn api.inference_api:app --reload
```

Open the API documentation in your browser:

```
http://127.0.0.1:8000/docs
```

This page provides an interactive interface where you can test the prediction endpoint.

---

## Example Prediction Request

Endpoint:

```
POST /predict
```

Request body:

```json
{
  "median_income": 5,
  "housing_median_age": 20,
  "total_rooms": 2000,
  "total_bedrooms": 400,
  "population": 1000,
  "households": 350,
  "latitude": 34,
  "longitude": -118,
  "ocean_proximity": "INLAND"
}
```

Example response:

```json
{
  "predicted_price": 229511
}
```

---

## Health Check Endpoint

The API includes a simple endpoint to verify that the service is running.

```
GET /health
```

Response:

```
{
  "status": "API is running"
}
```

---

## Future Improvements

Some possible improvements for extending this project include:

- Model versioning using MLflow Model Registry  
- Automated training pipelines  
- CI/CD integration  
- Container orchestration using Kubernetes  
- Monitoring and logging integration  

---

## Author

Kandyana Venkata Sai Dinesh