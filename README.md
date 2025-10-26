# 🧠 DeepSeek ASS AI Quiz App

A full-stack **AI-Powered Quiz Application** built with **React (Vite)** on the frontend and **FastAPI + SQLAlchemy** on the backend.  
The app allows users to take quizzes, submit answers, and view results dynamically — with full data persistence and REST API support.

---

## 📁 Project Structure

```
DeepSeek_ASS_AI_Quiz_App/
│
├── Backend/
│   ├── main.py
│   ├── models.py
│   ├── database.py
│   ├── schemas.py
│   ├── crud.py
│   ├── __init__.py
│   ├── requirements.txt
│   └── venv/
│
├── Frontend/
│   ├── index.html
│   ├── package.json
│   ├── vite.config.js
│   ├── public/
│   └── src/
│       ├── App.jsx
│       ├── main.jsx
│       ├── components/
│       │   ├── QuizCard.jsx
│       │   ├── QuestionForm.jsx
│       │   └── ResultCard.jsx
│       ├── pages/
│       │   ├── Home.jsx
│       │   └── QuizPage.jsx
│       └── styles/
│           └── app.css
│
└── README.md
```

---

## ⚙️ Backend Setup (FastAPI)

### 🪄 Step 1: Navigate to the backend folder
```bash
cd Backend
```

### 🪄 Step 2: Create and activate virtual environment
**Windows:**
```powershell
python -m venv venv
venv\Scripts\Activate.ps1
```

**Mac/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

---

### 🪄 Step 3: Install dependencies
```bash
pip install -r requirements.txt
```

If you don’t have a `requirements.txt`, install manually:
```bash
pip install fastapi uvicorn sqlalchemy pydantic "python-multipart" passlib[bcrypt]
```

---

### 🪄 Step 4: Run the backend server
```bash
uvicorn main:app --reload
```

✅ Server will start on:  
👉 `http://127.0.0.1:8000`

### 🧪 Test in Browser:
- API Docs (Swagger): `http://127.0.0.1:8000/docs`
- API Root: `http://127.0.0.1:8000/`

---

## ⚛️ Frontend Setup (React + Vite)

### 🪄 Step 1: Navigate to frontend folder
```bash
cd ../Frontend
```

### 🪄 Step 2: Install dependencies
```bash
npm install
```

### 🪄 Step 3: Run the React app
```bash
npm run dev
```

✅ The frontend runs on:  
👉 `http://localhost:5173`

---

## 🧩 Application Functionalities

### 🎯 Frontend (React + Vite)
- Displays quiz questions dynamically from backend API.
- Allows users to select answers and submit responses.
- Shows score and feedback after completion.
- Clean UI built with custom CSS and reusable components.

### ⚙️ Backend (FastAPI)
- Provides REST API for quiz questions and answers.
- Stores user attempts and quiz data using SQLAlchemy models.
- Includes input validation via Pydantic schemas.
- Integrated CORS middleware to allow frontend communication.

---

## 🧱 Tech Stack

**Frontend:**
- React (Vite)
- Axios (for API calls)
- Custom CSS

**Backend:**
- FastAPI
- SQLAlchemy ORM
- Uvicorn (ASGI server)
- Pydantic for data validation

**Database:**
- SQLite (local) or PostgreSQL (production)

---

## 🚀 Deployment Notes
- **Frontend** can be deployed on Vercel, Netlify, or GitHub Pages.
- **Backend** can be deployed on Render, Railway, or any FastAPI-compatible server.
- Update backend URL in frontend’s API configuration before deploying.

---

## 👨‍💻 Author
**Barika Suresh**  
Full Stack Developer | React.js | FastAPI | PostgreSQL  

---

## 📜 License
This project is open-source and free to use for learning or demo purposes.
