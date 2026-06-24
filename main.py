from fastapi import FastAPI
from pydantic import BaseModel
from inference import predict
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class InputData(BaseModel):
    pregnancies: float
    glucose: float
    blood_pressure: float
    skin_thickness: float
    insulin: float
    bmi: float
    pedigree: float
    age: float

@app.post("/predict")
def get_prediction(data: InputData):
    pred, prob = predict(data)

    re turn {
        "prediction": pred,
         "confidence": round(prob * 100, 2)
    }