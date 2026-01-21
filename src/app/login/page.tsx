"use client";

import { useAuth } from "@/src/context/AuthContext";
import { useRouter } from "next/navigation";
import { useState } from "react";

export default function LoginPage() {
  const [matricule, setMatricule] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState("");

  const { login } = useAuth();
  const router = useRouter();

  const handleLogin = async (e: React.FormEvent<HTMLFormElement>) => {
    e.preventDefault();
    setError("");

    try {
      const user = await login(matricule, password);
      switch (user?.role) {
        case "Étudiant":
          router.push("/studentPortal");
          break;
        case "Doyen":
        case "Vice-doyen":
          router.push("/doyenPortal");
          break;
        case "Chef de département":
          router.push("/deptManagerPortal");
          break;
        case "Administrateur examens":
          router.push("/examsManagerPortal");
          break;
        case "Professeur":
          router.push("/profPortal");
          break;
        default:
          router.push("/login");
      }
    } catch (err) {
      console.error(err);
      setError("Matricule ou mot de passe incorrect");
    }
  };

  return (
    <div className="min-h-screen flex items-center justify-center bg-gray-100">
      <form
        onSubmit={handleLogin}
        className="w-full max-w-sm bg-white p-6 rounded-xl shadow"
      >
        <h1 className="text-2xl font-bold text-center mb-6">Login</h1>

        <div className="mb-4">
          <label className="block text-sm font-medium mb-1">Matricule</label>
          <input
            type="text"
            value={matricule}
            onChange={(e) => setMatricule(e.target.value)}
            className="w-full border rounded-lg px-3 py-2 focus:outline-none focus:ring-2 focus:ring-blue-500"
            placeholder="Entrer le matricule"
            required
          />
        </div>

        <div className="mb-6">
          <label className="block text-sm font-medium mb-1">Mot de passe</label>
          <input
            type="password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            className="w-full border rounded-lg px-3 py-2 focus:outline-none focus:ring-2 focus:ring-blue-500"
            placeholder="Entrer le mot de passe"
            required
          />
        </div>
{error && <p className="text-red-500 mb-4 text-center">{error}</p>}
        <button
          type="submit"
          className="w-full bg-blue-600 text-white py-2 rounded-lg hover:bg-blue-700 transition"
        >
          Se connecter
        </button>
      </form>
    </div>
  );
}
