from fastapi import FastAPI
import joblib
import pandas as pd
from fastapi import HTTPException
import logging
from app.agents.inclusion_agent import InclusionAgent
from app.agents.fraud_agent import FraudAgent
from app.backend.schemas import InclusionRequest, FraudRequest

from app.backend.schemas import InclusionRequest
inclusion_agent = InclusionAgent()

fraud_agent = FraudAgent()
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)
app = FastAPI(

    title="AyushEquity AI",

    version="1.0",

    description="AI-powered Healthcare Inclusion & Fraud Detection"

)


# ---------------------------------
# Home API
# ---------------------------------

@app.get("/")

def home():

    return {

        "Project": "AyushEquity AI",

        "Status": "Running",

        "Version": "1.0"

    }

# ---------------------------------
# Health Check
# ---------------------------------


@app.get("/health")

def health():

    return {

        "Server": "Healthy",

        "Database": "Connected",

        "Models": "Loaded"

    }
# -----------------------------------
# Inclusion Prediction API
# -----------------------------------
@app.post("/predict/inclusion")
def predict_inclusion(data: InclusionRequest):

    try:

        df = pd.DataFrame([data.model_dump()])

        categorical_columns = [
            "Gender",
            "BPL_Status",
            "Ration_Card",
            "Disability",
            "Chronic_Disease",
            "PMJAY_Registered",
            "Occupation",
            "State"
        ]

        for col in categorical_columns:

            value = df[col].iloc[0]

            if value not in encoders[col].classes_:
                raise HTTPException(
                    status_code=400,
                    detail=f"Invalid value '{value}' for {col}"
                )

            df[col] = encoders[col].transform(df[col])

        result = inclusion_agent.predict(data.model_dump())

        return result

        confidence = inclusion_model.predict_proba(df)[0].max() * 100

        result = "Eligible" if prediction == 1 else "Not Eligible"

        logging.info("Prediction generated successfully.")

        return {
            "Prediction": result,
            "Confidence": f"{confidence:.2f}%"
        }

    except HTTPException:
        raise

    except Exception as e:

        logging.error(str(e))

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )
    
@app.post("/predict/fraud")
def predict_fraud(data: FraudRequest):

    try:

        result = fraud_agent.predict(
            data.model_dump()
        )

        return result

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )  
# -----------------------------------
# Load Inclusion Model
# -----------------------------------

inclusion_model = joblib.load(
    "app/models/inclusion_model.pkl"
)

encoders = joblib.load(
    "app/models/label_encoders.pkl"
)

