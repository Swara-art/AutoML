import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import streamlit as st
import pandas as pd
from src.data_analysis import dataset_summary

st.title("AutoML Model Explorer")

uploaded_file = st.file_uploader("Upload CSV dataset", type=["csv"])

if uploaded_file is not None:

    df = pd.read_csv(uploaded_file)

    st.subheader("Dataset Preview")
    st.dataframe(df.head())

    summary = dataset_summary(df)

    st.write("Rows:", summary["rows"])
    st.write("Columns:", summary["columns"])

    st.subheader("Numeric Columns")
    st.write(summary["numeric_columns"])

    st.subheader("Categorical Columns")
    st.write(summary["categorical_columns"])

    st.subheader("Missing Values")
    st.write(summary["missing_values"])