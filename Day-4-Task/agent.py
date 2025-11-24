# agent.py
import os
from dotenv import load_dotenv
from openai import AsyncOpenAI
from agents import Agent
from agents.models.openai_chatcompletions import OpenAIChatCompletionsModel
from tools import extract_pdf_text, load_pdf_for_quiz

# 1️⃣ Load environment variables first
load_dotenv()

# 2️⃣ Get API key
gemini_api_key = os.getenv("GEMINI_API_KEY")
if not gemini_api_key:
    raise ValueError("GEMINI_API_KEY environment variable not set in .env")

# 3️⃣ Initialize AsyncOpenAI client for Gemini
openai_client = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)

# 4️⃣ Wrap Gemini model in OpenAIChatCompletionsModel
gemini_model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash-001",  # Make sure this is a valid model
    openai_client=openai_client,
)

# 5️⃣ Configure the Agent
agent = Agent(
    name="PDF Summarizer & Quiz Generator",
    instructions=(
        "You summarize PDFs and generate quizzes. "
        "Use tools to extract PDF text. Summaries must be concise. "
        "Quizzes may be MCQs or mixed format."
    ),
    tools=[extract_pdf_text, load_pdf_for_quiz],
    model=gemini_model,
)
