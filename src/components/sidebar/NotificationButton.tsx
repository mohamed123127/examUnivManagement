import { fetchNotifications } from "@/src/services/NotificationService";
import { useEffect, useState } from "react";
import { FaBell } from "react-icons/fa";
import { FaInfoCircle } from "react-icons/fa";
import { FaCheckCircle, FaTimesCircle } from "react-icons/fa";


type Notification = {
  message:string;
  type:string;
}

export const NotificationButton= () => {
  const [open, setOpen] = useState(false);
  const [notifications,setNotifications] = useState<Notification[]>([]);

  useEffect(() => {
    fetchNotifications().then((data) => {
      setNotifications(
        data.map((n: any) => ({ message: n.message, type: n.type }))
      );
    });

  }, []);
  return (
    <div className="relative inline-block">
      <button
        onClick={() => setOpen(!open)}
        className="relative p-2 rounded hover:bg-gray-200 focus:outline-none"
      >
        <FaBell size={24} className="text-blue-600"/>
        {notifications.length > 0 && (
          <span className="absolute top-0 right-0 inline-flex items-center justify-center px-1.5 py-0.5 text-xs font-bold leading-none text-white bg-red-500 rounded-full">
            {notifications.length}
          </span>
        )}
      </button>

      {open && (
        <div className="absolute left-0 bottom-12 mt-2 w-64 bg-white shadow-lg border-2 border-black h-64 rounded-md z-50">
          {notifications.length === 0 ? (
            <div className="p-4 text-gray-500 text-xl font-semibold flex justify-center items-center h-full">No notifications</div>
          ) : (
            <div className="h-64 overflow-y-auto">
              {notifications.map((note, idx) => (
                <div key={idx} className="flex gap-2 items-center text-start px-2 py-2 hover:bg-gray-100 cursor-pointer text-sm  text-gray-700">
                  {
                    note.type == "successe" ?
                    <FaCheckCircle className="w-5 h-5 text-green-600"/> :
                    <FaTimesCircle className="w-5 h-5 text-red-500"/>
                  }
                  <p className="flex-1">{note.message}</p>
                </div>
              ))}
            </div>
          )}
        </div>
      )}
    </div>
  );
};
