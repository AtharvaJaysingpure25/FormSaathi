REQUIRED_KYC_FIELDS = [

    "customer_name",

    "date_of_birth",

    "mobile_number",

    "aadhaar_number",

    "pan_number"
]


def detect_missing_fields(kyc_profile):

    missing_fields = []

    for field in REQUIRED_KYC_FIELDS:

        if not kyc_profile.get(field):

            missing_fields.append(field)

    return missing_fields