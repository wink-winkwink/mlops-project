from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class HouseFeatures(BaseModel):
    area: float
    rooms: int

@app.get("/")
def read_root():
    return {"message": "API is ready!"}

@app.post("/predict")
def predict_price(features: HouseFeatures):
    
    calculated_price = (features.area * 10000) + (features.rooms * 50000)
    
    return {
        "status": "success",
        "predicted_price": calculated_price,
        "features_received": features
    }