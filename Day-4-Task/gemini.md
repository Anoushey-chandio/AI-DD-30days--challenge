# Role: Senior Python AI Engineer

**Objective:** Build a "PDF Summarizer & Quiz Generator Agent" using Streamlit and the `openai-agents` SDK.

## 1. Project Overview
The goal is to develop a minimal, web-based study assistant that:

* Summarizes PDF documents
* Generates quizzes (MCQs or mixed style)
* Uses tools for PDF text extraction

* **UI:** Streamlit (Interactive, minimal interface)
* **Model:** Google Gemini model named `gemini-2.0-flash-001` (via OpenAI Agents SDK)
* **Tools:** PyPDF extraction functions
* **Execution:** Zero-bloat, deterministic agent logic

---

## 2. Critical Technical Constraints
**You must adhere to the following strict configuration rules:**

1. **Zero-Bloat Protocol (CRITICAL)**
    * **Do NOT write extra code.** No extra features, comments, or helpers.
    * Focus strictly on the integration: Streamlit UI ↔ Agent ↔ Tools.
    * **No “Hallucinated” Features:** Do not invent SDK functions or classes.

2. **API Configuration**
    * Use the **OpenAI Agents SDK** (NOT the standard `openai` library)
    * **Base URL:** `https://generativelanguage.googleapis.com/v1beta/openai/`
    * **API Key:** Load from environment variable `GEMINI_API_KEY`
    * **Model:** Pass as string `"gemini-2.0-flash-001"` to Agent

3. **SDK Specificity**
    * Follow exact syntax from `openai-agents` documentation
    * Tools must use SDK decorators (`@tool` or `FunctionTool`)
    * Do not use undocumented attributes, classes, or agents

4. **Error Recovery Protocol**
    * On `SyntaxError`, `ImportError`, or `AttributeError`:
        * **STOP immediately**
        * Re-run `get-library-docs("openai-agents")` to verify correct syntax

5. **Dependency Management**
    * Use `uv` for package installation:

    ```
    uv add streamlit pypdf openai-agents python-dotenv
    ```

    * Do not reinstall if already present
    * Ensure dependencies appear inside `pyproject.toml`

---

## 3. Architecture & File Structure

*Note: Current directory is root.*

```text
.
├── .env                   # Environment variables
├── tools.py               # PDF extraction functions (SDK format)
├── agent.py               # Agent configuration & tool binding
├── app.py                 # Streamlit UI logic
├── uploads/               # Folder for user-uploaded PDFs
└── pyproject.toml         # UV config

4. Implementation Steps

Follow this exact logical flow. Do not skip steps.

Step 1: Documentation & Pattern Analysis

Before writing any code:

Run MCP tool:

get-library-docs("openai-agents")


Confirm:

How to define tools

How to register tools

How to initialize Agent()

How to pass model as string

Check SDK examples carefully

Step 2: Tool Implementation (tools.py)

Create two PyPDF-based tools following SDK format:

extract_pdf_text(file_path: str)

Reads full PDF

Returns plain text

load_pdf_for_quiz(file_path: str)

Reads PDF

Returns raw text for quiz generation

Rules:

Only PyPDF

No preprocessing

Must follow SDK tool pattern exactly

Step 3: Agent Configuration (agent.py)

Configure agent following SDK pattern:

from dotenv import load_dotenv
load_dotenv()  # Must run before agent creation

from agents import Agent
from tools import extract_pdf_text, load_pdf_for_quiz

agent = Agent(
    name="PDF Summarizer & Quiz Generator",
    instructions=(
        "You summarize PDFs and generate quizzes. "
        "Use tools to extract PDF text. Summaries must be concise. "
        "Quizzes may be MCQs or mixed format."
    ),
    tools=[extract_pdf_text, load_pdf_for_quiz],
    model="gemini-2.0-flash-001",
)


Model must be string "gemini-2.0-flash-001"

Do not pass api_key or base_url to Agent

No extra instructions

Step 4: UI & Application Logic (app.py)

Minimal Streamlit workflow:

Upload PDF → saved in /uploads

"Summarize PDF" button → extract PDF text → agent → display summary

"Generate Quiz" button → load PDF text → agent → display quiz

Rules:

No streaming mode

Only display results using st.write()

No session persistence

No extra UI elements

Step 5: Environment & Dependencies

.env must contain:

GEMINI_API_KEY=YOUR_KEY_HERE


pyproject.toml must include:

streamlit
pypdf
openai-agents
python-dotenv


Do not reinstall packages if already present

5. Testing Scenarios

PDF Summarization: Upload PDF → Click "Summarize PDF" → Agent returns summary

Quiz Generation: Upload PDF → Click "Generate Quiz" → Agent produces MCQs/mixed quiz

Minimal UI: Only buttons and output; no extra formatting

Tool Verification: Agent must always use PyPDF tools to read PDF