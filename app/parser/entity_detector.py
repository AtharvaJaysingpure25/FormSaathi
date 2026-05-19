import re


def detect_entities(grouped_text):

    extracted_entities = {}

    for line in grouped_text:

        text = line["text"]

        # DATE DETECTION
        date_match = re.search(
            r"\b\d{2}/\d{2}/\d{4}\b",
            text
        )

        if date_match:

            extracted_entities["Date Of Birth"] = (
                date_match.group()
            )

        # EMAIL DETECTION
        email_match = re.search(
            r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}",
            text
        )

        if email_match:

            extracted_entities["Email"] = (
                email_match.group()
            )

        # PHONE NUMBER DETECTION
        phone_match = re.search(
            r"\b\d{10}\b",
            text
        )

        if phone_match:

            extracted_entities["Phone Number"] = (
                phone_match.group()
            )

        # STUDENT / ACCOUNT / ID NUMBER
        id_match = re.search(
            r"\b[A-Z0-9]{8,}\b",
            text
        )

        if id_match:

            extracted_entities["ID Number"] = (
                id_match.group()
            )

    return extracted_entities