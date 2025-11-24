from pydantic import BaseModel, Field
from pypdf import PdfReader
from agents.tool import function_tool
import os

# Define Pydantic models for tool input schemas
class FilePathInput(BaseModel):
    file_path: str = Field(..., description="The path to the PDF file")

@function_tool
def extract_pdf_text(file_path: FilePathInput) -> str:
    """
    Reads an entire PDF and returns its plain text content.
    """
    try:
        reader = PdfReader(file_path.file_path)
        text = ""
        for page in reader.pages:
            text += page.extract_text() + "\n"
        return text
    except Exception as e:
        return f"Error extracting text from PDF: {e}"

@function_tool
def load_pdf_for_quiz(file_path: FilePathInput) -> str:
    """
    Returns raw PDF text intended specifically for quiz generation.
    """
    try:
        reader = PdfReader(file_path.file_path)
        text = ""
        for page in reader.pages:
            text += page.extract_text() + "\n"
        return text
    except Exception as e:
        return f"Error loading PDF for quiz generation: {e}"
