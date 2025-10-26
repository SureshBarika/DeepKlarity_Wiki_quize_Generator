# llm_quiz_generator.py
import os
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import ChatPromptTemplate
from langchain.schema import HumanMessage
from dotenv import load_dotenv
import json

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

def generate_quiz_from_text(article_text: str, title: str):
    """Generate quiz questions and summary from article text."""
    llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash", google_api_key=API_KEY)

    prompt = f"""
    You are an educational quiz generator. Based on the following Wikipedia article:
    Title: {title}

    Article Text:
    {article_text[:5000]}  # limit to avoid token overflow

    Generate a quiz in valid JSON format with the following structure:
    {{
      "title": "string",
      "summary": "short summary of the article",
      "questions": [
        {{
          "question": "string",
          "options": ["A", "B", "C", "D"],
          "answer": "correct option letter"
        }}
      ]
    }}
    """

    response = llm.invoke([HumanMessage(content=prompt)])
    try:
        data = json.loads(response.content)
    except Exception:
        # Try to clean any extra text before JSON
        text = response.content.strip()
        start = text.find('{')
        end = text.rfind('}') + 1
        data = json.loads(text[start:end])
    return data
