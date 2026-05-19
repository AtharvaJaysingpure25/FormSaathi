import re


COMMON_FIELD_LABELS = [
    "name",
    "dob",
    "date of birth",
    "phone",
    "mobile",
    "email",
    "address",
    "account number",
    "ifsc",
    "aadhaar",
    "pan"
]


def clean_text(text):

    text = text.strip()

    text = re.sub(r"[:\-]", "", text)

    return text


def find_nearest_right_text(label_item, ocr_data):

    label_x1 = label_item["bbox"][2]
    label_y = label_item["bbox"][1]

    best_candidate = None
    min_distance = float("inf")

    for item in ocr_data:

        if item == label_item:
            continue

        candidate_x = item["bbox"][0]
        candidate_y = item["bbox"][1]

        # Same line check
        if abs(candidate_y - label_y) < 30:

            # Must be right side
            if candidate_x > label_x1:

                distance = candidate_x - label_x1

                if distance < min_distance:
                    min_distance = distance
                    best_candidate = item

    return best_candidate


def extract_fields(ocr_data):

    extracted_fields = {}

    for item in ocr_data:

        text = clean_text(item["text"]).lower()

        if text in COMMON_FIELD_LABELS:

            value_item = find_nearest_right_text(item, ocr_data)

            if value_item:

                normalized_key = clean_text(item["text"]).title()
                extracted_fields[normalized_key] = value_item["text"]

    return extracted_fields