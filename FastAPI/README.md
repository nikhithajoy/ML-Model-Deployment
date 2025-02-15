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

## FastAPI Components
FastAPI is a modern, high-performance web framework for building APIs with Python. It is based on Pydantic for data validation and Starlette for ASGI applications. Below are the core components:

### 1. FastAPI App Instance
Before defining API endpoints, you need to create a FastAPI application instance.
```
app = FastAPI()
```
- FastAPI() creates an instance of the FastAPI framework.
- This app instance is used to define API routes and handle requests.

### 2. Route Decorators (@app.get(), @app.post())
Routes define API endpoints, and decorators like @app.get() and @app.post() specify the type of HTTP request.

#### a) @app.get() – Handling GET Requests
The GET method is used for retrieving data from the server.
```
@app.get("/")
def read_root():
    return {"message": "Welcome to FastAPI!"}
```
- The function read_root() is mapped to the root path /.
- When accessed via a browser or API client (GET http://127.0.0.1:8000/), it returns {"message": "Welcome to FastAPI!"}.

#### b) @app.post() – Handling POST Requests
The POST method is used for sending data to the server, typically for creating or modifying resources.
```
@app.post('/predict')
def predict_authentication(data: BankNote):  # Enforces input validation using BankNote model
    //block of code
```

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
