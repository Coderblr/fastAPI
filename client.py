import random
import requests

SOURCE_IDS = ["Y2", "Y4", "Y5", "U7"]
VILLAGE_CODES = ["556949", "50987", "8765", "64335"]
CUSTOMER_TYPES = ["010203", "020304", "030405"]
CROSS_BORDER_RISKS = ["ZZ", "AA", "BB"]
GENDERS = ["F", "M", "O"]
DOCUMENT_TYPES = ["49", "50", "51"]
OCCUPATION_CODES = ["0301", "0302", "0303"]
TITLES = ["01", "02", "03", "04", "05"]
FIRST_NAMES = ["RAJESH", "PRIYA", "AMIT", "SUNITA", "VIKASH", "MEERA", "SUNIL", "KAVITA"]
LAST_NAMES = ["SHARMA", "PATEL", "SINGH", "KUMAR", "GUPTA", "VERMA", "AGARWAL", "JAIN"]
CITIES = ["MUM", "DEL", "BLR", "HYD", "CHN", "KOL", "AHM", "PUN"]
STATES = ["MH", "DL", "KA", "TS", "TN", "WB", "GJ", "UP"]
DISTRICTS = ["001", "002", "003", "004", "005"]
PIN_CODES = ["400001", "110001", "560001", "500001", "600001", "700001"]
EDUCATION_CODES = ["01", "02", "03", "04"]
MARITAL_STATUS = ["S", "M", "D", "W"]
RELATIVE_CODES = ["F", "S", "G"]

def generate_random_date(start_year=1970, end_year=2005):
    year = random.randint(start_year, end_year)
    month = random.randint(1, 12)
    day = random.randint(1, 28)
    return f"{day:02d}{month:02d}{year}"

def generate_random_mobile():
    return f"91{random.randint(7000000000, 9999999999)}"

def generate_payload():
    return {
        "SOURCE_ID": random.choice(SOURCE_IDS),
        "VILLAGE_CODE": random.choice(VILLAGE_CODES),
        "CUSTOMER_TYPE": random.choice(CUSTOMER_TYPES),
        "CROSS_BORDER_RISK": random.choice(CROSS_BORDER_RISKS),
        "GENDER_CODE": random.choice(GENDERS),
        "OVD_KYC_DOCUMENT_TYPE": random.choice(DOCUMENT_TYPES),
        "OCCUPATION_CODE": random.choice(OCCUPATION_CODES),
        "TITLE": random.choice(TITLES),
        "FIRST_NAME": random.choice(FIRST_NAMES),
        "LAST_NAME": random.choice(LAST_NAMES),
        "CITY_CODE": random.choice(CITIES),
        "STATE": random.choice(STATES),
        "DISTRICT_CODE": random.choice(DISTRICTS),
        "PIN_CODE": random.choice(PIN_CODES),
        "EDUCATION_CODE": random.choice(EDUCATION_CODES),
        "MARITAL_STATUS": random.choice(MARITAL_STATUS),
        "RELATIVE_CODE": random.choice(RELATIVE_CODES),
        "MOBILE_NUMBER": generate_random_mobile(),
        "DATE_OF_BIRTH": generate_random_date(),
        "REQUEST_REFERENCE_NUMBER": "SBIY" + str(random.randint(1000000000, 9999999999))
    }

def main():
    url = "http://127.0.0.1:8000/customers/AOF2personal/cifCreation/"
    payload = generate_payload()
    print("Sending payload:")
    print(payload)
    response = requests.post(url, json=payload)
    print("Response from server:")
    print(response.json())

if __name__ == "__main__":
    main()
