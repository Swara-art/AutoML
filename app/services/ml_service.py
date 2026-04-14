import pandas as pd
import numpy as np
import os
import joblib
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score, r2_score

# ROOT PATH
ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))

MODEL_DIR = os.path.join(ROOT_DIR, "models")
os.makedirs(MODEL_DIR, exist_ok=True)

def analyze_data(df: pd.DataFrame):
    column_info = {}
    for col in df.columns:
        column_info[col] = {
            "dtype": str(df[col].dtype),
            "unique_values": int(df[col].nunique()),
            "missing_values": int(df[col].isnull().sum())
        }
    return {
        "columns_analysis": column_info,
        "total_rows": len(df),
        "message": "Select target column to proceed"
    }

def train_model(df: pd.DataFrame, file_id: str, target: str):
    # Basic cleaning: drop rows where target is missing
    df = df.dropna(subset=[target])
    
    # Fill missing values in other columns
    for col in df.columns:
        if df[col].dtype == "object":
            df[col] = df[col].fillna(df[col].mode()[0] if not df[col].mode().empty else "Unknown")
        else:
            df[col] = df[col].fillna(df[col].mean())

    X = df.drop(columns=[target])
    y = df[target]

    # Feature Encoding for X
    X = pd.get_dummies(X)
    feature_columns = X.columns.tolist()

    # Determine problem type
    is_categorical = y.dtype == "object" or y.nunique() < 10
    label_encoder = None

    if is_categorical:
        model_type = "classification"
        label_encoder = LabelEncoder()
        y = label_encoder.fit_transform(y.astype(str))
        model = LogisticRegression(max_iter=1000)
    else:
        model_type = "regression"
        model = LinearRegression()

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)

    if model_type == "classification":
        score = accuracy_score(y_test, y_pred.round())
    else:
        score = r2_score(y_test, y_pred)

    # Save model, feature columns, and label encoder
    model_data = {
        "model": model,
        "feature_columns": feature_columns,
        "model_type": model_type,
        "label_encoder": label_encoder,
        "target": target
    }
    
    model_path = os.path.join(MODEL_DIR, f"{file_id}.pkl")
    joblib.dump(model_data, model_path)

    return {
        "model_type": model_type,
        "score": float(score),
        "message": "Model trained successfully"
    }

def predict(file_id: str, data: dict):
    model_path = os.path.join(MODEL_DIR, f"{file_id}.pkl")
    if not os.path.exists(model_path):
        return {"error": "Model not found. Please train the model first."}

    model_data = joblib.load(model_path)
    model = model_data["model"]
    feature_columns = model_data["feature_columns"]
    label_encoder = model_data["label_encoder"]

    # Prep input data
    input_df = pd.DataFrame([data])
    
    # Ensure types match (some might come as strings from API)
    # We don't have the original schema here easily, but we can try to infer or just use get_dummies
    input_df = pd.get_dummies(input_df)

    # Align columns with training data
    for col in feature_columns:
        if col not in input_df.columns:
            input_df[col] = 0
            
    input_df = input_df[feature_columns]

    prediction = model.predict(input_df)[0]
    
    result = float(prediction)
    if label_encoder:
        try:
            result = label_encoder.inverse_transform([int(round(prediction))])[0]
        except:
            pass # Keep as float if inverse fails

    return {
        "prediction": result
    }