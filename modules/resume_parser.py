"""
modules/resume_parser.py
────────────────────────
Extract plain text from an uploaded PDF resume.
Handles multi-page documents and basic encoding issues.
"""

import io
import PyPDF2
import streamlit as st


def extract_text_from_pdf(uploaded_file) -> str:
    """
    Read a Streamlit UploadedFile object (PDF) and return all text as a string.

    Returns an empty string if extraction fails.
    """
    text = ""
    try:
        pdf_bytes = io.BytesIO(uploaded_file.read())
        reader = PyPDF2.PdfReader(pdf_bytes)

        for page_num, page in enumerate(reader.pages):
            try:
                page_text = page.extract_text()
                if page_text:
                    text += page_text + "\n"
            except Exception as page_err:
                st.warning(f"Could not read page {page_num + 1}: {page_err}")

        # Basic cleanup
        text = text.strip()
        if not text:
            st.error("No text found in PDF. It may be a scanned image-based PDF.")

    except Exception as exc:
        st.error(f"Failed to read PDF: {exc}")

    return text