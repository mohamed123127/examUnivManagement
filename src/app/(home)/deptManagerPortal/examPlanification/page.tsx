'use client'

import DataGrid from '@/src/components/DataGrid/DataGrid'
import React, { useEffect, useState } from 'react'
import SearchArea from '../../examsManagerPortal/examPlanification/SearchArea';
import { useAuth } from "@/src/context/AuthContext";
import { API_BASE_URL } from '@/src/settings';

export type Column = {
  key: string;
  header: string;
  width?: number;
};

export type FormationYear = {
  formation_year_id: number;
  formation_name: string;
  formation_year: number;
  total_groups: number;
  total_modules: number;
  department_name: string;
};

type PagedResponse = {
  page: number;
  page_size: number;
  total_items: number;
  total_pages: number;
  items: FormationYear[];
};

const Page = () => {
  const { user } = useAuth();
  const [formationYearData,setFormationYearData] = useState<PagedResponse>();
  const [currentPage, setCurrentPage] = useState(1);
  const [filter,setFilter] = useState({
    selectedDept : user?.deptId,
    selectedFormation : null,
    selectedYear : null,
  });



  useEffect(() => {
  const params = new URLSearchParams();

  if (filter.selectedDept) {
    params.append("department_id", String(filter.selectedDept));
  }

  if (filter.selectedYear) {
    params.append("year", filter.selectedYear);
  }

  if (filter.selectedFormation) {
    params.append("formation_id", filter.selectedFormation);
  }

  const query = params.toString();
  const url = `${API_BASE_URL}/FormationYear/${currentPage}${query ? `?${query}` : ""}`;

  fetch(url)
    .then((res) => res.json())
    .then((data) => {
      setFormationYearData(data);
    })
    .catch((err) => {
      console.error("Error fetching formation years:", err);
    });

}, [currentPage, filter.selectedDept, filter.selectedYear,filter.selectedFormation]);

const columns: Column[] = [
  
  { key: "department_name", header: "Département",width: 400 },
  { key: "formation_name", header: "Formation"},
  { key: "formation_year", header: "Année", width: 300},
  { key: "total_groups", header: "Nombre de groupes",width: 150 },
  { key: "total_modules", header: "Nombre de modules",width: 150 },
];

  return (
    <div className='flex flex-col w-full h-screen'>
      {/* Search section: by anne,module,dept,formation */}
      <SearchArea setFilter={setFilter} isItChefDept={true}/>
      {/* data grid for tables */}
      <div className='w-full flex-1 overflow-auto'>
        <DataGrid columns={columns} data={formationYearData?.items} pageNumber={currentPage}/>
         {/* Pagination */}
      <div className="flex justify-center items-center gap-2 mt-4">
  <button
    onClick={() => setCurrentPage(prev => Math.max(prev - 1, 1))}
    disabled={currentPage === 1}
    className="px-4 py-2 bg-gray-200 rounded disabled:opacity-50"
  >
    Prev
  </button>

  <span>
    Page {formationYearData?.page} of {formationYearData?.total_pages}
  </span>

  <button
    onClick={() =>{
      setCurrentPage(prev =>
        Math.min(prev + 1, formationYearData?.total_pages ?? 0)
      )
    }}
    disabled={currentPage === formationYearData?.total_pages}
    className="px-4 py-2 bg-gray-200 rounded disabled:opacity-50"
  >
    Next
  </button>
</div>
      </div>
     

    </div>
  )
}

export default Page
