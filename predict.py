from processing.data_manager import load_data, load_pipeline
from processing.features import add_features, encode_binary_ordinal


def run_prediction(input_df=None):
    pipe = load_pipeline()

    if input_df is not None:
        _, input_df = encode_binary_ordinal(input_df.copy(), input_df.copy())
        _, input_df = add_features(input_df.copy(), input_df.copy())
        proba = pipe.predict_proba(input_df)[:, 1]
        return proba

    train, test, sample_submission = load_data()
    train, test = encode_binary_ordinal(train, test)
    train, test = add_features(train, test)
    proba = pipe.predict_proba(test.drop(columns=["id"]))[:, 1]
    sample_submission["Will_Buy_EV"] = proba
    sample_submission.to_csv("submissions/submission.csv", index=False)
    print("Predictions saved to submissions/submission.csv")
    return proba


if __name__ == "__main__":
    run_prediction()
