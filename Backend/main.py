# main.py
from fastapi import FastAPI, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
import json

from database import SessionLocal, init_db, Quiz
from scraper import scrape_wikipedia
from llm_quiz_generator import generate_quiz_from_text

init_db()

app = FastAPI(title="AI Wiki Quiz Generator")

# Allow frontend to connect
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Dependency for DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/generate_quiz")
def generate_quiz(payload: dict, db: Session = Depends(get_db)):
    url = payload.get("url")
    if not url:
        raise HTTPException(status_code=400, detail="URL is required")

    scraped = scrape_wikipedia(url)
    quiz_data = generate_quiz_from_text(scraped["content"], scraped["title"])

    # Save to database
    quiz_record = Quiz(
        url=url,
        title=quiz_data["title"],
        scraped_content=scraped["content"],
        full_quiz_data=json.dumps(quiz_data)
    )
    db.add(quiz_record)
    db.commit()
    db.refresh(quiz_record)

    return quiz_data


@app.get("/history")
def get_history(db: Session = Depends(get_db)):
    quizzes = db.query(Quiz).all()
    return [
        {"id": q.id, "url": q.url, "title": q.title, "date_generated": q.date_generated}
        for q in quizzes
    ]


@app.get("/quiz/{quiz_id}")
def get_quiz(quiz_id: int, db: Session = Depends(get_db)):
    quiz = db.query(Quiz).filter(Quiz.id == quiz_id).first()
    if not quiz:
        raise HTTPException(status_code=404, detail="Quiz not found")

    return json.loads(quiz.full_quiz_data)
