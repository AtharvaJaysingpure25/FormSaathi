def merge_line_tokens(lines):

    merged_lines = []

    for line in lines:

        merged_text = " ".join(
            item["text"]
            for item in line
        )

        merged_lines.append({
            "text": merged_text,
            "tokens": line
        })

    return merged_lines