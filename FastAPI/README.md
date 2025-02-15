# Model Deployment Using FastAPI - Bank Note Authentication

## Overview  
This project demonstrates how to use **FastAPI** to build an API that authenticates banknotes as **real or fake** using a **machine learning model** trained on the BankNote Authentication dataset.  

We use **Random Forest Classifier** from `scikit-learn` for prediction and **FastAPI** for creating a simple API that serves the model. The API takes numerical inputs representing the statistical properties of banknotes and returns whether they are **"Fake"** or **"Not Fake"**.

---

## What is FastAPI?  
**FastAPI** is a modern, fast (high-performance) web framework for building APIs with Python. It is based on standard Python **type hints** and offers:  
✅ **Automatic API documentation** (Swagger UI & ReDoc)  
✅ **Asynchronous support** (ideal for high-performance apps)  
✅ **Fast execution** (thanks to Starlette & Pydantic)  
✅ **Type validation** (ensures correct input format)  

FastAPI is an excellent choice for serving machine learning models as web APIs.

---

## Run the FastAPI Server
```
uvicorn app:app --host 127.0.0.1 --port 8000 --reload
```
## Test the API
Open your browser and go to:
🔹 Swagger UI: http://127.0.0.1:8000/docs
🔹 Redoc UI: http://127.0.0.1:8000/redoc

To test via cURL or Postman, send a POST request to:
```
POST http://127.0.0.1:8000/predict
Content-Type: application/json
{
    "variance": 2.1,
    "skewness": 3.2,
    "curtosis": 1.5,
    "entropy": 0.9
}
```
