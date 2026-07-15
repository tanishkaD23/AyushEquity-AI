import joblib
import pandas as pd

# -------------------------------
# Load Model
# -------------------------------

model = joblib.load("app/models/fraud_model.pkl")

encoders = joblib.load("app/models/fraud_label_encoders.pkl")


class FraudAgent:

    def preprocess(self, claim):

        df = pd.DataFrame([claim])

        categorical_columns = [

            "Duplicate_Claim",

            "Disease",

            "Treatment",

            "Hospital_Type",

            "Previous_Fraud"

        ]

        for col in categorical_columns:

            df[col] = encoders[col].transform(df[col])

        return df

    def predict(self, claim):

        df = self.preprocess(claim)

        prediction = model.predict(df)[0]

        probability = model.predict_proba(df)[0].max() * 100

        if prediction == 1:

            status = "Fraud"

            risk = "High"

        else:

            status = "Genuine"

            risk = "Low"

        return {

            "Prediction": status,

            "Risk": risk,

            "Confidence": round(probability,2)

        }


if __name__ == "__main__":

    sample = {

        "Claim_Amount":95000,

        "Package_Amount":70000,

        "Duplicate_Claim":"Yes",

        "Disease":"Heart Disease",

        "Treatment":"Angioplasty",

        "Hospital_Type":"Private",

        "Previous_Fraud":"Yes",

        "Beds":120,

        "Doctors":30,

        "Rating":2.9,

        "Length_of_Stay":6,

        "Claim_Ratio":1.35,

        "High_Claim":1,

        "Fraud_Hospital":1,

        "Doctor_Bed_Ratio":0.25,

        "Claim_Per_Bed":791,

        "Claim_Difference":25000

    }

    agent = FraudAgent()

    result = agent.predict(sample)

    print(result)