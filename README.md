# FormSaathi

AI-powered KYC & Bank Account Opening Assistant that extracts information from identity documents and bank forms using OCR + intelligent field mapping.

---

##  Project Overview

FormSaathi is a Document AI pipeline designed to simplify the bank account opening and KYC process.

The system can:

- Upload Aadhaar / PAN / Bank Forms / PDFs
- Perform OCR extraction
- Detect text regions visually
- Group OCR tokens into meaningful lines
- Extract structured fields
- Build a unified KYC profile
- Detect missing KYC fields
- Prepare data for auto-filling bank account opening forms

---

#  Current Workflow

```text
Upload Document
      ↓
OCR Extraction (Tesseract)
      ↓
Bounding Box Detection
      ↓
Line Grouping
      ↓
Text Cleaning & Merging
      ↓
Field Extraction
      ↓
Entity Detection
      ↓
KYC Profile Generation
      ↓
Missing Field Detection
```

---

#  Current Project Structure

```text
formsaathi/
│
├── app/
│   ├── ocr/
│   │   └── ocr_engine.py
│   │
│   ├── parser/
│   │   ├── field_parser.py
│   │   ├── line_grouping.py
│   │   ├── text_cleaner.py
│   │   └── entity_detector.py
│   │
│   ├── kyc/
│   │   ├── autofill_mapper.py
│   │   ├── kyc_schema.py
│   │   └── missing_fields.py
│   │
│   ├── pipeline/
│   │   └── pipeline.py
│   │
│   ├── ui/
│   │   └── gradio_app.py
│   │
│   └── utils/
│       ├── file_handler.py
│       ├── image_utils.py
│       └── visualizer.py
│
├── data/
│   ├── uploads/
│   └── temp/
│
├── run.py
├── requirements.txt
└── README.md
```

---

#  Features Implemented

## OCR Engine

- Tesseract OCR integration
- PDF support using `pdf2image`
- Image preprocessing
- Confidence filtering
- Bounding box extraction

---

## OCR Visualization

- Green boxes → detected OCR regions
- Blue labels → extracted text tokens

This helps debug OCR quality visually.

---

## Intelligent Text Processing

### Line Grouping

Groups nearby OCR tokens into readable lines.

### Token Merging

Combines fragmented OCR text into clean sentences.

---

## Structured Field Extraction

Currently extracts:

- Names
- Dates
- Numbers
- IDs
- Addresses (basic)

---

## KYC Profile Builder

Creates a unified KYC JSON structure:

```json
{
  "customer_name": null,
  "date_of_birth": null,
  "mobile_number": null,
  "email_address": null,
  "aadhaar_number": null,
  "pan_number": null,
  "ifsc_code": null,
  "account_number": null,
  "address": null
}
```

---

## Missing Field Detection

Detects incomplete KYC profiles automatically.

Example:

```json
[
  "pan_number",
  "mobile_number"
]
```

---

#  UI

Built using Gradio.

Current interface supports:

- Image Upload
- PDF Upload
- OCR Visualization
- Structured JSON Output

---

#  Current Status

## Working

- OCR pipeline
- PDF parsing
- Visualization
- Line grouping
- KYC profile generation
- Missing field detection
- Gradio interface

---

## In Progress

- Robust Aadhaar field mapping
- PAN card parsing
- Multi-document merging
- Smart bank form autofill
- Claude API integration
- Form understanding layer

---

#  Final Goal

The final system will:

1. Accept KYC documents + bank forms
2. Understand the form structure
3. Extract user information automatically
4. Auto-fill the bank account opening form
5. Highlight missing fields
6. Support multilingual documents
7. Work as a conversational KYC assistant

---

#  Installation

## Clone Repository

```bash
git clone <your-repo-url>
cd formsaathi
```

---

## Create Virtual Environment

```bash
python -m venv venv
```

Activate:

### Linux / Mac

```bash
source venv/bin/activate
```

### Windows

```bash
venv\Scripts\activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# ▶ Run Project

```bash
python run.py
```

Gradio app launches at:

```text
http://127.0.0.1:7860
```

---

#  Tech Stack

- Python
- OpenCV
- Tesseract OCR
- pdf2image
- Gradio
- Regex + Rule-based NLP

---

#  Upcoming Milestones

- PAN card intelligent parser
- Claude-powered document reasoning
- Bank form template understanding
- Auto-fill engine
- Multi-page KYC memory
- Signature detection
- Production deployment

---

#  Author

Built as part of an AI-powered Document Intelligence & Banking Automation project.
