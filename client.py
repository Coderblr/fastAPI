# nonpayload.py
import random
import string
from datetime import datetime

def generate_non_cif_payload():
    mobile_number = str(random.randint(6000000000, 9999999999))
    first_id_number = str(random.randint(100000, 999999))  
    email_prefix = ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))
    email_id = f"{email_prefix}@gmail.com"
    domestic_risk = random.choice(["00", "09"])
    cross_border_risk = random.choice(["00", "09"])
    today_date = datetime.today().strftime("%d%m%Y")  
    payload = {
        "SOURCE_ID": "IN",
        "REQUEST_TELLER_ID": "8901",
        "REQUEST_AUTH_ID": "103",
        "BRANCH_CODE": "00437",
        "CUSTOMER_TYPE": "021703",
        "CUSTOMER_TYPE_2": "021703",
        "NAME_OF_THE_ENTITY": "MOHIT ENTERPRISE",
        "THRESHOLD_LIMIT": "100000",
        "ADDRESS_LINE_1": "Belapur ",
        "ADDRESS_LINE_2": "Nerul",
        "ADDRESS_LINE_3": "Sanpada",
        "DISTRICT_CODE": "603",
        "HOME_BRANCH": "00437",
        "SUB_DISTRICT": "99999",
        "VILLAGE_CODE": "803339",
        "PIN_CODE": "600001",
        "MOBILE_NUMBER": mobile_number,
        "NATIONALITY": "IN",
        "FIRST_ID_NUMBER": first_id_number,
        "FIRST_ID_TYPE": "66",
        "ID_ISSUE_DATE": today_date,
        "DOMESTIC_RISK": domestic_risk,
        "CROSS_BORDER_RISK": cross_border_risk,
        "COUNTRY_OF_RISK": "BB",
        "COUNTRY": "IN",
        "STATE": "33",
        "CITY_CODE": "600",
        "EMAIL_ID": email_id,
        "CUSTOMER_EVALUATION_REQUIRED": "N",
        "BSR_ORGANISATION_CODE": "33",
        "ISD_CODE": "91",
        "TFN_INDICATOR": "0",
        "INDUSTRY_CLASSIFICATION": "17",
        "BUSINESS_SECTOR_CODE": "300",
        "DATE_OF_INCORPORATION_OR_FORMATION": "15101974",
        "DATE_OF_COMMENCEMENT": "09112023",
        "CIS_ORGANISATION_CODE": "34",
        "CIN": "U65999DL1998PTC09384",
        "CONSENT_FOR_DATA_SHARING": "N",
        "CONSENT_DATE": "04072025",
        "PLACE_OF_INCORPORATION_OR_FORMATION": "Chennai",
        "RMME_ID": "99",
        "RMME_SUB_ID": "9",
        "SOURCE_OF_FUNDS": "01",
        "FORM60_OR_PAN": "F",
        "TURNOVER": "100000",
        "FORM60_SUBMISSION_DATE": "23062025",
        "TRANSACTION_DATE": "23072025",
        "AGRICULTURAL_INCOME": "877",
        "OTHER_THAN_AGRICULTURAL_INCOME": "787687",
        "PAN_APPLIED_FLAG": "N",
        "CONST_TYPE": "A",
        "ID_PROOF": "03",
        "AD_PROOF": "03",
        "LOCAL_LINE_1": "Test Line 1",
        "LOCAL_LINE_2": "Test Line 2",
        "LOCAL_LINE_3": "Test Line 3",
        "LOCAL_CITY_CODE": "600",
        "LOCAL_PIN_CODE": "600001",
        "LOCAL_STATE_CODE": "33",
        "LOCAL_DISTRICT_CODE": "603",
        "LOCAL_SUB_DISTRICT_CODE": "99999",
        "LOCAL_VILLAGE": "803339",
        "LOCAL_COUNTRY_CODE": "IN",
        "ID_TYPE_1": "66"
    }

    return payload


# main.py
from fastapi import FastAPI
from nm import generate_non_cif_payload

app = FastAPI()

@app.post("/noncif/account")
def create_non_cif_account():
    payload = generate_non_cif_payload()
    return {"status": "success", "data": payload}

