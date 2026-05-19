import re


FIELD_ALIASES = {

    # Name
    "name": "Full Name",
    "full name": "Full Name",

    # DOB
    "dob": "Date Of Birth",
    "d.o.b": "Date Of Birth",
    "date of birth": "Date Of Birth",
    "birth date": "Date Of Birth",

    # Mobile
    "mobile": "Mobile Number",
    "phone": "Mobile Number",
    "mobile number": "Mobile Number",

    # Aadhaar
    "aadhaar": "Aadhaar Number",
    "aadhar": "Aadhaar Number",

    # PAN
    "pan": "PAN Number",

    # Email
    "email": "Email Address",

    # IFSC
    "ifsc": "IFSC Code",

    # Account
    "account number": "Account Number"
}


def normalize_field_name(field_name):

    cleaned = field_name.strip().lower()

    cleaned = re.sub(r"[:\-]", "", cleaned)

    return FIELD_ALIASES.get(
        cleaned,
        field_name
    )