from pydantic import BaseModel
from typing import Literal


class EVPurchaseInput(BaseModel):
    Age: int
    Annual_Income_USD: float
    Daily_Commute_km: float
    Number_of_Cars_Owned: int
    Charging_Stations_Near_Home: int
    Charging_Stations_Near_Work: int
    Environmental_Concern_Level: float
    Gender: Literal["Male", "Female", "Other"]
    City_Type: Literal["Urban", "Suburban", "Rural"]
    Current_Car_Type: Literal["Sedan", "SUV", "Hatchback", "Truck"]
    Home_Charging_Possible: Literal["Yes", "No"]
    Subsidy_Available: Literal["Yes", "No"]
    Range_Anxiety_Level: Literal["Low", "Medium", "High"]


class PredictionOutput(BaseModel):
    probability: float
