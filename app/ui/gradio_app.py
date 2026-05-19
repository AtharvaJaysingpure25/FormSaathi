import gradio as gr

from app.utils.file_handler import save_uploaded_file
from app.pipeline.pipeline import process_document


def upload_document(file):

    if file is None:
        return None, None

    # Save uploaded file
    saved_path = save_uploaded_file(file)

    # Run pipeline
    result = process_document(saved_path)

    return (
        result["visualized_image"],
        {
            "grouped_text": result.get("grouped_text"),
            "extracted_fields": result.get("extracted_fields"),
            "detected_entities": result.get("detected_entities"),
            "kyc_profile": result.get("kyc_profile"),
            "missing_fields": result.get("missing_fields")
            
        }
    )


demo = gr.Interface(
    fn=upload_document,

    inputs=gr.File(
        label="Upload Form/Image/PDF"
    ),

    outputs=[
        gr.Image(label="OCR Visualization"),
        gr.JSON(label="Structured Output")
    ],

    title="FormSaathi",
    description="Document AI Pipeline"
)

if __name__ == "__main__":
    demo.launch()