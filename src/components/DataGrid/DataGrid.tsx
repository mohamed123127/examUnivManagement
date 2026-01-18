import React, { useState } from "react";
import { HiChevronRight } from "react-icons/hi";
import ExamSchedule from "../planification/ExamSchedule";
import Card from "../planification/Card";
import { FormationYear } from "@/src/app/(home)/examsManagerPortal/examPlanification/page";

export type Column = {
  key: string;
  header: string;
  width?: number;
};

type DataGridProps = {
  columns: Column[];
  data: FormationYear[] | undefined;
  pageNumber: number;
  isCanControlData: boolean;
};

const DataGrid: React.FC<DataGridProps> = ({ columns, data,pageNumber,isCanControlData=false}) => {
  const [expandedRows, setExpandedRows] = useState<Set<number>>(new Set());

  const toggleRow = (index: number) => {
    const newSet = new Set(expandedRows);
    if (newSet.has(index)) {
      newSet.delete(index);
    } else {
      newSet.add(index);
    }
    setExpandedRows(newSet);
  };

  return (
    <div className="w-full border rounded-lg overflow-auto">
      <table className="w-full border-collapse ">
        <thead>
          <tr className="bg-gray-200">
            <th className="p-2 border text-left font-semibold w-[50px]">#</th>
            {columns.map((col) => (
              <th
                key={col.key}
                className={`p-2 border text-left font-semibold ${col.width ? `w-[${col.width}px]` : ""}`}
              >
                {col.header}
              </th>
            ))}
          </tr>
        </thead>

        <tbody>
          {data?.length === 0 && (
            <tr>
              <td colSpan={columns.length + 1} className="p-3 text-center">
                No data found
              </td>
            </tr>
          )}

          {data?.map((row, i) => {
            const isExpanded = expandedRows.has(i);
            return (
              <React.Fragment key={i}>
                {/* Main row */}
                <tr className="hover:bg-gray-100 transition">
                  <td className="flex justify-center items-center p-2 border cursor-pointer" onClick={() => toggleRow(i)}>
                    <HiChevronRight
                      className={`text-2xl text-blue-600 transition-transform duration-300 ${isExpanded ? "rotate-90" : ""}`}
                    />
                    <p className="ml-2">{(pageNumber-1) * 10 + i + 1}</p>
                  </td>
                  {columns.map((col) => (
                    <td key={col.key} className={`p-2 border ${col.width ? `w-[${col.width}px]` : ""}`}>
                      {row[col.key]}
                    </td>
                  ))}
                </tr>

                {/* Expanded row */}
                {isExpanded && (
                    <tr>
                        <td colSpan={columns.length + 1} className="p-2 border">
                        <ExamSchedule formationYearId={row['formation_year_id']} totalGroups={row['total_groups']} isCanControlData={isCanControlData}/>
                        {/* <Card /> */}
                        </td>
                    </tr>
                )}
              </React.Fragment>
            );
          })}
        </tbody>
      </table>
    </div>
  );
};

export default DataGrid;
