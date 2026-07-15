def explain_prediction(claim):

    reasons = []

    if claim["Duplicate_Claim"] == "Yes":

        reasons.append("Duplicate Claim Detected")

    if claim["Previous_Fraud"] == "Yes":

        reasons.append("Hospital has Previous Fraud History")

    if claim["Claim_Amount"] > claim["Package_Amount"]:

        reasons.append("Claim exceeds Package Amount")

    if claim["Rating"] < 3:

        reasons.append("Low Rated Hospital")

    if claim["Length_of_Stay"] < 1:

        reasons.append("Abnormally Short Hospital Stay")

    if len(reasons) == 0:

        reasons.append("No suspicious pattern found")

    return reasons


if __name__ == "__main__":

    sample = {

        "Claim_Amount":95000,

        "Package_Amount":70000,

        "Duplicate_Claim":"Yes",

        "Previous_Fraud":"Yes",

        "Rating":2.5,

        "Length_of_Stay":0

    }

    explanation = explain_prediction(sample)

    print("\nFraud Reasons")

    for i in explanation:

        print("✔", i)