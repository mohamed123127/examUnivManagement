'use client'
import React, { useEffect, useState } from "react";
import { useRouter } from "next/navigation";

const UnauthorizedPage = () => {
  const router = useRouter();
  const [secondsLeft, setSecondsLeft] = useState(5);

  useEffect(() => {
    const interval = setInterval(() => {
      setSecondsLeft((prev) => prev - 1);
    }, 1000);

    const timeout = setTimeout(() => {
      router.push("/login");
    }, 5000);

    return () => {
      clearInterval(interval);
      clearTimeout(timeout);
    };
  }, [router]);

  return (
    <div className="flex flex-col items-center justify-center h-screen bg-gray-100">
      <div className="bg-white p-10 rounded shadow-md text-center">
        <h1 className="text-3xl font-bold text-red-600 mb-4">Accès refusé</h1>
        <p className="text-gray-700 mb-4">
          Vous n&apos;êtes pas autorisé à accéder à cette page.
        </p>

        <p className="text-gray-500 text-sm">
          Redirection vers la page de connexion dans {secondsLeft} secondes...
        </p>
      </div>
    </div>
  );
};

export default UnauthorizedPage;
