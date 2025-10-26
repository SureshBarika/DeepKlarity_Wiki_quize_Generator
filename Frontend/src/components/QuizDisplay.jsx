export default function QuizDisplay({ quiz }) {
  if (!quiz) return null;

  return (
    <div className="mt-6 bg-white p-4 rounded-lg shadow-md">
      <h2 className="text-xl font-bold mb-2">{quiz.title}</h2>
      <p className="text-gray-700 mb-4">{quiz.summary}</p>

      <div className="space-y-4">
        {quiz.questions.map((q, index) => (
          <div key={index} className="border p-3 rounded-md bg-gray-50">
            <p className="font-semibold">{q.question}</p>
            <ul className="list-disc pl-6">
              {q.options.map((opt, idx) => (
                <li key={idx}>{opt}</li>
              ))}
            </ul>
            <p className="mt-2 text-green-600 font-medium">
              ✅ Answer: {q.answer}
            </p>
          </div>
        ))}
      </div>
    </div>
  );
}
