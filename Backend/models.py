# models.py
from pydantic import BaseModel, Field
from typing import List

# Pydantic schema for each quiz question
class Question(BaseModel):
    question: str = Field(..., example="What is the capital of France?")
    options: List[str] = Field(..., example=["Paris", "London", "Berlin", "Rome"])
    answer: str = Field(..., example="Paris")


# Pydantic schema for the overall quiz output
class QuizOutput(BaseModel):
    title: str = Field(..., example="French Geography Quiz")
    summary: str = Field(..., example="A short quiz about France and its geography.")
    questions: List[Question]


# Request schema for the POST /generate_quiz endpoint
class QuizRequest(BaseModel):
    url: str = Field(..., example="https://en.wikipedia.org/wiki/France")
