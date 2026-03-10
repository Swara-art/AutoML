import pandas as pd

def dataset_summary(df):

    summary = {}

    summary["rows"] = df.shape[0]
    summary["columns"] = df.shape[1]
    summary["missing_values"] = df.isnull().sum()
    summary["numeric_columns"] = df.select_dtypes(include=["int64","float64"]).columns.tolist()
    summary["categorical_columns"] = df.select_dtypes(include=["object"]).columns.tolist()

    return summary