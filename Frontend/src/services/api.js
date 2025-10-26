import axios from "axios";
const API_BASE = "http://127.0.0.1:8000"; // FastAPI backend URL

export const generateQuiz = async (url) => {
  const res = await axios.post(`${API_BASE}/generate_quiz`, { url });
  return res.data;
};

export const getHistory = async () => {
  const res = await axios.get(`${API_BASE}/history`);
  return res.data;
};

export const getQuizById = async (id) => {
  const res = await axios.get(`${API_BASE}/quiz/${id}`);
  return res.data;
};
