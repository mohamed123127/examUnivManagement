from datetime import date, time

# =========================
# ROLES
# =========================
roles = [
    {"id": 1, "name": "ADMIN"},
    {"id": 2, "name": "PROFESSOR"},
    {"id": 3, "name": "STUDENT"},
]

# =========================
# DEPARTMENTS
# =========================
departments = [
    {"id": 1, "name": "Computer Science"},
    {"id": 2, "name": "Mathematics"},
]

# =========================
# FORMATIONS
# =========================
formations = [
    {"id": 1, "name": "Licence Informatique", "department_id": 1},
    {"id": 2, "name": "Master Informatique", "department_id": 1},
    {"id": 3, "name": "Licence Mathématiques", "department_id": 2},
    {"id": 4, "name": "Master Mathématiques", "department_id": 2},
]

# =========================
# FORMATION YEARS
# =========================
formation_years = [
    {"id": 1, "formation_id": 1, "year": "L1"},
    {"id": 2, "formation_id": 1, "year": "L2"},
    {"id": 3, "formation_id": 1, "year": "L3"},
    {"id": 4, "formation_id": 2, "year": "M1"},
    {"id": 5, "formation_id": 2, "year": "M2"},
    {"id": 6, "formation_id": 3, "year": "L1"},
    {"id": 7, "formation_id": 3, "year": "L2"},
    {"id": 8, "formation_id": 3, "year": "L3"},
    {"id": 9, "formation_id": 4, "year": "M1"},
    {"id": 10, "formation_id": 4, "year": "M2"},
    {"id": 11, "formation_id": 1, "year": "Prep"},
    {"id": 12, "formation_id": 3, "year": "Prep"},
    {"id": 13, "formation_id": 2, "year": "Research"},
    {"id": 14, "formation_id": 4, "year": "Research"},
]

# =========================
# MODULES
# =========================
modules = [
    {"id": 1, "name": "Algorithms"},
    {"id": 2, "name": "Databases"},
    {"id": 3, "name": "Mathematics I"},
    {"id": 4, "name": "Statistics"},
    {"id": 5, "name": "Linear Algebra"},
    {"id": 6, "name": "Analysis"},
    {"id": 7, "name": "Probability"},
    {"id": 8, "name": "Numerical Methods"},
    {"id": 9, "name": "Programming I"},
    {"id": 10, "name": "Programming II"},
    {"id": 11, "name": "Operating Systems"},
    {"id": 12, "name": "Networks"},
    {"id": 13, "name": "Software Engineering"},
    {"id": 14, "name": "Artificial Intelligence"},
    {"id": 15, "name": "Machine Learning"},
    {"id": 16, "name": "Web Development"},
    {"id": 17, "name": "Mobile Development"},
    {"id": 18, "name": "Discrete Mathematics"},
    {"id": 19, "name": "Mathematical Modeling"},
    {"id": 20, "name": "Statistics II"},
    {"id": 21, "name": "Topology"},
    {"id": 22, "name": "Differential Equations"},
    {"id": 23, "name": "Optimization"},
    {"id": 24, "name": "Complex Analysis"},
    {"id": 25, "name": "Cybersecurity"},
    {"id": 26, "name": "Cloud Computing"},
    {"id": 27, "name": "DevOps"},
    {"id": 28, "name": "Data Science"},
    {"id": 29, "name": "Computer Graphics"},
    {"id": 30, "name": "Robotics"},
    {"id": 31, "name": "Big Data"},
    {"id": 32, "name": "Quantum Computing"},
    {"id": 33, "name": "Numerical Linear Algebra"},
    {"id": 34, "name": "Game Development"},
    {"id": 35, "name": "Simulation Techniques"},
    {"id": 36, "name": "Optimization Methods"},
    {"id": 37, "name": "Information Theory"},
    {"id": 38, "name": "Computer Vision"},
    {"id": 39, "name": "Embedded Systems"},
    {"id": 40, "name": "Graph Theory"},
    {"id": 41, "name": "Operations Research"},
    {"id": 42, "name": "Database Security"},
]

# =========================
# FORMATION YEAR MODULES
# =========================
formation_year_modules = [
    {"id": 1, "formation_year_id": 1, "module_id": 1},
    {"id": 48, "formation_year_id": 1, "module_id": 2},
    {"id": 2, "formation_year_id": 1, "module_id": 3},
    {"id": 3, "formation_year_id": 1, "module_id": 9},
    {"id": 4, "formation_year_id": 1, "module_id": 18},
    {"id": 5, "formation_year_id": 2, "module_id": 1},
    {"id": 6, "formation_year_id": 2, "module_id": 2},
    {"id": 7, "formation_year_id": 2, "module_id": 10},
    {"id": 8, "formation_year_id": 2, "module_id": 19},
    {"id": 9, "formation_year_id": 3, "module_id": 3},
    {"id": 10, "formation_year_id": 3, "module_id": 4},
    {"id": 11, "formation_year_id": 3, "module_id": 11},
    {"id": 12, "formation_year_id": 3, "module_id": 20},
    {"id": 13, "formation_year_id": 4, "module_id": 5},
    {"id": 14, "formation_year_id": 4, "module_id": 6},
    {"id": 15, "formation_year_id": 4, "module_id": 12},
    {"id": 16, "formation_year_id": 4, "module_id": 21},
    {"id": 17, "formation_year_id": 5, "module_id": 2},
    {"id": 18, "formation_year_id": 5, "module_id": 4},
    {"id": 19, "formation_year_id": 5, "module_id": 13},
    {"id": 20, "formation_year_id": 5, "module_id": 22},
    {"id": 21, "formation_year_id": 6, "module_id": 7},
    {"id": 22, "formation_year_id": 6, "module_id": 8},
    {"id": 23, "formation_year_id": 6, "module_id": 23},
    {"id": 24, "formation_year_id": 7, "module_id": 14},
    {"id": 25, "formation_year_id": 7, "module_id": 15},
    {"id": 26, "formation_year_id": 7, "module_id": 24},
    {"id": 27, "formation_year_id": 8, "module_id": 16},
    {"id": 28, "formation_year_id": 8, "module_id": 17},
    {"id": 29, "formation_year_id": 8, "module_id": 25},
    {"id": 30, "formation_year_id": 9, "module_id": 26},
    {"id": 31, "formation_year_id": 9, "module_id": 27},
    {"id": 32, "formation_year_id": 9, "module_id": 28},
    {"id": 33, "formation_year_id": 10, "module_id": 29},
    {"id": 34, "formation_year_id": 10, "module_id": 30},
    {"id": 35, "formation_year_id": 10, "module_id": 31},
    {"id": 36, "formation_year_id": 11, "module_id": 32},
    {"id": 37, "formation_year_id": 11, "module_id": 33},
    {"id": 38, "formation_year_id": 11, "module_id": 34},
    {"id": 39, "formation_year_id": 12, "module_id": 35},
    {"id": 40, "formation_year_id": 12, "module_id": 36},
    {"id": 41, "formation_year_id": 12, "module_id": 37},
    {"id": 42, "formation_year_id": 13, "module_id": 38},
    {"id": 43, "formation_year_id": 13, "module_id": 39},
    {"id": 44, "formation_year_id": 13, "module_id": 40},
    {"id": 45, "formation_year_id": 14, "module_id": 41},
    {"id": 46, "formation_year_id": 14, "module_id": 42},
    {"id": 47, "formation_year_id": 14, "module_id": 8},
    
]

# =========================
# GROUPS (3–4 per formation year)
# =========================
groups = [
    # Formation Year 1
    {"id": 1, "group_number": 1, "formation_year_id": 1},
    {"id": 2, "group_number": 2, "formation_year_id": 1},
    {"id": 3, "group_number": 3, "formation_year_id": 1},

    # Formation Year 2
    {"id": 4, "group_number": 1, "formation_year_id": 2},
    {"id": 5, "group_number": 2, "formation_year_id": 2},
    {"id": 6, "group_number": 3, "formation_year_id": 2},
    {"id": 7, "group_number": 4, "formation_year_id": 2},

    # Formation Year 3
    {"id": 8, "group_number": 1, "formation_year_id": 3},
    {"id": 9, "group_number": 2, "formation_year_id": 3},
    {"id": 10, "group_number": 3, "formation_year_id": 3},

    # Formation Year 4
    {"id": 11, "group_number": 1, "formation_year_id": 4},
    {"id": 12, "group_number": 2, "formation_year_id": 4},
    {"id": 13, "group_number": 3, "formation_year_id": 4},
    {"id": 14, "group_number": 4, "formation_year_id": 4},

    # Formation Year 5
    {"id": 15, "group_number": 1, "formation_year_id": 5},
    {"id": 16, "group_number": 2, "formation_year_id": 5},
    {"id": 17, "group_number": 3, "formation_year_id": 5},

    # Formation Year 6
    {"id": 18, "group_number": 1, "formation_year_id": 6},
    {"id": 19, "group_number": 2, "formation_year_id": 6},
    {"id": 20, "group_number": 3, "formation_year_id": 6},
    {"id": 21, "group_number": 4, "formation_year_id": 6},

    # Formation Year 7
    {"id": 22, "group_number": 1, "formation_year_id": 7},
    {"id": 23, "group_number": 2, "formation_year_id": 7},
    {"id": 24, "group_number": 3, "formation_year_id": 7},

    # Formation Year 8
    {"id": 25, "group_number": 1, "formation_year_id": 8},
    {"id": 26, "group_number": 2, "formation_year_id": 8},
    {"id": 27, "group_number": 3, "formation_year_id": 8},
    {"id": 28, "group_number": 4, "formation_year_id": 8},

    # Formation Year 9
    {"id": 29, "group_number": 1, "formation_year_id": 9},
    {"id": 30, "group_number": 2, "formation_year_id": 9},
    {"id": 31, "group_number": 3, "formation_year_id": 9},

    # Formation Year 10
    {"id": 32, "group_number": 1, "formation_year_id": 10},
    {"id": 33, "group_number": 2, "formation_year_id": 10},
    {"id": 34, "group_number": 3, "formation_year_id": 10},
    {"id": 35, "group_number": 4, "formation_year_id": 10},

    # Formation Year 11
    {"id": 36, "group_number": 1, "formation_year_id": 11},
    {"id": 37, "group_number": 2, "formation_year_id": 11},
    {"id": 38, "group_number": 3, "formation_year_id": 11},

    # Formation Year 12
    {"id": 39, "group_number": 1, "formation_year_id": 12},
    {"id": 40, "group_number": 2, "formation_year_id": 12},
    {"id": 41, "group_number": 3, "formation_year_id": 12},
    {"id": 42, "group_number": 4, "formation_year_id": 12},

    # Formation Year 13
    {"id": 43, "group_number": 1, "formation_year_id": 13},
    {"id": 44, "group_number": 2, "formation_year_id": 13},
    {"id": 45, "group_number": 3, "formation_year_id": 13},

    # Formation Year 14
    {"id": 46, "group_number": 1, "formation_year_id": 14},
    {"id": 47, "group_number": 2, "formation_year_id": 14},
    {"id": 48, "group_number": 3, "formation_year_id": 14},
    {"id": 49, "group_number": 4, "formation_year_id": 14},
]


# =========================
# PROFESSORS (34)
# =========================
professors = []
for i in range(1, 35):
    professors.append({
        "id": i,
        "first_name": f"Prof{i}",
        "last_name": "Teacher",
        "department_id": 1 if i <= 17 else 2,
        "matricule": f"PROF{i:03}"
    })

# =========================
# CLASSROOMS
# 5 Amphi (40), 6 Class (20)
# =========================
classrooms = []

for i in range(1, 6):
    classrooms.append({
        "id": i,
        "name": f"Amphi {i}",
        "capacity": 40,
        "type": "amphi",
        "department_id": 1
    })

for i in range(6, 12):
    classrooms.append({
        "id": i,
        "name": f"Class {i}",
        "capacity": 20,
        "type": "class",
        "department_id": 2
    })

# =========================
# EXAMS
# =========================
exams = [
    {"id": 8,  "module_id": 23,  "exam_date": date(2025, 12, 24), "exam_time": time(13, 45)},
    # {"id": 9,  "module_id": 23, "exam_date": date(2025, 12, 24), "exam_time": time(13, 45)},
    # {"id": 10, "module_id": 2,  "exam_date": date(2025, 12, 29), "exam_time": time(13, 45)},
    # {"id": 11, "module_id": 8,  "exam_date": date(2026, 1, 1),   "exam_time": time(13, 45)},
    # {"id": 12, "module_id": 36, "exam_date": date(2026, 1, 3),   "exam_time": time(13, 45)},
    # {"id": 13, "module_id": 3,  "exam_date": date(2026, 1, 5),   "exam_time": time(13, 45)},
    # {"id": 14, "module_id": 29, "exam_date": date(2025, 12, 24),   "exam_time": time(13, 45)},
    # {"id": 10, "module_id": 2,  "exam_date": date(2025, 12, 25), "exam_time": time(13, 45)},
    # {"id": 11, "module_id": 8,  "exam_date": date(2025, 12, 24),   "exam_time": time(13, 45)},
    # {"id": 12, "module_id": 36, "exam_date": date(2025, 12, 24),   "exam_time": time(13, 45)},
    # {"id": 13, "module_id": 3,  "exam_date": date(2025, 12, 24),   "exam_time": time(13, 45)},
]


# =========================
# EXAM SESSIONS
# =========================
exam_sessions = [
    {"id": '8_1', "exam_id": 8,  "classroom_id": 1, "group_id": 1, "part": None},
    # {"id": 3, "exam_id": 9,  "classroom_id": 2, "group_id": 2, "part": 1},
    # {"id": 4, "exam_id": 11, "classroom_id": 3, "group_id": 1, "part": 1},
    # {"id": 5, "exam_id": 10, "classroom_id": 4, "group_id": 1, "part": 1},
    # {"id": 6, "exam_id": 13, "classroom_id": 7, "group_id": 1, "part": 1},
]

# =========================
# EXAM SUPERVISIONS
# =========================
exam_supervisions = [
    {"id": 1, "exam_session_id": '8_1', "professor_id": 1},
    # {"id": 2, "exam_session_id": 2, "professor_id": 2},
    # {"id": 3, "exam_session_id": 2, "professor_id": 34},
    # {"id": 4, "exam_session_id": 3, "professor_id": 34},
    # {"id": 5, "exam_session_id": 3, "professor_id": 23},
    # {"id": 6, "exam_session_id": 3, "professor_id": 1},
    # {"id": 7, "exam_session_id": 4, "professor_id": 1},
]

# =========================
# FINAL OBJECT
# =========================
fake_db = {
    "roles": roles,
    "departments": departments,
    "formations": formations,
    "formation_years": formation_years,
    "modules": modules,
    "formation_year_modules": formation_year_modules,
    "groups": groups,
    "professors": professors,
    "classrooms": classrooms,
    "exams": exams,
    "exam_sessions": exam_sessions,
    "exam_supervisions": exam_supervisions
}
