'use client'

import { SplitCircleStatCard } from '@/src/components/statistiques/SplitCircleStatCard'
import { StatCard } from '@/src/components/statistiques/StatCard'
import { PieChart } from '@mui/x-charts'
import React, { useEffect, useState } from 'react'
import { useAuth } from "@/src/context/AuthContext";
import { API_BASE_URL } from '@/src/settings'

export type TableRow = {
  exam_time: string;
  count: number;
};

const Page = () => {
    const { user } = useAuth();
  const [generaleStats,setGeneraleStats] = useState({
      'exams': '0',
      'examsSession': '0',
      'sallesPerDay': '0',
      'avgSessionsPerProf': '0'
  })
  const [tableData,setTableData] = useState<TableRow[]>([]);
  const [examPerDept, setExamPerDept] = useState<Array<{ department_id: number, examPerDept: number }>>([]);

  useEffect(() => {
    const fetchGeneralStats = async () => {
      try {
        const res = await fetch(`${API_BASE_URL}/exams-stats?department_id=`+user?.deptId);
        const data = await res.json();

        setGeneraleStats({
          exams: data.total_exams,
          examsSession: data.total_exam_sessions,
          sallesPerDay: data.salles_per_day,
          avgSessionsPerProf: data.avg_sessions_per_prof,
        });

      } catch (error) {
        console.error("Error fetching general stats:", error);
      }
    };

    const fetchStudentGroups = async () => {
      try {
        const res = await fetch(`${API_BASE_URL}/most-used-hours?department_id=`+user?.deptId);
        const data = await res.json();
        setTableData(data);
      } catch (error) {
        console.error("Error fetching student groups stats:", error);
      }
    };

    const fetchExamPerDept = async () => {
      try {
        const res = await fetch(`${API_BASE_URL}/exam-per-department?department_id=`+user?.deptId);
        const data = await res.json();
        setExamPerDept(data);
        console.log(data)
      } catch (error) {
        console.error("Error fetching exams per department:", error);
      }
    };

    fetchGeneralStats();
    fetchStudentGroups();
    fetchExamPerDept();
  }, []);

  return (
        <div className='w-full h-full flex flex-col items-center bg-blue-50 p-8'>
          <h1 className='text-3xl text-center font-bold'>Statistiques</h1>
          <div className='flex justify-between mt-12 w-full px-12'>
              <StatCard width='w-1/5' title='Examens' value={generaleStats.exams}/>
              <StatCard width='w-1/5' title='Séances d&apos;examen' value={generaleStats.examsSession}/>
              <StatCard width='w-1/5' title='Avg Salles/Jour' value={generaleStats.sallesPerDay}/>
              <StatCard width='w-1/5' title='Avg Séances/Prof' value={generaleStats.avgSessionsPerProf}/>
          </div>
          <div className='flex justify-between w-full mt-16 space-x-48 px-32'>
            <div className="w-full bg-white rounded-xl shadow-lg overflow-hidden">
              <table className="w-full text-center">
                <thead className="bg-blue-600 text-white">
                  <tr>
                    <th className="py-3">Heure</th>
                    <th>Nombre d&apos;examens</th>
                  </tr>
                </thead>
                <tbody>
                  {tableData.map((raw,key)=>(
                     <tr key={key} className="even:bg-blue-50">
                      <td className="py-3 font-semibold text-blue-800">{raw.exam_time}</td>
                      <td className="text-blue-700 font-semibold">{raw.count}</td>
                    </tr>
                  ))}
                </tbody>
              </table>
            </div>
          </div>
        </div>
  )
}

export default Page
