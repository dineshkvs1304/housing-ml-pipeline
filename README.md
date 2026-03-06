![Python](https://img.shields.io/badge/Python-3.10-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-API-green)
![MLflow](https://img.shields.io/badge/MLflow-Experiment%20Tracking-orange)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-ML-red)
![Docker](https://img.shields.io/badge/Docker-Containerization-blue)

# Housing Price Prediction API

## Overview

This project demonstrates an end-to-end machine learning workflow for predicting housing prices using a structured dataset. The goal was to design a simple but realistic ML system where a trained model can be accessed through an API and used to generate predictions based on new input data.

The model is trained on the California Housing dataset and deployed through a FastAPI service. Users can send housing feature values to the API and receive a predicted housing price as a response.

The project focuses on demonstrating how a machine learning model moves from training to deployment in a clean and structured engineering workflow.

---

## System Architecture

The project follows a simple machine learning deployment pipeline.

```
        Dataset
           │
           ▼
  Data Processing & Preprocessing
           │
           ▼
       Model Training
      (Random Forest)
           │
           ▼
      MLflow Tracking
   (parameters / metrics)
           │
           ▼
      Saved Model File
        model.pkl
           │
           ▼
        FastAPI API
         /predict
           │
           ▼
      JSON Prediction
```

---

## Tech Stack

This project uses the following tools and frameworks:

- **Python**
- **FastAPI** – API framework for model inference
- **Scikit-Learn** – machine learning model
- **Pandas** – data handling
- **MLflow** – experiment tracking
- **Docker** – containerization

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
│       └── logger.py
│
├── data
│   └── housing.csv
│
├── Dockerfile
├── requirements.txt
├── README.md
└── .gitignore
```

---

# Running the Project Locally

Follow the steps below to run the project on your machine.

---

## 1. Clone the Repository

```
git clone https://github.com/dineshkvs1304/housing-ml-pipeline.git
```

Move into the project directory.

```
cd housing-ml-pipeline
```

---

## 2. Create a Virtual Environment

Creating a virtual environment keeps project dependencies isolated.

### Windows

```
python -m venv venv
venv\Scripts\activate
```

### Linux / Mac

```
python3 -m venv venv
source venv/bin/activate
```

---

## 3. Install Required Dependencies

Install all required libraries from the requirements file.

```
pip install -r requirements.txt
```

---

## 4. Start the FastAPI Server

Run the API using Uvicorn.

```
uvicorn api.inference_api:app --reload
```

You should see something similar to:

```
Uvicorn running on http://127.0.0.1:8000
```

---

## 5. Open API Documentation

FastAPI automatically generates interactive API documentation.

Open this in your browser:

```
http://127.0.0.1:8000/docs
```

From here you can test the prediction endpoint directly.

---

# Example Prediction Request

Endpoint:

```
POST /predict
```

Example JSON input:

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

Example API response:

```json
{
  "predicted_price": 229511
}
```

---

# Health Check Endpoint

A simple health check endpoint is included to verify that the API is running.

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

# Future Improvements

Some possible improvements for extending this project include:

- Model versioning using MLflow Model Registry  
- Automated training pipelines  
- CI/CD integration  
- Deployment on cloud platforms  
- Model monitoring and logging improvements  

---

# Author

Kandyana Venkata Sai Dinesh
