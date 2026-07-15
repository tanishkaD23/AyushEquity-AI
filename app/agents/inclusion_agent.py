import joblib
import pandas as pd

# --------------------------------
# Load Trained Model
# --------------------------------

model = joblib.load("app/models/inclusion_model.pkl")


class InclusionAgent:

    def predict(self, citizen_data):

        df = pd.DataFrame([citizen_data])

        prediction = model.predict(df)[0]

        confidence = model.predict_proba(df)[0].max() * 100

        if prediction == 1:
            result = "Eligible"
        else:
            result = "Not Eligible"

        return {
            "Prediction": result,
            "Confidence": f"{confidence:.2f}%"
        }


# --------------------------------
# Example
# --------------------------------

if __name__ == "__main__":

    sample = {
        "Age": 45,
        "Gender": 1,
        "Monthly_Income": 5000,
        "Annual_Income": 60000,
        "Family_Size": 5,
        "BPL_Status": 1,
        "Ration_Card": 1,
        "Disability": 0,
        "Chronic_Disease": 1,
        "PMJAY_Registered": 1,
        "Occupation": 2,
        "State": 3
    }

    agent = InclusionAgent()

    result = agent.predict(sample)

    print("=" * 50)
    print("INCLUSION AGENT")
    print("=" * 50)
    print(result)