import uvicorn  # ASGI server for running FastAPI applications
from fastapi import FastAPI  # Import FastAPI framework
from BankNotes import BankNote  # Import the Pydantic model for input validation
import numpy as np
import pickle
import pandas as pd

# Initialize a FastAPI app
app = FastAPI()

# Load the trained model from the pickle file
model = open("classifier.pkl", "rb")  # Open the saved model in read-binary mode
classifier = pickle.load(model)  # Load the trained model

# Root endpoint - A simple welcome message
@app.get('/')
def index():
    return {"message": "Hello, World"}

# Prediction endpoint - Accepts a POST request with BankNote data
@app.post('/predict')
def predict_authentication(data: BankNote):  # Enforces input validation using BankNote model
    data = data.dict()  # Convert Pydantic model object to a Python dictionary
    
    # Extract individual feature values from the request
    variance = data['variance']
    skewness = data['skewness']
    curtosis = data['curtosis']
    entropy = data['entropy']

    # Make a prediction using the trained model
    prediction = classifier.predict([[variance, skewness, curtosis, entropy]])

    # Convert numerical prediction to human-readable output
    if prediction[0] > 0.5:
        prediction = "Fake!"  # If output is 1, classify as Fake note
    else:
        prediction = "Not Fake!"  # If output is 0, classify as Not Fake

    # Return the prediction result as JSON
    return {
        'prediction': prediction
    }

# Run the FastAPI application using Uvicorn
if __name__ == '__main__':
    uvicorn.run(app, host='120.0.0.1', port=8000)
