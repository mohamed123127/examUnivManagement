"use client";

import { createContext, useContext, useState, ReactNode } from "react";
import { Role } from "../types/role";
import { API_BASE_URL } from "../settings";
 
export interface User {
  id: number;
  matricule: string;
  username:string;
  role: Role;
  groupId: number;
  group: number;
  deptId: number;
}

interface AuthContextType {
  user: User | null;
  login: (matricule: string, password: string) => Promise<User>;
  logout: () => void;
}

const AuthContext = createContext<AuthContextType | null>(null);

export function AuthProvider({ children }: { children: ReactNode }) {
  // load user from localStorage on initial render
  const [user, setUser] = useState<User | null>(() => {
    if (typeof window !== "undefined") {
      const saved = localStorage.getItem("user");
      return saved ? JSON.parse(saved) : null;
    }
    return null;
  });

  const login = async (matricule: string, password: string) => {
    try {
      const res = await fetch(`${API_BASE_URL}/login/`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ matricule, password }),
      });

      if (!res.ok) throw new Error("Login failed");

      const data = await res.json().then((ret) => ret.user);
      const userObj = {
        id: data.id,
        matricule: data.matricule,
        username: data.username,
        role: data.role,
        groupId: data.group_id,
        group: data.group,
        deptId: data.dept_id
      };
      setUser(userObj);
      localStorage.setItem("user", JSON.stringify(userObj));

      return data;
    } catch (err) {
      console.error(err);
      throw err;
    }
  };

  const logout = () => {
    setUser(null);
    localStorage.removeItem("user"); // remove from storage
  };

  return (
    <AuthContext.Provider value={{ user, login, logout }}>
      {children}
    </AuthContext.Provider>
  );
}

export const useAuth = () => {
  const ctx = useContext(AuthContext);
  if (!ctx) throw new Error("useAuth must be used inside AuthProvider");
  return ctx;
};
