# database.py
from sqlalchemy import create_engine, Column, Integer, String, DateTime, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime
from dotenv import load_dotenv
import os

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./quiz_history.db")
# Example for PostgreSQL:
# DATABASE_URL = "postgresql+psycopg2://username:password@localhost:5432/ai_quiz"

engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False} if "sqlite" in DATABASE_URL else {}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


class Quiz(Base):
    __tablename__ = "quizzes"
    id = Column(Integer, primary_key=True, index=True)
    url = Column(String, index=True)
    title = Column(String)
    date_generated = Column(DateTime, default=datetime.utcnow)
    scraped_content = Column(Text, nullable=True)
    full_quiz_data = Column(Text, nullable=False)  # Store serialized JSON


def init_db():
    Base.metadata.create_all(bind=engine)
