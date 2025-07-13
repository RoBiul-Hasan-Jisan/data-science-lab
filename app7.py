import streamlit as st
import pandas as pd
import numpy as np
import joblib
import os

MODEL_DIR = r"D:\ml_lern\model"

# Title and sidebar info
st.title("🏡 King County House Price Prediction")

st.sidebar.header("Select Model & Info")
model_options = [
    "linear_regression.pkl",
    "multiple_linear_regression.pkl",
    "polynomial_regression.pkl",
    "ridge_regression.pkl",
    "lasso_regression.pkl",
    "elastic_net.pkl",
    "svr.pkl",
    "decision_tree.pkl",
    "random_forest.pkl",
    "xgboost.pkl",
    "lightgbm.pkl",
    "catboost.pkl",
    "knn.pkl"
]
selected_model = st.sidebar.selectbox("Select Model", model_options)

st.sidebar.markdown(
    """
    This app predicts house prices based on selected features.
    Choose the model on the left, adjust the house features below, then hit **Predict Price**.
    """
)

# Load data for input ranges
@st.cache_data
def load_data():
    df = pd.read_csv(r"D:\ml_lern\data\kc_house_data.csv")
    for col in ['id', 'date']:
        if col in df.columns:
            df = df.drop(col, axis=1)
    return df

df = load_data()

# Load model, scaler, poly
model_path = os.path.join(MODEL_DIR, selected_model)
model = joblib.load(model_path)
scaler = joblib.load(os.path.join(MODEL_DIR, "scaler.pkl"))
poly = joblib.load(os.path.join(MODEL_DIR, "poly.pkl"))

st.header("Enter House Features")

# Split features into two columns for better layout
cols = st.columns(2)

# Get list of features except price
features_list = list(df.drop('price', axis=1).columns)

# Function to create sliders or number inputs with tooltips
def feature_input(col_name, container):
    min_val = float(df[col_name].min())
    max_val = float(df[col_name].max())
    mean_val = float(df[col_name].mean())
    step = 1.0
    tooltip = f"Range: {min_val} to {max_val}"
    if df[col_name].dtype == 'float64' or df[col_name].dtype == 'float32':
        step = 0.01
    # Use slider for certain continuous variables, number_input for others
    if max_val - min_val > 10 and col_name != 'waterfront' and col_name != 'view':
        return container.slider(label=f"{col_name.title()}", min_value=min_val, max_value=max_val, value=mean_val, step=step, help=tooltip)
    else:
        # For binary or small range features, use number input
        return container.number_input(label=f"{col_name.title()}", min_value=min_val, max_value=max_val, value=mean_val, step=step, help=tooltip)

# Assign inputs alternately to columns for neatness
input_values = {}
for i, feature in enumerate(features_list):
    col_container = cols[i % 2]
    input_values[feature] = feature_input(feature, col_container)

input_df = pd.DataFrame([input_values])

# Prepare data for prediction
X_input = input_df.values

if selected_model == "polynomial_regression.pkl":
    X_scaled = scaler.transform(X_input)
    X_poly = poly.transform(X_scaled)
    input_for_pred = X_poly
elif selected_model in ["linear_regression.pkl", "multiple_linear_regression.pkl",
                        "ridge_regression.pkl", "lasso_regression.pkl", "elastic_net.pkl",
                        "svr.pkl", "knn.pkl"]:
    input_for_pred = scaler.transform(X_input)
else:
    input_for_pred = X_input

if st.button("Predict Price"):
    prediction = model.predict(input_for_pred)[0]
    st.markdown(
        f"""
        <div style="
            background-color:#E6F2FF;
            padding:15px;
            border-radius:10px;
            margin-top:20px;
            font-size:20px;
            font-weight:bold;
            color:#003366;">
            💰 Predicted House Price: ${prediction:,.2f}
        </div>
        """,
        unsafe_allow_html=True
    )

if st.checkbox("Show raw data"):
    st.write(df.head())
