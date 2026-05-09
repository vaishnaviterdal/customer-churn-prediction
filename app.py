import streamlit as st
import pickle
import numpy as np

# Load model
model = pickle.load(open("model.pkl", "rb"))

st.title("Telecom Customer Churn Prediction System")
st.write("Predict whether a customer is likely to leave the telecom service.")
st.write("Enter customer details")

# Inputs
age = st.number_input("Age", min_value=0)

tenure = st.number_input("Tenure", min_value=0)

monthly_charges = st.number_input("Monthly Charges", min_value=0.0)

total_charges = st.number_input("Total Charges", min_value=0.0)

contract_one_year = st.selectbox("One Year Contract", ["Yes","No"])

contract_two_year = st.selectbox("Two Year Contract", ["Yes","No"])

payment_credit = st.selectbox("Payment: Credit Card", ["Yes","No"])

payment_electronic = st.selectbox("Payment: Electronic Check", ["Yes","No"])

payment_mailed = st.selectbox("Payment: Mailed Check", ["Yes","No"])

gender = st.selectbox("Gender", ["Male", "Female", "Other"])

# Prediction
if st.button("Predict"):

    input_data = np.array([[age,
                        tenure,
                        monthly_charges,
                        total_charges,

                        1 if contract_one_year == "Yes" else 0,

                        1 if contract_two_year == "Yes" else 0,

                        1 if payment_credit == "Yes" else 0,

                        1 if payment_electronic == "Yes" else 0,

                        1 if payment_mailed == "Yes" else 0,

                        1 if gender == "Male" else 0,

                        1 if gender == "Other" else 0
                        ]])

    prediction = model.predict(input_data)

    if prediction[0] == 1:
        st.error("⚠️ Customer is likely to churn.")

    else:
        st.success("✅ Customer is likely to stay.")