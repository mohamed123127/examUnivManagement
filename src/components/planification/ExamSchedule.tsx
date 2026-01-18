import { Exam, KeyValue } from "@/src/types/exam";
import React, { useEffect, useState } from "react";
import { HiPlus,HiX } from "react-icons/hi";
import dayjs from "dayjs";
import "dayjs/locale/fr";
import Card from "./Card";
import MultiSelectDropDownMenu from "../MultiSelectDropDownMenu";
import { ExecException } from "child_process";



type ExamScheduleProps = {
  formationYearId:number;
  totalGroups: number;
  isCanControlData: boolean;
};

type IdNameType = {
  id:number;
  name:string;
}

type ExamForm = {
  module: string
  classroom: number[]
  date: Date
  time: string
  supervisions: number[]
}


const ExamSchedule: React.FC<ExamScheduleProps> = ({ formationYearId,totalGroups,isCanControlData=false }) => {
  const [isFormOpned,setIsFormOpned] = useState(false);
  const examTimes: Record<string, string> = {
    "08:30:00": "08:30",
    "10:15:00": "10:15",
    "12:00:00": "12:00",
    "13:45:00": "13:45",
    "15:30:00": "15:30",
  };
  const supervisors = ['s1','s2','s1','s2']
  const [Exams,setExams] = useState<Exam[] | null>([])
  const AddExamHandled = ()=>{

    setExams(prev => (prev ? [...prev, examForm] : [examForm]));
    setIsFormOpned(false);
  }
  const [selectedTime,setSelectedTime] = useState('')

  const [examForm, setExamForm] = useState<ExamForm>({
  module: "",
  classroom: [],
  date: new Date(),
  time: selectedTime,
  supervisions: []
});

  const deleteExamHandler = (date: Date, time: string) => {
  setExams(prev =>
    prev.filter(e => !(dayjs(e.date).isSame(date) && e.time === time))
  );
};

  const [notReservedModules,setNotReservedModules] = useState<IdNameType[]>([]);
  const [modules,setModules] = useState<IdNameType[]>([]);
  const [classrooms,setClassrooms] = useState<IdNameType[]>([]);
  const [supervisions,setSupervisions] = useState<IdNameType[]>([]);

  useEffect(() => {
      fetch(`http://127.0.0.1:8000/FormationYear/${formationYearId}/Modules`)
        .then(res => res.json())
        .then(data => {
          setModules(data)
        })
        .catch(err => {
          console.error("Error fetching modules:", err)
        })

        const fetchExams = async () => {
      try {
        const res = await fetch(`http://127.0.0.1:8000/FormationYear/${formationYearId}/Exams`);
        if (!res.ok) throw new Error("Failed to fetch exams");

        const data: Exam[] = await res.json();
        setExams(data);
        const ReservedModules = data.map(e => e.exam_id);
        const RestModules = modules.filter(m => !ReservedModules.includes(m.id));
        setNotReservedModules(RestModules)
      } catch (err) {
        // console.error(err.message);
      }
    };

    fetchExams();
    }, [formationYearId])

  useEffect(() => {
      fetch(`http://127.0.0.1:8000/Classrooms?Date=${examForm.date}&Time=${selectedTime}`)
        .then(res => res.json())
        .then(data => {
          setClassrooms(data);
        })
        .catch(err => {
          console.error("Error fetching modules:", err)
        })
    }, [examForm.date,selectedTime])

  return (
    <div className="flex justify-center">
      {!isFormOpned ?
      <table className="h-full border-collapse text-center">
        <thead>
          <tr>
            <th className="border bg-gray-200">Time</th>
            {modules?.map((module,key) => (
              <th key={key} className="border p-2 bg-gray-200">
                {Exams?.find(e=>e.module_id==module.id) 
                  ? dayjs(Exams?.find(e=>e.module_id==module.id)?.date).locale("fr").format("dddd YYYY-MM-DD") 
                  : 'Not selected yet'}
              </th>
            ))}
          </tr>
        </thead>
        <tbody>
          {Object.keys(examTimes).map((time) => (
            <tr key={time}>
              {/* Left column: time */}
              <td className="border p-2 bg-gray-100 font-semibold w-16">{examTimes[time]}</td>

              {/* Empty cells for modules */}
              
              {modules?.map((module, key) => {
                const selectedExam = Exams?.find(
                  e => e.module_id==module.id &&
                       time === e.time)
                // find matching exam for this cell
                // const selectedExam = Exams?.find(
                //   e =>
                //     dayjs(exam.date).isSame(e.date, "day") &&   // compare only date
                //     time === e.time                        // same time
                // );

                return (
                  <td
                    key={key + time}
                    className="border p-2 relative group"
                  >
                    {/* Button appears on hover */}
                    {isCanControlData &&
                    <button
                    onClick={() =>{setSelectedTime(time); setIsFormOpned(true)}}
                    className={`absolute top-1 left-1 p-1 bg-blue-500 text-white rounded opacity-0 ${!selectedExam && 'group-hover:opacity-100'} transition-opacity duration-200`}
                    >
                      <HiPlus className="w-5 h-5" />
                    </button>
                    }

                    {/* Render card if exam exists */}
                    {selectedExam && (
                      <div  className="flex justify-center items-center">

                      <Card
                        module={selectedExam.module_name}
                        classrooms={selectedExam.total_classrooms}
                        Suppervisiors={selectedExam.total_profs}
                        date={selectedExam.date}
                        time={time}
                        DeleteAction={(date, time) => deleteExamHandler(date, time)}
                        isCanControlData={isCanControlData}
                        />
                        </div>
                    )}
                  </td>
                );
              })}

            </tr>
          ))}
        </tbody>
      </table>
      :
      <div
  className="absolute inset-0 bg-black/50 backdrop-blur-sm flex justify-center items-center z-50"
  onClick={() => setIsFormOpned(false)}
>
  <div
    className="flex flex-col justify-between bg-white rounded-lg p-4 shadow-lg overflow-auto w-1/4 h-auto"
    onClick={(e) => e.stopPropagation()}
  >
    <div className="flex justify-between items-center mb-4">
      <h2 className="text-2xl font-bold">Ajouter un nouvel examen</h2>
      <button onClick={() => setIsFormOpned(false)}>
        <HiX className="text-red-600 font-bold text-3xl" />
      </button>
    </div>

    <div className="space-y-4">

      {/* Module dropdown */}
      <div>
        <label className="font-semibold text-lg">Module</label>
        <select
          className="border p-2 w-full"
          onChange={(e) =>
            setExamForm(prev => ({
              ...prev,
              module: e.target.value
            }))
          }
        >
          <option value="">Choisir un module</option>
          {notReservedModules?.map((module, i) => (
            <option key={i} value={module.id}>
              {module.name}
            </option>
          ))}
        </select>
      </div>
      <p className="text-red-600 font-light">
          – vous devez sélectionner salles des examen et surveillants pour {totalGroups} group
      </p>
      {/* Classroom */}
      <div>
        <label className="font-semibold text-lg">Salles</label>
        <MultiSelectDropDownMenu
  label="Select classrooms"
  options={classrooms}
  setSelectedItems={(newSelected: number[]) => {     
    setExamForm(prev => ({
      ...prev,
      classroom: newSelected
    }))
  }}
/>
      </div>

      {/* Supervisors */}
      <div>
        <label className="font-semibold text-lg">Surveillants</label>
        <MultiSelectDropDownMenu
    label="sélectionné des surveillants"
    options={supervisions}
    setSelectedItems={(newSelected: number[]) => {     
      setExamForm(prev => ({
        ...prev,
        supervisions: newSelected
      }))
    }}
  />
      </div>

    </div>

    <button
      onClick={AddExamHandled}
      className="bg-green-700 p-2 rounded-md text-white mt-2"
    >
      Créer l’examen
    </button>
  </div>
</div>

}
    </div>
  );
};

export default ExamSchedule;
