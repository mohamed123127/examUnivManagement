from sqlalchemy import text
from sqlalchemy.orm import Session
from faker import Faker
import random

from dbSetup import SessionLocal  # <-- adjust if filename differs

fake = Faker()

# CONFIG
NUM_DEPARTMENTS = 7
NUM_STUDENTS = 13000
NUM_FORMATIONS = 200
MIN_MODULES = 6
MAX_MODULES = 9
AVG_GROUP_SIZE_MIN = 38
AVG_GROUP_SIZE_MAX = 44
NUM_PROFESSORS = 400
num_amphi = 75
num_class = 60


def sql_str(s):
    return "'" + str(s).replace("'", "''") + "'" if s is not None else "NULL"


def seed_database():
    user_id = 1
    student_id = 1
    prof_id = 1
    dept_id = 1
    formation_id = 1
    formation_year_id = 1
    group_id = 1
    module_id = 1
    classroom_id = 1

    insert_sql = []

    # ---------- ROLES ----------
    insert_sql.append(
        "INSERT INTO roles (id,name) VALUES (1, 'Étudiant'),(2, 'Professeur'),(3, 'Administrateur examens'),(4, 'Chef de département'),(5, 'Doyen'),(6, 'Vice-doyen');"
    )

    # ---------- DEPARTMENTS ----------
    for i in range(NUM_DEPARTMENTS):
        insert_sql.append(
            f"INSERT INTO departments (id,name) VALUES ({dept_id},{sql_str('Department '+str(dept_id))});"
        )
        dept_id += 1

    # ---------- FORMATIONS ----------
    dept_ids = list(range(1, NUM_DEPARTMENTS + 1))

    for i in range(NUM_FORMATIONS):
        d = random.choice(dept_ids)
        insert_sql.append(
            f"INSERT INTO formations (id,name,department_id) VALUES ({formation_id},{sql_str('Formation '+str(formation_id))},{d});"
        )
        formation_id += 1

    # ---------- FORMATION YEARS ----------
    formation_year_map = []

    for i in range(1, NUM_FORMATIONS + 1):
        y = random.choice(["L1", "L2", "L3", "M1", "M2"])
        insert_sql.append(
            f"INSERT INTO formation_years (id,formation_id,year) VALUES ({formation_year_id},{i},{sql_str(y)});"
        )
        formation_year_map.append(formation_year_id)
        formation_year_id += 1

    # ---------- MODULES + FormationYearModules ----------
    for fy in formation_year_map:
        n = random.randint(MIN_MODULES, MAX_MODULES)
        for j in range(n):
            insert_sql.append(
                f"INSERT INTO modules (id,name) VALUES ({module_id},{sql_str('Module '+str(module_id))});"
            )
            insert_sql.append(
                f"INSERT INTO formation_year_modules (formation_year_id,module_id) VALUES ({fy},{module_id});"
            )
            module_id += 1

    # ---------- GROUPS ----------
    groups = []
    total_students_remaining = NUM_STUDENTS

    for fy in formation_year_map:
        if total_students_remaining <= 0:
            break

        num_groups_here = random.randint(1, 3)

        for g in range(num_groups_here):
            if total_students_remaining <= 0:
                break

            groups.append(group_id)
            insert_sql.append(
                f"INSERT INTO groups (id,group_number,formation_year_id) VALUES ({group_id},{g+1},{fy});"
            )
            group_id += 1

    # ---------- CLASSROOMS ----------

    for i in range(num_amphi):
        d = random.choice(dept_ids)
        insert_sql.append(
            f"INSERT INTO classrooms (id,name,capacity,type,department_id) "
            f"VALUES ({classroom_id},{sql_str('Amphi '+str(classroom_id))},40,'amphi',{d});"
        )
        classroom_id += 1

    for i in range(num_class):
        d = random.choice(dept_ids)
        insert_sql.append(
            f"INSERT INTO classrooms (id,name,capacity,type,department_id) "
            f"VALUES ({classroom_id},{sql_str('Class '+str(classroom_id))},20,'class',{d});"
        )
        classroom_id += 1

    # ---------- USERS + STUDENTS ----------
    total_students_created = 0

    for g in groups:
        if total_students_created >= NUM_STUDENTS:
            break

        group_size = random.randint(AVG_GROUP_SIZE_MIN, AVG_GROUP_SIZE_MAX)

        for i in range(group_size):
            if total_students_created >= NUM_STUDENTS:
                break

            matricule = "STU" + str(100000 + student_id)

            insert_sql.append(
                f"INSERT INTO users (id,matricule,password,role_id) "
                f"VALUES ({user_id},{sql_str(matricule)},{sql_str('hashed-password')},1);"
            )

            insert_sql.append(
                f"INSERT INTO students (id,first_name,last_name,group_id,matricule) "
                f"VALUES ({student_id},{sql_str(fake.first_name())},{sql_str(fake.last_name())},{g},{sql_str(matricule)});"
            )

            user_id += 1
            student_id += 1
            total_students_created += 1

    # ---------- PROFESSORS ----------
    for i in range(NUM_PROFESSORS):
        d = random.choice(dept_ids)
        matricule = "PRF" + str(100000 + prof_id)

        insert_sql.append(
            f"INSERT INTO users (id,matricule,password,role_id) "
            f"VALUES ({user_id},{sql_str(matricule)},{sql_str('hashed-password')},2);"
        )

        insert_sql.append(
            f"INSERT INTO professors (id,first_name,last_name,department_id,matricule) "
            f"VALUES ({prof_id},{sql_str(fake.first_name())},{sql_str(fake.last_name())},{d},{sql_str(matricule)});"
        )

        user_id += 1
        prof_id += 1

    # ---------- ADMINSTRATION ----------

    insert_sql.append(
        "INSERT INTO `administration` (`id`, `matricule`, `first_name`, `last_name`, `department_id`) VALUES(4, 'CDI111022', 'Youcef', 'Yahyatain', 1),(6, 'PLE294771', 'Zayed', 'Mekdad', 1),(7, 'D12784633', 'abdellah', 'lmohsen', NULL),(8, 'VD6482512', 'jaafar', 'khadour', NULL);"
    )

    # ---------- EXECUTE IN DATABASE ----------
    session: Session = SessionLocal()
    try:
        for stmt in insert_sql:
            session.execute(text(stmt))
        session.commit()
        print("Database seeded successfully.")
    except Exception as e:
        session.rollback()
        print("Error:", e)
    finally:
        session.close()


if __name__ == "__main__":
    seed_database()
