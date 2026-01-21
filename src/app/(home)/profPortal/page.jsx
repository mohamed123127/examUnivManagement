'use client';

import React, { use, useEffect, useState } from "react";
import { User } from "@/src/context/AuthContext";
import { useRouter } from "next/navigation";
import { API_BASE_URL } from "@/src/settings";

const examTimes = {
  "08:30:00":"08:30", 
  "10:15:00":"10:15", 
  "12:00:00":"12:00", 
  "13:45:00":"13:45", 
  "15:30:00":"15:30"
};

const Page = () => {
  const userString = localStorage.getItem("user");
  const user = userString ? JSON.parse(userString) : null;
  const router = useRouter();

  useEffect(()=>{
    const isAuthorized = user?.role == 'Professeur';
    if(!isAuthorized) router.push("/Unauthorized")
  },[])

  const [exams, setExams] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetch(API_BASE_URL+"/profs/"+user?.id+"/ExamsSchedule")
      .then((res) => res.json())
      .then((data) => {setExams(data);})
      .finally(() => setLoading(false));
      
  }, []);


  // Get unique dates
  const dates = Array.from(new Set(exams.map((e) => e.date))).sort();

  // Helper to find exam by date and time
  const getExamAt = (date, time) =>{
    return exams.find((e) => e.date == date && e.time == time)
  }

  const getFormatedDay = (date)=>{
    if (!(date instanceof Date)) {
    date = new Date(date);
  }

  const weekday = date.toLocaleDateString('fr-FR', { weekday: 'long' });
  const dayMonthYear = date.toLocaleDateString('fr-FR', { day: '2-digit', month: '2-digit', year: 'numeric' });

  
  return <>
    {weekday}
    <br/>
    {dayMonthYear}
  </>;
}

if (loading) return <p>Loading exams...</p>;

  return (
    <div className="flex flex-col  p-4 items-center h-screen">
      <h1 className="text-3xl font-bold mb-16 mt-8">Exams Schedule</h1>

      <div className="overflow-x-auto">
        <table className="border-collapse border border-gray-300 w-full text-center">
          <thead>
            <tr className="bg-gray-200">
              <th className="border border-gray-300 px-4 py-2">Time</th>
              {dates.map((date,i) => (
                <th key={i} className="border border-gray-300 px-4 py-2">
                  <>
                    { getFormatedDay(date)}
                  </>
                </th>
              ))}
            </tr>
          </thead>
          <tbody>
            {Object.keys(examTimes).map(key => (
              <tr key={key}>
                <td className="border border-gray-300 px-4 py-2 font-semibold">{examTimes[key]}</td>
                {dates.map((date) => {
                  const exam = getExamAt(date, key);
                  return (
                    <td key={date + key} className="border border-gray-300 px-2 py-2">
                      {exam ? (
                        <div className="bg-blue-100 p-2 rounded shadow text-left">
                          <p className="font-semibold">{exam.module_name}</p>
                          <p><span className="font-semibold">Classroom:</span> {exam.classroom}</p>
                        </div>
                      ) : null}
                    </td>
                  );
                })}
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
};

export default Page;