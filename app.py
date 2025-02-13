import streamlit as st
import joblib  # For loading the trained model
import pandas as pd

# Load trained model
model = joblib.load("beam_failure_model.pkl")  # Ensure this file exists

# Streamlit UI
st.title("Beam Failure Prediction AI")
st.write("Enter the details below to predict failure:")

# User inputs
applied_load = st.number_input("Applied Load (kN)")
span_length = st.number_input("Span Length (m)")
material_strength = st.number_input("Material Strength (MPa)")
reinforcement_area = st.number_input("Reinforcement Area (cm²)")

# Prediction
if st.button("Predict"):
    input_data = [[applied_load, span_length, material_strength, reinforcement_area]]
    prediction = model.predict(input_data)

    result = "Failure" if prediction[0] == 1 else "No Failure"
    st.subheader(f"Prediction: {result}")
