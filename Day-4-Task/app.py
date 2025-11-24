# app.py
import streamlit as st
import os
import asyncio
from agents import Runner
from agent import agent  # Import configured agent
from pydantic import BaseModel

# Context to pass uploaded file path to agent
class AppContext(BaseModel):
    uploaded_file_path: str

st.title("PDF Summarizer & Quiz Generator")

# Create uploads directory
UPLOADS_DIR = "uploads"
os.makedirs(UPLOADS_DIR, exist_ok=True)

uploaded_file = st.file_uploader("Upload a PDF file", type=["pdf"])

if uploaded_file is not None:
    file_path = os.path.join(UPLOADS_DIR, uploaded_file.name)
    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())
    st.success(f"File '{uploaded_file.name}' uploaded successfully!")

    context = AppContext(uploaded_file_path=file_path)
    
    col1, col2 = st.columns(2)

    if col1.button("Summarize PDF"):
        st.info("Generating summary...")
        try:
            # Pass prompt to agent; agent will use extract_pdf_text tool
            prompt_summarize = f"Summarize the PDF at path: {file_path}"
            result = asyncio.run(Runner.run(agent, prompt_summarize, context=context))
            st.subheader("Summary")
            st.write(result.final_output)
        except Exception as e:
            st.error(f"Error generating summary: {e}")

    if col2.button("Generate Quiz"):
        st.info("Generating quiz...")
        try:
            # Pass prompt to agent; agent will use load_pdf_for_quiz tool
            prompt_quiz = f"Generate a quiz (MCQ or mixed format) from the PDF at path: {file_path}"
            result = asyncio.run(Runner.run(agent, prompt_quiz, context=context))
            st.subheader("Quiz")
            st.write(result.final_output)
        except Exception as e:
            st.error(f"Error generating quiz: {e}")
