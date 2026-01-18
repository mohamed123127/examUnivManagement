'use client'

import { useAuth } from "@/src/context/AuthContext";
import "../globals.css";
import Sidebar from "@/src/components/sidebar/Sidebar";
import { useRouter } from "next/navigation";
import { useEffect } from "react";

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  const { user } = useAuth();
  const router = useRouter();

  useEffect(() => {
    if (!user) {
      router.replace("/login");
    }
  }, [user, router]);

  if (!user) return null;

  return (
    <div className="flex">
      <div className="w-72">
        <Sidebar role={user.role}/>
      </div>
        <main className="flex-1">{children}</main>
    </div>
  );
}
