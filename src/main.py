from fastapi import FastAPI

from .inference import get_prediction
from .entities import PredictRequest, PredictResponse


app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hello from the ML Inference API"}

@app.post("/predict", response_model=PredictResponse)
def predict(req: PredictRequest):
    """
    Принимает JSON вида:
    {
        "features": [1.0, 2.5, 3.1, ...]
    }
    Возвращает:
    {
        "prediction": 10.4
    }
    """
    pred_value = get_prediction(req.features)
    return PredictResponse(prediction=pred_value)
