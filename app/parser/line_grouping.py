def group_tokens_into_lines(ocr_data, y_threshold=35):

    if not ocr_data:
        return []

    # Sort top-to-bottom
    sorted_data = sorted(
        ocr_data,
        key=lambda x: x["bbox"][1]
    )

    lines = []
    current_line = []

    current_y = sorted_data[0]["bbox"][1]

    for item in sorted_data:

        y = item["bbox"][1]

        # Same line
        if abs(y - current_y) < y_threshold:

            current_line.append(item)

        else:

            lines.append(current_line)

            current_line = [item]

            current_y = y

    if current_line:
        lines.append(current_line)

    # Sort each line left-to-right
    for line in lines:
        line.sort(key=lambda x: x["bbox"][0])

    return lines