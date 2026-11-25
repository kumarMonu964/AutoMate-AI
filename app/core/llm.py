import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
GROQ_MODEL = os.getenv(
    "GROQ_MODEL",
    "openai/gpt-oss-20b"
)

if not GROQ_API_KEY:
    raise ValueError("GROQ_API_KEY is missing from .env")

llm  = ChatGroq(
    model = GROQ_MODEL,
    api_key = GROQ_API_KEY,
    temperature = 0
)

