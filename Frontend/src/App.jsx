import { useState } from "react";
import GenerateQuizTab from "./tabs/GenerateQuizTab";
import HistoryTab from "./tabs/HistoryTab";
import TabButton from "./components/TabButton";

export default function App() {
  const [activeTab, setActiveTab] = useState("generate");

  return (
    <div className="min-h-screen p-6">
      <h1 className="text-3xl font-bold text-center text-blue-600 mb-6">
        🧠 AI Wiki Quiz Generator
      </h1>

      <div className="flex justify-center space-x-4 mb-8">
        <TabButton
          label="Generate Quiz"
          active={activeTab === "generate"}
          onClick={() => setActiveTab("generate")}
        />
        <TabButton
          label="History"
          active={activeTab === "history"}
          onClick={() => setActiveTab("history")}
        />
      </div>

      {activeTab === "generate" ? <GenerateQuizTab /> : <HistoryTab />}
    </div>
  );
}
