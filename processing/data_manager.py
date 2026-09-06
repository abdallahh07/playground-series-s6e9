import pandas as pd
import joblib
from pathlib import Path

DATA_DIR = Path(__file__).parent.parent/"data"/"raw"
MODEL_DIR = Path(__file__).parent.parent/"trained_model"

def load_data():
    train = pd.read_csv(DATA_DIR / "train.csv")
    test = pd.read_csv(DATA_DIR / "test.csv")
    sample_submission = pd.read_csv(DATA_DIR / "sample_submission.csv")
    return train, test, sample_submission
  
def save_pipeline(pipeline,filename="model.pkl"):
  MODEL_DIR.mkdir(exist_ok=True)
  joblib.dump(pipeline, MODEL_DIR / filename)
  
def load_pipeline(filename="model.pkl"):
  return joblib.load(MODEL_DIR / filename)