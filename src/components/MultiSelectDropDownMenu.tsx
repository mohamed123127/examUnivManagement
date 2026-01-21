import { useState } from "react";
import { FiCheck, FiChevronDown, FiX } from "react-icons/fi";

type Option = {
  id: number;
  name: string;
};

type MultiSelectProps = {
  label: string;
  options: Option[];
  setSelectedItems: (selectedIds: number[]) => void;
};

const MultiSelectDropDownMenu = ({label,options,  setSelectedItems}: MultiSelectProps) => {
  const [open, setOpen] = useState(false);
  const [selected, setSelected] = useState<number[]>([]);

  const toggleSelect = (id: number) => {
    const newSelected = selected.includes(id)
      ? selected.filter(x => x !== id)
      : [...selected, id];
    setSelectedItems(newSelected);
    setSelected(newSelected);
  };

  const removeTag = (id: number) => {
    setSelectedItems(selected.filter(x => x !== id));
    setSelected(selected.filter(x => x !== id));
  };

  return (
    <div className="relative w-full">

      {/* INPUT */}
      <div
        className="border rounded p-2 flex items-center min-h-[40px] cursor-pointer"
        onClick={() => setOpen(o => !o)}
      >
        <span className="text-gray-400">
          {label}
        </span>

        <FiChevronDown
          className={`ml-auto transition-transform ${open ? "rotate-180" : ""}`}
        />
      </div>

      {/* DROPDOWN */}
      {open && (
  <div className="absolute z-10 w-full mt-1 border rounded shadow bg-white max-h-60 overflow-y-auto">
    {options.length === 0 ? (
      <div className="p-2 text-gray-400 text-center">
        Aucun élément à sélectionner
      </div>
    ) : (
      options.map(item => {
        const isSelected = selected.includes(item.id);

        return (
          <div
            key={item.id}
            onClick={() => toggleSelect(item.id)}
            className="p-2 flex justify-between items-center hover:bg-gray-100 cursor-pointer"
          >
            <span>{item.name}</span>
            {isSelected && <FiCheck className="text-green-600" />}
          </div>
        );
      })
    )}
  </div>
)}


      <div
        className={`flex flex-wrap gap-2 mt-3 border-2 rounded-lg p-3 h-24 ${
          selected.length === 0
            ? "justify-center items-center text-center"
            : "justify-start items-start"
        } border-blue-600 overflow-y-auto`}
      >
        {selected.length === 0 && (
          <span className="text-gray-400">
            aucun élément sélectionné pour le moment !!
          </span>
        )}

        {selected.map(id => {
          const item = options.find(o => o.id === id);

          return (
            <div
              key={id}
              className="flex items-center gap-1 bg-blue-100 text-blue-700 px-2 py-1 rounded-md text-sm"
            >
              {item?.name}

              {/* small remove button */}
              <button
                onClick={() => removeTag(id)}
                className="ml-1"
              >
                <FiX />
              </button>
            </div>
          );
        })}
      </div>
    </div>
  );
};

export default MultiSelectDropDownMenu;
