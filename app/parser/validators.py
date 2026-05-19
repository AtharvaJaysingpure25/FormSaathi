import re


def validate_pan(value):

    pattern = r"^[A-Z]{5}[0-9]{4}[A-Z]$"

    return bool(
        re.match(pattern, value)
    )


def validate_aadhaar(value):

    cleaned = value.replace(" ", "")

    pattern = r"^\d{12}$"

    return bool(
        re.match(pattern, cleaned)
    )


def validate_ifsc(value):

    pattern = r"^[A-Z]{4}0[A-Z0-9]{6}$"

    return bool(
        re.match(pattern, value)
    )