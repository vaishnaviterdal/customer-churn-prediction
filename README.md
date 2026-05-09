# Telecom Customer Churn Prediction

## About the Project
This project focuses on predicting customer churn in a telecom company using Machine Learning.  
The goal is to identify customers who are likely to leave the service based on factors such as tenure, contract type, monthly charges, payment method, and demographic information.

I built this project to understand the complete workflow of a data science project — from data preprocessing and analysis to model building and deployment using Streamlit.

---

## Problem Statement
Customer churn directly affects company revenue.  
If businesses can identify customers who are likely to leave early, they can take steps such as offers, support, or retention campaigns to reduce customer loss.

This project attempts to predict whether a customer will churn or not.

---

## Dataset Features
The dataset contains customer-related information such as:

- Age
- Gender
- Tenure
- Monthly Charges
- Total Charges
- Contract Type
- Payment Method
- Churn Status

---

## Steps Performed

### 1. Data Cleaning
- Removed unnecessary columns like CustomerID
- Checked for missing values
- Handled categorical data using encoding techniques

### 2. Exploratory Data Analysis (EDA)
Performed analysis to understand patterns affecting churn.

Some observations:
- Customers with low tenure were more likely to churn
- Customers paying higher monthly charges showed higher churn rates
- Long-term contracts reduced churn significantly

### 3. Model Building
Used Logistic Regression for prediction.

Initially, the model showed poor performance in detecting churn customers because the dataset contained more non-churn customers than churn customers.

To improve this, class balancing was applied during model training, which improved churn detection performance.

### 4. Model Evaluation
The model was evaluated using:
- Accuracy
- Precision
- Recall
- F1-score

Special attention was given to recall because correctly identifying churn customers is more important than simply achieving high accuracy.

---

## Streamlit Web Application
A simple Streamlit application was created where users can:
- Enter customer information
- Predict whether the customer is likely to churn

---

## Technologies Used
- Python
- Pandas
- NumPy
- Scikit-learn
- Streamlit
- Pickle

---

## Project Structure

```text
customer-churn-prediction/
│
├── app.py
├── model.pkl
├── Customer_churn.ipynb
├── requirements.txt
└── README.md
