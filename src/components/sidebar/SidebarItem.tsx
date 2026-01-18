"use client";

import Link from "next/link";
import { ReactNode } from "react";
import { usePathname } from "next/navigation";

interface SidebarItemProps {
  href: string;
  icon?: ReactNode;
  label: string;
}

export default function SidebarItem({ href, icon, label }: SidebarItemProps) {
  const pathname = usePathname();
  const isActive = pathname === href;

  return (
    <Link
      href={href}
      className={`
        flex items-center gap-3 px-4 py-2 rounded-lg transition-colors
        ${isActive ? "bg-blue-600 text-white" : "text-gray-700 hover:bg-gray-100"}
      `}
    >
      {icon && <span className="text-lg">{icon}</span>}
      <span>{label}</span>
    </Link>
  );
}
