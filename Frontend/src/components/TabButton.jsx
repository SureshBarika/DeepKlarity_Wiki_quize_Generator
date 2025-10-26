export default function TabButton({ label, active, onClick }) {
  return (
    <button
      onClick={onClick}
      className={`px-4 py-2 rounded-lg font-semibold transition ${
        active
          ? "bg-blue-600 text-white"
          : "bg-gray-200 hover:bg-gray-300 text-gray-700"
      }`}
    >
      {label}
    </button>
  );
}
