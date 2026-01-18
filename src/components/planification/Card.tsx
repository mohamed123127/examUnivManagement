import React from "react";
import { HiTrash } from "react-icons/hi";

type CardProps = {
  module:string;
  classrooms: number;
  Suppervisiors: number;
  DeleteAction?: (date: Date, time: string) => void; // delete handler
  date: Date;
  time: string;
  isCanControlData: boolean;
};

const Card: React.FC<CardProps> = ({
  module = "Web",
  classrooms = 3,
  Suppervisiors = 9,
  DeleteAction,
  date,
  time,
  isCanControlData=false
}) => {
  return (
    <div className="h-32 w-48 bg-blue-100 rounded-2xl p-2 relative">

      {/* Delete button */}
      {isCanControlData && 
      <button
      onClick={() => DeleteAction && date && time && DeleteAction(date, time)}
      className="absolute bottom-2 right-2 p-1 bg-red-500 text-white rounded-md hover:bg-red-600 transition"
      >
        <HiTrash className="w-4 h-4" />
      </button>
      }

      {/* Card content */}
      <div className={`flex flex-col h-full ${isCanControlData ? 'text-left' : 'items-center justify-center'}`}>

      <div className="flex">
        <h4 className="font-semibold mr-2">Module:</h4>
        <p>{module}</p>
      </div>

      <div className="flex">
        <h4 className="font-semibold mr-2">Total classrooms:</h4>
        <p>{classrooms}</p>
      </div>

      <div className="flex">
        <h4 className="font-semibold mr-2">Total supervisors:</h4>
        <p>{Suppervisiors}</p>
      </div>
        </div>
    </div>
  );
};

export default Card;
