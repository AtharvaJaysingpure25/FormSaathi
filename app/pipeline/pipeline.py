from app.ocr.ocr_engine import extract_text_and_boxes

from app.utils.visualizer import draw_ocr_boxes

from app.parser.field_parser import extract_fields

from app.parser.line_grouping import (
    group_tokens_into_lines
)

from app.parser.text_cleaner import (
    merge_line_tokens
)

from app.parser.entity_detector import (
    detect_entities
)

from app.kyc.autofill_mapper import (
    build_kyc_profile
)

from app.kyc.missing_fields import (
    detect_missing_fields
)


def process_document(file_path):
    print("PROCESS DOCUMENT STARTED")
    # -------------------------
    # OCR
    # -------------------------
    ocr_output = extract_text_and_boxes(
        file_path
    )

    ocr_result = ocr_output["ocr_data"]

    processed_image = ocr_output["image"]
    print("IMAGE CHECK:")
    print(type(processed_image))

    if processed_image is None:
        print("IMAGE IS NONE")
    else:
        print(processed_image.shape)

    # -------------------------
    # Group tokens into lines
    # -------------------------
    grouped_lines = group_tokens_into_lines(
        ocr_result
    )

    # -------------------------
    # Merge line tokens
    # -------------------------
    merged_lines = merge_line_tokens(
        grouped_lines
    )

    # -------------------------
    # Extract label-value fields
    # -------------------------
    fields = extract_fields(
        ocr_result
    )

    # -------------------------
    # Detect entities
    # -------------------------
    detected_entities = detect_entities(
        merged_lines
    )

    # -------------------------
    # Build KYC profile
    # -------------------------
    kyc_profile = build_kyc_profile(
        fields
    )

    # -------------------------
    # Detect missing fields
    # -------------------------
    missing_fields = detect_missing_fields(
        kyc_profile
    )

    # -------------------------
    # Draw OCR boxes
    # -------------------------
    visualized_image = draw_ocr_boxes(
        processed_image,
        ocr_result
    )
    print("RETURNING FINAL OUTPUT")

    print({
        "ocr_data": ocr_result,
        "grouped_text": merged_lines,
        "extracted_fields": fields,
        "detected_entities": detected_entities,
        "kyc_profile": kyc_profile,
        "missing_fields": missing_fields
    }.keys())
    # -------------------------
    # Final output
    # -------------------------
    print(type(visualized_image))
    print(visualized_image.shape)
    return {

        "ocr_data": ocr_result,

        "grouped_text": merged_lines,

        "extracted_fields": fields,

        "detected_entities": detected_entities,

        "kyc_profile": kyc_profile,

        "missing_fields": missing_fields,

        "visualized_image": visualized_image
    }