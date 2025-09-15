from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

class CustomerRequest(BaseModel):
    SOURCE_ID: str
    VILLAGE_CODE: str
    CUSTOMER_TYPE: str
    CROSS_BORDER_RISK: str
    GENDER_CODE: str
    OVD_KYC_DOCUMENT_TYPE: str
    OCCUPATION_CODE: str
    TITLE: str
    FIRST_NAME: str
    LAST_NAME: str
    CITY_CODE: str
    STATE: str
    DISTRICT_CODE: str
    PIN_CODE: str
    EDUCATION_CODE: str
    MARITAL_STATUS: str
    RELATIVE_CODE: str
    MOBILE_NUMBER: str
    DATE_OF_BIRTH: str
    REQUEST_REFERENCE_NUMBER: Optional[str] = None
    # Add other fields if needed

@app.post("/customers/AOF2personal/cifCreation/")
async def create_cif(request: CustomerRequest):
    # Return fixed mock response with request reference echoed back
    return {
        "CUSTOMER_NUMBER": "85002473610",
        "CIF_CREATION": "033744636",
        "ANNUAL_INCOME": "033744637",
        "ERROR_CODE": "",
        "ERROR_DESCRIPTION": "",
        "RESPONSE_STATUS": "0",
        "RESPONSE_DATE": "29-08-2025 10:30:06",
        "REQUEST_REFERENCE_NUMBER": request.REQUEST_REFERENCE_NUMBER or "N/A"
    }
