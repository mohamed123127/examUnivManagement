import LoadingButton from '@/src/components/LoadingButton'
import { createNotification } from '@/src/services/NotificationService';
import { KeyValue } from '@/src/types/exam'
import React, { useEffect, useState } from 'react'
import { useAuth } from "@/src/context/AuthContext";
import { API_BASE_URL } from '@/src/settings';

const SearchArea = ({setFilter,isCanControlData=false,isItChefDept=false}) => {
    const [depts,setDepts] = useState()
    const [formations,setFormations] = useState()
    const [years,setYears] = useState()
    const { user } = useAuth();

    async function fetchData() {
    const res = await fetch(`${API_BASE_URL}/${endpoint}`);
    if (!res.ok) throw new Error("Failed to fetch " + endpoint);
    return res.json();
    }

    useEffect(() => {

        fetchData("FormationYears")
        .then(setYears)
        .catch(console.error);
        
        fetchData("Formations")
        .then(setFormations)
        .catch(console.error);

        fetchData("Departments")
        .then(setDepts)
        .catch(console.error);
    }, []);

    const AcceptHandled = async () => {
    await createNotification({
      message: "Le planning des examens a été accepté par M/Mme "+ user?.username,
      type: "successe",
    });
    alert('L’opération de validation du planning des examens a été effectuée avec succès')
  };
    
      const RefuseHandled = async ()=>{
        await createNotification({
      message: "Le planning des examens a été refusé par M/Mme "+ user?.username,
      type: "error",
    });
    alert('L’opération de refus du planning des examens a été effectuée avec succès')
      }

  return (
    <div className='flex justify-between w-full h-20 items-center p-2 bg-slate-50'>
        <div className={`flex space-x-4 ${isItChefDept ? 'w-1/2' : 'w-3/4'}`}>
        {!isItChefDept &&
            <div className='flex h-10 space-x-1 w-full items-center'>
                <label className="text-lg font-medium">Department</label>
                <select 
                    className="border-2 border-blue-700 rounded-lg p-2 w-full
                    hover:border-blue-700 focus:border-blue-700 focus:ring-blue-700 outline-none"
                    onChange={(e) => {
  setFilter(prev => ({ ...prev, selectedDept: e.target.value }));
}}>
                    <option value="">Tous</option>
                    {depts?.map((dept, i) => (
                        <option key={i} value={dept.id}>
                        {dept.name}
                    </option>
                    ))}
                </select>
            </div>
}
             <div className='flex h-10 space-x-1  w-full items-center'>
                <label className="text-lg font-medium">Formation</label>
                <select 
                    className="border-2 border-blue-700 rounded-lg p-2 w-full
                    hover:border-blue-700 focus:border-blue-700 focus:ring-blue-700 outline-none"
                    onChange={(e) => {
  setFilter(prev => ({ ...prev, selectedFormation: e.target.value }));
}}>
                    <option value="">Tous</option>
                    {formations?.map((dept, i) => (
                        <option key={i} value={dept.id}>
                        {dept.name}
                    </option>
                    ))}
                </select>
            </div>
             <div className='flex h-10 space-x-1 items-center w-1/2'>
                <label className="text-lg font-medium">Year</label>
                <select 
                    className="border-2 border-blue-700 rounded-lg p-2 w-full
                    hover:border-blue-700 focus:border-blue-700 focus:ring-blue-700 outline-none"
                    onChange={(e) => {
  setFilter(prev => ({ ...prev, selectedYear: e.target.value }));
}}>
                    <option value="">Tous</option>
                    {years?.map((dept, i) => (
                        <option key={i} value={dept}>
                        {dept}
                    </option>
                    ))}
                </select>
            </div>
             
        </div>
        {isCanControlData ?
        <LoadingButton />
        :
        <div className='space-x-4'>
            <button onClick={RefuseHandled} className='px-4 py-1 bg-red-600 text-white text-lg font-semibold rounded-lg'>Refuse</button>
            <button onClick={AcceptHandled} className='px-4 py-1 bg-green-600 text-white text-lg font-semibold rounded-lg'>Accept</button>
        </div>
        }
    </div>
  )
}

export default SearchArea
