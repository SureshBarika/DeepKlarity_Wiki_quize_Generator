import { useState } from "react";
import { generateQuiz } from "../services/api";
import QuizDisplay from "../components/QuizDisplay";

export default function GenerateQuizTab() {
  const [url, setUrl] = useState("");
  const [quiz, setQuiz] = useState(null);
  const [loading, setLoading] = useState(false);

  const handleGenerate = async () => {
    if (!url.trim()) return alert("Please enter a valid Wikipedia URL");
    setLoading(true);
    try {
      const data = await generateQuiz(url);
      setQuiz(data);
    } catch (error) {
      alert("Error generating quiz. Check console.");
      console.error(error);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="max-w-3xl mx-auto">
      <div className="flex space-x-2">
        <input
          type="text"
          placeholder="Enter Wikipedia URL..."
          className="border p-2 rounded w-full"
          value={url}
          onChange={(e) => setUrl(e.target.value)}
        />
        <button
          onClick={handleGenerate}
          className="bg-blue-600 text-white px-4 rounded"
        >
          {loading ? "Generating..." : "Generate"}
        </button>
      </div>

      {quiz && <QuizDisplay quiz={quiz} />}
    </div>
  );
}
