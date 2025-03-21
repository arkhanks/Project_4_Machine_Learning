import streamlit as st
import pandas as pd
import numpy as np
import pickle

# Load trained models
rf_reg = pickle.load(open("inspection_score_model.pkl", "rb"))
rf_clf = pickle.load(open("risk_category_model.pkl", "rb"))

# App Title
st.title("🏢 Restaurant Inspection Score & Risk Prediction")

# User Inputs for Violation Data
st.sidebar.header("📋 Input Violation Data")

# Get the feature names the model was trained on
feature_names = rf_reg.feature_names_in_

# Create input fields dynamically based on feature names
input_values = {}

for feature in feature_names:
    if feature in ['business_id', 'inspection_id']:  # IDs should allow large numbers
        input_values[feature] = st.sidebar.number_input(f"Enter value for {feature}:", max_value=999999, step=1)
    elif feature in ['business_latitude', 'business_longitude']:  # Allow decimals for coordinates
        input_values[feature] = st.sidebar.number_input(f"Enter value for {feature}:", min_value=-180.0, max_value=180.0, step=0.0001)
    else:  # General numerical inputs with no upper restriction
        input_values[feature] = st.sidebar.number_input(f"Enter value for {feature}:", min_value=0, step=1)

# Create input data as a DataFrame with correct feature names
input_data = pd.DataFrame([input_values], columns=feature_names)

# Predict Inspection Score
score_prediction = rf_reg.predict(input_data)[0]

# Predict Risk Category
risk_prediction = rf_clf.predict(input_data)[0]

# Display Predictions
st.subheader("📊 Prediction Results")
st.write(f"🔢 **Predicted Inspection Score:** {round(score_prediction, 2)}")
st.write(f"⚠️ **Predicted Risk Category:** {risk_prediction}")

# Display Alerts
if score_prediction < 70:
    st.error("🚨 Warning: The predicted score is low, indicating a failed inspection!")
elif score_prediction < 85:
    st.warning("⚠️ The predicted score suggests a moderate risk of violations.")
else:
    st.success("✅ The predicted score suggests good compliance with food safety regulations.")

if risk_prediction == "High Risk":
    st.error("⚠️ This establishment falls into the HIGH-RISK category!")
elif risk_prediction == "Moderate Risk":
    st.warning("🔶 This establishment falls into the MODERATE-RISK category.")
else:
    st.success("✅ This establishment falls into the LOW-RISK category.")

