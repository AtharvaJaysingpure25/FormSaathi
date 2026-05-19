from app.kyc.kyc_schema import KYC_SCHEMA


FIELD_MAPPING = {

    "Full Name": "customer_name",

    "Date Of Birth": "date_of_birth",

    "Mobile Number": "mobile_number",

    "Email Address": "email_address",

    "Aadhaar Number": "aadhaar_number",

    "PAN Number": "pan_number",

    "IFSC Code": "ifsc_code",

    "Account Number": "account_number",

    "Address": "address"
}


def build_kyc_profile(extracted_fields):

    kyc_profile = KYC_SCHEMA.copy()

    for field_name, value in extracted_fields.items():

        mapped_key = FIELD_MAPPING.get(field_name)

        if mapped_key:

            kyc_profile[mapped_key] = value

    return kyc_profile