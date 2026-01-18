"use client";

import { useAuth } from "@/src/context/AuthContext";
import { FaSignOutAlt } from "react-icons/fa";
import { NotificationButton } from "./NotificationButton";
import { useEffect, useState } from "react";
import { fetchNotifications} from "../../services/NotificationService"


export default function Account() {
  const { user,logout } = useAuth();
  const LogoutHandled = ()=>{
    logout()
  }

  return (
    <div className="flex items-center justify-between">
      <div className="flex items-center gap-3">
        <div className="w-9 h-9 rounded-full bg-blue-600 text-white flex items-center justify-center font-bold">
          {user?.username.substring(0,1)}
        </div>

        <div>
          <p className="text-sm font-medium">{user?.username}</p>
          <p className="text-xs text-gray-500">
            {user?.role}
            {user?.role &&  user?.role === "Étudiant" && ' group' + user?.group}
          </p>
        </div>
      </div>
      <div className="mt-1">
        {user?.role == 'Administrateur examens' &&
        <button>
                <NotificationButton />
        </button>
        }

        <button onClick={LogoutHandled}>
          <FaSignOutAlt size={24} className="text-red-600 ml-2"/>
        </button>
      </div>
    </div>
  );
}
