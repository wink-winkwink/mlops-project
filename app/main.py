from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import joblib
import pandas as pd

app = FastAPI()

model = joblib.load("app/house_model.joblib")

class HouseFeatures(BaseModel):
    area: float
    rooms: int

@app.get("/")
def read_root():
    return {"status": "online", "message": "Model is deployed"}

@app.post("/predict")
def predict_price(features: HouseFeatures):
    
    if features.area <= 0:
        raise HTTPException(status_code=400, detail="Error : Area can't be negative!")
    
    if features.rooms <= 0:
        raise HTTPException(status_code=400, detail="Error : Room can't be negative!")
    
    input_df = pd.DataFrame([features.model_dump()])
    
    prediction = model.predict(input_df)
    
    final_price = prediction[0].item()
    
    if final_price < 0:
        raise HTTPException(status_code=400, detail="Prediction Error : Price can't be negative!")
        
    return {
        "status": "success",
        "predicted_price": final_price,
        "method": "Random Forest / Linear Regression Model"
    }