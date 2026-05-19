import os
import cv2
import pytesseract

from pdf2image import convert_from_path

from app.utils.image_utils import preprocess_image


print("NEW OCR ENGINE LOADED")


TEMP_IMAGE_DIR = "data/temp/pdf_pages"

os.makedirs(TEMP_IMAGE_DIR, exist_ok=True)


def process_single_image(image_path):

    processed = preprocess_image(image_path)

    rgb = cv2.cvtColor(
        processed,
        cv2.COLOR_GRAY2RGB
    )

    custom_config = r'--oem 3 --psm 6'

    data = pytesseract.image_to_data(
        rgb,
        config=custom_config,
        output_type=pytesseract.Output.DICT
    )

    extracted_data = []

    n_boxes = len(data["text"])

    for i in range(n_boxes):

        text = data["text"][i].strip()

        confidence = int(
            float(data["conf"][i])
        )

        if text == "":
            continue

        if confidence < 40:
            continue

        if not any(char.isalnum() for char in text):
            continue

        if len(text) <= 2 and confidence < 70:
            continue

        x = data["left"][i]
        y = data["top"][i]
        w = data["width"][i]
        h = data["height"][i]

        extracted_data.append({

            "text": text,

            "bbox": [
                x,
                y,
                x + w,
                y + h
            ],

            "confidence": confidence
        })

    return {

        "ocr_data": extracted_data,

        "image": rgb
    }


def extract_text_and_boxes(file_path):

    extension = os.path.splitext(
        file_path
    )[1].lower()

    all_results = []

    final_image = None

    # IMAGE FILES
    if extension in [
        ".jpg",
        ".jpeg",
        ".png"
    ]:

        result = process_single_image(
            file_path
        )

        all_results.extend(
            result["ocr_data"]
        )

        final_image = result["image"]

    # PDF FILES
    elif extension == ".pdf":

        pages = convert_from_path(
            file_path
        )

        for page_num, page in enumerate(pages):

            temp_img_path = os.path.join(
                TEMP_IMAGE_DIR,
                f"page_{page_num}.jpg"
            )

            page.save(
                temp_img_path,
                "JPEG"
            )

            result = process_single_image(
                temp_img_path
            )

            for item in result["ocr_data"]:

                item["page"] = page_num + 1

            all_results.extend(
                result["ocr_data"]
            )

            if page_num == 0:

                final_image = result[
                    "image"
                ]

    else:
        raise ValueError(
            "Unsupported file format"
        )

    return {

        "ocr_data": all_results,

        "image": final_image
    }