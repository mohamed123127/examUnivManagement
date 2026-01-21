'use client'

import { SplitCircleStatCard } from '@/src/components/statistiques/SplitCircleStatCard'
import { StatCard } from '@/src/components/statistiques/StatCard'
import { PieChart } from '@mui/x-charts'
import React, { useEffect, useState } from 'react'
import { useAuth } from "@/src/context/AuthContext";
import { API_BASE_URL } from '@/src/settings'

export type TableRow = {
  studentPerGroup: number; 
  group_repetition: number;
};

const Page = () => {
    const { user } = useAuth();
  const [generaleStats,setGeneraleStats] = useState({
      'students': '0',
      'profs': '0',
      'formations': '0',
      'modules': '0'
  })
  const [tableData,setTableData] = useState<TableRow[]>([]);
  const [classroomsCount,setClassroomsCount] = useState({
    'amphi': 65,
    'class': 98
  })

  useEffect(() => {
    // Fetch general stats
    const fetchGeneralStats = async () => {
      try {
        const res = await fetch(`${API_BASE_URL}/general-stats?department_id=`+user?.deptId);
        const data = await res.json();

        setGeneraleStats({
          students: data.total_students,
          profs: data.total_professors,
          formations: data.total_formations,
          modules: data.total_modules,
        });

        // Convert classroom list into object
        const counts: Record<string, number> = {};
        data.classrooms_by_type.forEach((c: any) => {
          counts[c.type] = c.occupation_rate;
        });
        console.log(counts)
        setClassroomsCount(counts as { amphi: number; class: number })
      } catch (error) {
        console.error("Error fetching general stats:", error);
      }
    };

    // Fetch student per group table
    const fetchStudentGroups = async () => {
      try {
        const res = await fetch(`${API_BASE_URL}/student-groups-stats?department_id=`+user?.deptId);
        const data = await res.json();
        setTableData(data);
      } catch (error) {
        console.error("Error fetching student groups stats:", error);
      }
    };

    fetchGeneralStats();
    fetchStudentGroups();
  }, []);

  return (
        <div className='w-full h-full flex flex-col items-center bg-blue-50 p-8'>
          <h1 className='text-3xl text-center font-bold'>Tableau de bord</h1>
          <div className='flex justify-between mt-12 w-full px-12'>
              <StatCard width='w-1/5' title='Étudiants' value={generaleStats.students}/>
              <StatCard width='w-1/5' title='Professeurs' value={generaleStats.profs}/>
              <StatCard width='w-1/5' title='Formations' value={generaleStats.formations}/>
              <StatCard width='w-1/5' title='Modules' value={generaleStats.modules}/>
          </div>
          <div className='flex justify-between w-full mt-16 space-x-48 px-32'>
            <div className="w-full bg-white rounded-xl shadow-lg overflow-hidden">
              <table className="w-full text-center">
                <thead className="bg-blue-600 text-white">
                  <tr>
                    <th className="py-3">étudiants par groupe</th>
                    <th>Nombre de groupes</th>
                  </tr>
                </thead>
                <tbody>
                  {tableData.map((raw,key)=>(
                     <tr key={key} className="even:bg-blue-50">
                      <td className="py-3 font-semibold text-blue-800">{raw.studentPerGroup}</td>
                      <td className="text-blue-700 font-semibold">{raw.group_repetition}</td>
                    </tr>
                  ))}
                </tbody>
              </table>
            </div>
            <div className='flex flex-col items-center'>
              <PieChart
                series={[
                  {
                    data: [
                      { id: 0, value: classroomsCount.amphi, label: 'Amphi',color: '#1e40af' },
                      { id: 1, value: classroomsCount.class, label: 'Class',color: '#60a5fa' },
                    ],
                  },
                ]}
                width={300}
                height={300}
              />
              <h3 className='text-2xl font-bold mr-16'>Classrooms</h3>
            </div>
          </div>
        </div>
  )
}

export default Page
