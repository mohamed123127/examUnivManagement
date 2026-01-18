import { Exam, KeyValue } from "@/src/types/exam";
import React, { useEffect, useState } from "react";
import { HiPlus,HiX } from "react-icons/hi";
import dayjs from "dayjs";
import "dayjs/locale/fr";
import Card from "./Card";
import MultiSelectDropDownMenu from "../MultiSelectDropDownMenu";
import { ExecException } from "child_process";
import { API_BASE_URL } from "@/src/settings";



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
  const [selectedTime,setSelectedTime] = useState('')

  const [examForm, setExamForm] = useState<ExamForm>({
  module: "",
  classroom: [],
  date: new Date(),
  time: selectedTime,
  supervisions: []
});

  const [notReservedModules,setNotReservedModules] = useState<IdNameType[]>([]);
  const [modules,setModules] = useState<IdNameType[]>([]);
  const [classrooms,setClassrooms] = useState<IdNameType[]>([]);
  const [supervisions,setSupervisions] = useState<IdNameType[]>([]);

  useEffect(() => {
      fetch(`${API_BASE_URL}/FormationYear/${formationYearId}/Modules`)
        .then(res => res.json())
        .then(data => {
          setModules(data)
        })
        .catch(err => {
          console.error("Error fetching modules:", err)
        })

        const fetchExams = async () => {
      try {
        const res = await fetch(`${API_BASE_URL}/FormationYear/${formationYearId}/Exams`);
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
      fetch(`${API_BASE_URL}/Classrooms?Date=${examForm.date}&Time=${selectedTime}`)
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
    </div>
  );
};

export default ExamSchedule;
