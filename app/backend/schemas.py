from pydantic import BaseModel
from enum import Enum


# =====================================================
# ENUMS FOR INCLUSION MODEL
# =====================================================

class GenderEnum(str, Enum):
    Male = "Male"
    Female = "Female"


class YesNoEnum(str, Enum):
    Yes = "Yes"
    No = "No"


class RationCardEnum(str, Enum):
    APL = "APL"
    BPL = "BPL"
    PHH = "PHH"
    AAY = "AAY"


class OccupationEnum(str, Enum):
    Farmer = "Farmer"
    Labourer = "Labourer"
    Driver = "Driver"
    Tailor = "Tailor"
    Student = "Student"
    Shopkeeper = "Shopkeeper"
    Teacher = "Teacher"
    Carpenter = "Carpenter"
    Electrician = "Electrician"
    Unemployed = "Unemployed"


class StateEnum(str, Enum):
    Madhya_Pradesh = "Madhya Pradesh"
    Maharashtra = "Maharashtra"
    Uttar_Pradesh = "Uttar Pradesh"
    Rajasthan = "Rajasthan"
    Gujarat = "Gujarat"
    Bihar = "Bihar"
    Odisha = "Odisha"
    Chhattisgarh = "Chhattisgarh"
    Jharkhand = "Jharkhand"
    West_Bengal = "West Bengal"


# =====================================================
# INCLUSION REQUEST
# =====================================================

class InclusionRequest(BaseModel):

    Age: int

    Gender: GenderEnum

    Monthly_Income: int

    Annual_Income: int

    Family_Size: int

    BPL_Status: YesNoEnum

    Ration_Card: RationCardEnum

    Disability: YesNoEnum

    Chronic_Disease: YesNoEnum

    PMJAY_Registered: YesNoEnum

    Occupation: OccupationEnum

    State: StateEnum


# =====================================================
# ENUMS FOR FRAUD MODEL
# =====================================================

class HospitalTypeEnum(str, Enum):
    Government = "Government"
    Private = "Private"


class DiseaseEnum(str, Enum):
    Cancer = "Cancer"
    Dengue = "Dengue"
    Malaria = "Malaria"
    Diabetes = "Diabetes"
    Heart_Disease = "Heart Disease"
    Kidney_Disease = "Kidney Disease"
    Asthma = "Asthma"
    COVID19 = "COVID-19"
    Tuberculosis = "Tuberculosis"
    Pneumonia = "Pneumonia"


class TreatmentEnum(str, Enum):
    Surgery = "Surgery"
    Dialysis = "Dialysis"
    Chemotherapy = "Chemotherapy"
    Angioplasty = "Angioplasty"
    ICU = "ICU"
    General_Medicine = "General Medicine"
    Consultation = "Consultation"
    Delivery = "Delivery"
    Vaccination = "Vaccination"
    Physiotherapy = "Physiotherapy"


# =====================================================
# FRAUD REQUEST
# =====================================================

class FraudRequest(BaseModel):

    Claim_Amount: float

    Package_Amount: float

    Duplicate_Claim: YesNoEnum

    Disease: DiseaseEnum

    Treatment: TreatmentEnum

    Hospital_Type: HospitalTypeEnum

    Previous_Fraud: YesNoEnum

    Beds: int

    Doctors: int

    Rating: float

    Length_of_Stay: int

    Claim_Ratio: float

    High_Claim: int

    Fraud_Hospital: int

    Doctor_Bed_Ratio: float

    Claim_Per_Bed: float

    Claim_Difference: float