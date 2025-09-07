import { useState, useEffect } from "react";

export default function Clock() {
  const [time, setTime] = useState(new Date());

  // Auto-update every second
//   useEffect(() => {
//     const timer = setInterval(() => setTime(new Date()), 1000);
//     return () => clearInterval(timer); // cleanup
//   }, []);

  return (
    <div className="flex flex-col items-center justify-center min-h-screen bg-gradient-to-r from-gray-900 via-black to-gray-800 text-white">
      <div className="text-6xl font-mono font-bold tracking-widest bg-gray-900/40 backdrop-blur-md px-8 py-6 rounded-2xl shadow-lg border border-gray-700">
        {time.toLocaleTimeString()}
      </div>
      <div className="mt-4 text-lg text-gray-400">
        {time.toDateString()}
      </div>
      <button
        onClick={() => setTime(new Date())}
        className="mt-6 px-6 py-2 rounded-xl bg-blue-600 hover:bg-blue-700 transition duration-300 shadow-md font-semibold"
      >
        Refresh
      </button>
    </div>
  );
}
