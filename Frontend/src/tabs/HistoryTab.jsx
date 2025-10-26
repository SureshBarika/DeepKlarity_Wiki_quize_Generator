import { useEffect, useState } from "react";
import { getHistory, getQuizById } from "../services/api";
import HistoryTable from "../components/HistoryTable";
import Modal from "../components/Modal";
import QuizDisplay from "../components/QuizDisplay";

export default function HistoryTab() {
  const [history, setHistory] = useState([]);
  const [selectedQuiz, setSelectedQuiz] = useState(null);
  const [modalOpen, setModalOpen] = useState(false);

  useEffect(() => {
    const fetchHistory = async () => {
      const data = await getHistory();
      setHistory(data);
    };
    fetchHistory();
  }, []);

  const handleView = async (id) => {
    const data = await getQuizById(id);
    setSelectedQuiz(data);
    setModalOpen(true);
  };

  return (
    <div className="max-w-5xl mx-auto">
      <HistoryTable data={history} onView={handleView} />

      <Modal show={modalOpen} onClose={() => setModalOpen(false)}>
        {selectedQuiz ? <QuizDisplay quiz={selectedQuiz} /> : <p>Loading...</p>}
      </Modal>
    </div>
  );
}
