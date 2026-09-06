from processing.data_manager import load_data, load_pipeline
 
 
def run_prediction(input_df=None):
    pipe = load_pipeline()
 
    if input_df is not None:
        proba = pipe.predict_proba(input_df)[:, 1]
        return proba
 
    train, test, sample_submission = load_data()
    proba = pipe.predict_proba(test)[:, 1]
    sample_submission["Will_Buy_EV"] = proba
    sample_submission.to_csv("submissions/submission.csv", index=False)
    print("Predictions saved to submissions/submission.csv")
    return proba
 
 
if __name__ == "__main__":
    run_prediction()