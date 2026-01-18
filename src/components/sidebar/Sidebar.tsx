
import Account from "./Account";
import SidebarItem from "./SidebarItem";

interface SidebarProps {
  role: "Doyen" | "Vice-doyen" | "Administrateur examens" | "Chef de département" | "Étudiant" | "Professeur";
}

export default function Sidebar({role}: SidebarProps) {
  return (
    <aside className="flex flex-col justify-between w-72 h-screen border-r bg-white p-4">
      <div>
        <h2 className="text-xl font-bold mb-16 text-center">Exam Management Platform</h2>

      <nav className="flex flex-col gap-2">
        {(role == 'Doyen' || role == 'Vice-doyen') && (
          <div>
            <SidebarItem href="/doyenPortal" label="Tableau de bord" />
            <SidebarItem href="/doyenPortal/examPlanification" label="Planification des examens" />
            <SidebarItem href="/doyenPortal/statistiques" label="Statistiques" />
          </div>
        )}

        {role == 'Chef de département' && (
          <div>
            <SidebarItem href="/deptManagerPortal" label="Tableau de bord" />
            <SidebarItem href="/deptManagerPortal/examPlanification" label="Planification des examens" />
            <SidebarItem href="/deptManagerPortal/statistiques" label="Statistiques" />
          </div>
        )}

        {role == 'Administrateur examens' && (
          <div>
            <SidebarItem href="/examsManagerPortal" label="Tableau de bord" />
            <SidebarItem href="/examsManagerPortal/examPlanification" label="Planification des examens" />
            <SidebarItem href="/examsManagerPortal/statistiques" label="Statistiques" />
          </div>
        )}

        {role == 'Professeur' && (
          <div>
            <SidebarItem href="/profPortal" label="Programme" />
          </div>
        )}

        {role == 'Étudiant' && (
          <div>
            <SidebarItem href="/studentPortal" label="Programme" />
          </div>
        )}
      </nav>
      </div>

      <Account />
    </aside>
  );
}

