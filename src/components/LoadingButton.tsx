import { useState, useEffect } from "react";
import CircularWithValueLabel from "./CircularProgressWithLabel";

export default function LoadingButton() {
  const [loading, setLoading] = useState(false);
  const [progress, setProgress] = useState(0);
  const [seconds,setSeconds] = useState(0);

  const handleClick = () => {
    setLoading(true);
    setProgress(0);

    // Start the planification process
    fetch("http://127.0.0.1:8000/StartPlanification")
      .then((res) => res.json())
      .then((data) => {
        // console.log("Planification started:", data);
        setSeconds(0);
      })
      .catch((err) => {
        console.error("Error starting planification:", err);
        setLoading(false);
      });
  };

  // Poll endpoint every second to check progress
  useEffect(() => {
    if (!loading) return;

    const interval = setInterval(() => {
      fetch("http://127.0.0.1:8000/PlanificationProgress") // your endpoint to get progress
        .then((res) => res.json())
        .then((data) => {
          // assuming your endpoint returns { progress: 0-100 }
          setProgress(data.progress);
          setSeconds(prev => prev + 1)
          if (data.progress >= 100) {
            setLoading(false); // stop loading when finished
            alert('Tous les examens ont été planifiés avec succès')
            clearInterval(interval);
          }
        })
        .catch((err) => {
          console.error("Error fetching progress:", err);
          setLoading(false);
          clearInterval(interval);
        });
    }, 1000);

    return () => clearInterval(interval); // cleanup
  }, [loading]);

  return (
    <button
      onClick={handleClick}
      className={`flex justify-between items-center space-x-2 w-[180px] px-4 py-2 rounded-lg font-semibold text-white bg-blue-600 hover:bg-blue-700 disabled:bg-blue-400`}
      disabled={loading}
    >
      <span>{loading ? `Planning...`+seconds+'s' : `Start planification`}</span>
      {loading && <CircularWithValueLabel value={progress} />}
    </button>
  );
}
