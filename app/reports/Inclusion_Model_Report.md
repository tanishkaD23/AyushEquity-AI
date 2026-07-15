# AyushEquity AI - Inclusion Prediction Model Report

## Project Overview

The Inclusion Prediction Model is designed to identify whether a citizen is eligible for the Ayushman Bharat PM-JAY scheme based on demographic, socioeconomic, and health-related information.

---

## Dataset Information

Dataset Name: beneficiaries.csv

Total Records: 10,000

Total Features: 12

Target Variable:
Eligible (Yes / No)

---

## Selected Features

- Age
- Gender
- Monthly Income
- Annual Income
- Family Size
- BPL Status
- Ration Card
- Disability
- Chronic Disease
- PMJAY Registered
- Occupation
- State

---

## Machine Learning Algorithms Used

1. Logistic Regression
2. Decision Tree
3. Random Forest
4. XGBoost

---

## Best Performing Model

Decision Tree

Accuracy: 99.95%

---

## Evaluation Metrics

- Accuracy
- Precision
- Recall
- F1 Score
- Confusion Matrix

Detailed metrics are available in:

app/reports/model_metrics.json

---

## Workflow

Beneficiary Data

↓

Feature Selection

↓

Data Preprocessing

↓

Train-Test Split

↓

Model Training

↓

Model Evaluation

↓

Save Best Model

↓

Prediction

---

## Output

Prediction:
Eligible / Not Eligible

Confidence Score:
0 - 100%

---

## Future Improvements

- SHAP Explainable AI
- Real Government Dataset
- Hyperparameter Tuning
- Deep Learning Model
- Live API Prediction
- Blockchain Integration
- Agentic AI Workflow

---

## Developed For

AyushEquity AI

AI-powered Healthcare Inclusion & Fraud Detection Platform