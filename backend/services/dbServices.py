# fake_db_from_sql.py
from dbSetup import SessionLocal
from datetime import date, time
from sqlalchemy import text

db_name="university_exam_planning_db"

db = SessionLocal()

def load_db_to_memory():
    fake_db = {}

    try:
        # ROLES
        roles = db.execute(text("SELECT id, name FROM roles")).fetchall()
        fake_db["roles"] = [{"id": r.id, "name": r.name} for r in roles]

        # DEPARTMENTS
        depts = db.execute(text("SELECT id, name FROM departments")).fetchall()
        fake_db["departments"] = [{"id": d.id, "name": d.name} for d in depts]

        # FORMATIONS
        formations = db.execute(text("SELECT id, name, department_id FROM formations")).fetchall()
        fake_db["formations"] = [{"id": f.id, "name": f.name, "department_id": f.department_id} for f in formations]

        # FORMATION YEARS
        fyears = db.execute(text("SELECT id, formation_id, year FROM formation_years")).fetchall()
        fake_db["formation_years"] = [{"id": fy.id, "formation_id": fy.formation_id, "year": fy.year} for fy in fyears]

        # MODULES
        modules = db.execute(text("SELECT id, name FROM modules")).fetchall()
        fake_db["modules"] = [{"id": m.id, "name": m.name} for m in modules]

        # FORMATION YEAR MODULES
        fymods = db.execute(text("SELECT id, formation_year_id, module_id FROM formation_year_modules")).fetchall()
        fake_db["formation_year_modules"] = [{"id": fm.id, "formation_year_id": fm.formation_year_id, "module_id": fm.module_id} for fm in fymods]

        # GROUPS
        groups = db.execute(text("SELECT id, group_number, formation_year_id FROM `groups`")).fetchall()
        fake_db["groups"] = [{"id": g.id, "group_number": g.group_number, "formation_year_id": g.formation_year_id} for g in groups]

        # PROFESSORS
        profs = db.execute(text("SELECT id, first_name, last_name, department_id, matricule FROM professors")).fetchall()
        fake_db["professors"] = [{"id": p.id, "first_name": p.first_name, "last_name": p.last_name,
                                  "department_id": p.department_id, "matricule": p.matricule} for p in profs]

        # CLASSROOMS
        classrooms = db.execute(text("SELECT id, name, capacity, type, department_id FROM classrooms")).fetchall()
        fake_db["classrooms"] = [{"id": c.id, "name": c.name, "capacity": c.capacity, "type": c.type, "department_id": c.department_id} for c in classrooms]

        # STUDENTS
        students = db.execute(text("SELECT id, first_name, last_name, group_id, matricule FROM students")).fetchall()
        fake_db["students"] = [{"id": s.id, "first_name": s.first_name, "last_name": s.last_name,
                                "group_id": s.group_id, "matricule": s.matricule} for s in students]

        # USERS
        users = db.execute(text("SELECT id, matricule, password, role_id FROM users")).fetchall()
        fake_db["users"] = [{"id": u.id, "matricule": u.matricule, "password": u.password, "role_id": u.role_id} for u in users]

        # EXAMS
        exams = db.execute(text("SELECT id, module_id, exam_date, exam_time FROM exams")).fetchall()
        fake_db["exams"] = [{"id": e.id, "module_id": e.module_id,
                             "exam_date": e.exam_date if isinstance(e.exam_date, date) else None,
                              "exam_time": time(e.exam_time.seconds // 3600, (e.exam_time.seconds // 60) % 60) } for e in exams]

        # EXAM SESSIONS
        exam_sessions = db.execute(text("SELECT id, exam_id, classroom_id, group_id, part FROM exam_sessions")).fetchall()
        fake_db["exam_sessions"] = [{"id": es.id, "exam_id": es.exam_id, "classroom_id": es.classroom_id,
                                     "group_id": es.group_id, "part": es.part} for es in exam_sessions]

        # EXAM SUPERVISIONS
        exam_supervisions = db.execute(text("SELECT id, exam_session_id, professor_id FROM exam_supervisions")).fetchall()
        fake_db["exam_supervisions"] = [{"id": ex.id, "exam_session_id": ex.exam_session_id, "professor_id": ex.professor_id} for ex in exam_supervisions]

    finally:
        db.close()

    return fake_db

def get_next_auto_increment(table_name):
    global db_name
    try:
        if db_name is None:
            db_name = db.execute(text("SELECT DATABASE()")).scalar()

        query = text("""
            SELECT AUTO_INCREMENT
            FROM information_schema.TABLES
            WHERE TABLE_SCHEMA = :db_name
            AND TABLE_NAME = :table_name
        """)
        result = db.execute(query, {"db_name": db_name, "table_name": table_name}).scalar()
        return result if result is not None else 0
    finally:
        db.close()