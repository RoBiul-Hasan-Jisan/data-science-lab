import streamlit as st
import pandas as pd
import joblib

# Load saved model and scaler
model = joblib.load(r"D:\ml_lern\model\modelLOR.joblib")
scaler = joblib.load(r"D:\ml_lern\model\scalerLOR.joblib")

st.title("Titanic Survival Prediction")

# User inputs
pclass = st.selectbox("Passenger Class (1 = 1st, 2 = 2nd, 3 = 3rd)", options=[1, 2, 3])
sex = st.selectbox("Sex", options=['male', 'female'])
age = st.number_input("Age", min_value=0.42, max_value=80.0, value=30.0)
sibsp = st.number_input("Number of siblings/spouses aboard", min_value=0, max_value=10, value=0)
parch = st.number_input("Number of parents/children aboard", min_value=0, max_value=10, value=0)
fare = st.number_input("Fare", min_value=0.0, max_value=600.0, value=32.20)
embarked = st.selectbox("Port of Embarkation", options=['C', 'Q', 'S'])
title = st.selectbox("Title", options=['Mr', 'Miss', 'Mrs', 'Master', 'Rare'])

family_size = sibsp + parch + 1

# Build input dictionary with all possible features your model/scaler might expect
input_dict = {
    'Pclass': pclass,
    'Age': age,
    'SibSp': sibsp,
    'Parch': parch,
    'Fare': fare,
    'FamilySize': family_size,
    'Sex_male': 1 if sex == 'male' else 0,
    'Embarked_Q': 1 if embarked == 'Q' else 0,
    'Embarked_S': 1 if embarked == 'S' else 0,
    'Title_Mr': 1 if title == 'Mr' else 0,
    'Title_Miss': 1 if title == 'Miss' else 0,
    'Title_Mrs': 1 if title == 'Mrs' else 0,
    'Title_Master': 1 if title == 'Master' else 0,
    'Title_Rare': 1 if title == 'Rare' else 0,
}

# Get the exact feature names and order expected by the scaler
expected_features = list(scaler.feature_names_in_)

# Filter input_dict to include only features scaler expects
filtered_input_dict = {feature: input_dict.get(feature, 0) for feature in expected_features}

# Create DataFrame with columns in exact order
input_df = pd.DataFrame([filtered_input_dict], columns=expected_features)

# Transform input features using scaler
input_scaled = scaler.transform(input_df)

if st.button("Predict Survival"):
    pred = model.predict(input_scaled)[0]
    proba = model.predict_proba(input_scaled)[0][pred]

    if pred == 1:
        st.success(f"🚢 Predicted to SURVIVE with probability {proba:.2f}")
    else:
        st.error(f"☠️ Predicted NOT to survive with probability {proba:.2f}")
