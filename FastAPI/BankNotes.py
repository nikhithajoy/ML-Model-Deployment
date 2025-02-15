# Import BaseModel from Pydantic for data validation
from pydantic import BaseModel

# Define a Pydantic model to validate input data for API requests
class BankNote(BaseModel):
    variance: float  # Feature representing variance of wavelet-transformed image
    skewness: float  # Feature representing skewness of the image
    curtosis: float  # Feature representing curtosis (shape of the probability distribution)
    entropy: float   # Feature representing entropy (measure of randomness)
