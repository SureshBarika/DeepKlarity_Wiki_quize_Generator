export default function HistoryTable({ data, onView }) {
  return (
    <table className="min-w-full border border-gray-300 bg-white rounded-md">
      <thead className="bg-gray-100">
        <tr>
          <th className="p-2 border">ID</th>
          <th className="p-2 border">Title</th>
          <th className="p-2 border">URL</th>
          <th className="p-2 border">Date</th>
          <th className="p-2 border">Actions</th>
        </tr>
      </thead>
      <tbody>
        {data.map((quiz) => (
          <tr key={quiz.id} className="text-center">
            <td className="p-2 border">{quiz.id}</td>
            <td className="p-2 border">{quiz.title}</td>
            <td className="p-2 border text-blue-600 underline">
              <a href={quiz.url} target="_blank">{quiz.url}</a>
            </td>
            <td className="p-2 border">
              {new Date(quiz.date_generated).toLocaleString()}
            </td>
            <td className="p-2 border">
              <button
                onClick={() => onView(quiz.id)}
                className="bg-blue-600 text-white px-3 py-1 rounded hover:bg-blue-700"
              >
                View
              </button>
            </td>
          </tr>
        ))}
      </tbody>
    </table>
  );
}
