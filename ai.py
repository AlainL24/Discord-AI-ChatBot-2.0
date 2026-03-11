import ollama
import os
from dotenv import load_dotenv

load_dotenv()

MODEL = os.getenv("OLLAMA_MODEL", "llama3")


def generate_answer(question, sources):

    source_list = "\n".join([s["url"] for s in sources])

    prompt = f"""
Answer the user's question using ONLY the sources provided.

Question:
{question}

Sources:
{source_list}

Rules:
- Prefer the most recent information.
- Do NOT guess.
- If the sources do not contain the answer say:
"I could not find a verified answer at this time."

Provide a clear answer followed by a brief explanation.
"""

    response = ollama.chat(
        model=MODEL,
        messages=[{"role": "user", "content": prompt}]
    )

    return response["message"]["content"]