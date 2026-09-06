from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
import lightgbm as lgb
 
LGB_PARAMS = dict(
    n_estimators=1000,
    max_depth=3,
    learning_rate=0.1,
    num_leaves=31,
    subsample=0.6,
    colsample_bytree=0.8,
    random_state=42,
)
 
 
def build_pipeline(categorical_cols):
    transformer = ColumnTransformer(
        [("one_hot", OneHotEncoder(drop="first", handle_unknown="ignore"), categorical_cols)],
        remainder="passthrough",
    )
 
    pipe = Pipeline([
        ("transformer", transformer),
        ("model", lgb.LGBMClassifier(**LGB_PARAMS)),
    ])
 
    return pipe
 