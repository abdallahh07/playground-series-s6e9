import pandas as pd
from fastapi import APIRouter

from app.schemas import EVPurchaseInput, PredictionOutput
from predict import run_prediction

router = APIRouter()


@router.post("/predict", response_model=PredictionOutput)
def predict(input_data: EVPurchaseInput):
    input_df = pd.DataFrame([input_data.model_dump()])
    proba = run_prediction(input_df=input_df)
    return PredictionOutput(probability=float(proba[0]))
