import cv2


def draw_ocr_boxes(image, ocr_data):

    visual = image.copy()

    for item in ocr_data:

        x1, y1, x2, y2 = item["bbox"]

        text = item["text"]

        cv2.rectangle(
            visual,
            (x1, y1),
            (x2, y2),
            (0, 255, 0),
            2
        )

        cv2.putText(
            visual,
            text,
            (x1, y1 - 10),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.5,
            (255, 0, 0),
            1
        )

    return visual