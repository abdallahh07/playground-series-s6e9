from sklearn.model_selection import train_test_split
from sklearn.metrics import roc_auc_score
 
from processing.data_manager import load_data, save_pipeline
from processing.features import add_features, encode_binary_ordinal
from pipeline import build_pipeline
 
 
def run_training():
    # 1. Load raw data
    train, test, sample_submission = load_data()
 
    # 2. Encode binary/ordinal columns
    train, test = encode_binary_ordinal(train, test)
 
    # 3. Feature engineering
    train, test = add_features(train, test)
 
    # 4. Split features/target
    x = train.drop(columns=["Will_Buy_EV", "id"])
    y = train["Will_Buy_EV"]
 
    x_train, x_val, y_train, y_val = train_test_split(
        x, y, test_size=0.2, stratify=y, random_state=42
    )
 
    # 5. Build pipeline
    categorical_cols = x_train.select_dtypes(include="object").columns.tolist()
    pipe = build_pipeline(categorical_cols)
 
    # 6. Fit + validate
    pipe.fit(x_train, y_train)
    y_pred_proba = pipe.predict_proba(x_val)[:, 1]
    auc = roc_auc_score(y_val, y_pred_proba)
    print(f"Validation AUC: {auc:.4f}")
 
    # 7. Refit on full data
    pipe.fit(x, y)
 
    # 8. Save
    save_pipeline(pipe)
    print("Pipeline saved to trained_model/model.pkl")
 
 
if __name__ == "__main__":
    run_training()