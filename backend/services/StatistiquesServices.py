from sqlalchemy.orm import Session
from sqlalchemy import func
from models import Student, Professor, Classroom, Formation, Module,Exam,ExamSession,ExamSupervision,FormationYear,FormationYearModule,Group

class StatsService:

    @staticmethod
    def get_general_stats(db: Session, department_id: int | None = None):
        # Total students (فلترة حسب department_id إذا تم تمريره)
        total_students_query = db.query(func.count(Student.id))
        if department_id is not None:
            total_students_query = total_students_query.join(
                Group, Student.group_id == Group.id
            ).join(
                FormationYear, Group.formation_year_id == FormationYear.id
            ).join(
                Formation, FormationYear.formation_id == Formation.id
            ).filter(
                Formation.department_id == department_id
            )
        total_students = total_students_query.scalar() or 0

        # Total professors
        total_professors_query = db.query(func.count(Professor.id))
        if department_id is not None:
            # إذا Professor مرتبط بـ Formation، نفعل join مشابه
            total_professors_query = total_professors_query.filter(
                Professor.department_id == department_id
            )
        total_professors = total_professors_query.scalar() or 0

        # Total formations
        total_formations_query = db.query(func.count(Formation.id))
        if department_id is not None:
            total_formations_query = total_formations_query.filter(Formation.department_id == department_id)
        total_formations = total_formations_query.scalar() or 0

        # Total modules
        total_modules_query = db.query(func.count(Module.id))
        if department_id is not None:
            total_modules_query = total_modules_query.join(
                FormationYearModule, Module.id == FormationYearModule.module_id
            ).join(
                FormationYear, FormationYearModule.formation_year_id == FormationYear.id
            ).join(
                Formation, FormationYear.formation_id == Formation.id
            ).filter(
                Formation.department_id == department_id
            )
        total_modules = total_modules_query.scalar() or 0

        # Classroom types occupation rate
        classrooms_query = db.query(
            Classroom.type, func.count(Classroom.id).label("occupation_rate")
        ).filter(Classroom.department_id==department_id if department_id is not None else True
        ).group_by(Classroom.type)
        classrooms_list = [
            {"type": c.type, "occupation_rate": float(c.occupation_rate)}
            for c in classrooms_query.all()
        ]

        return {
            "total_students": total_students,
            "total_professors": total_professors,
            "total_formations": total_formations,
            "total_modules": total_modules,
            "classrooms_by_type": classrooms_list
        }

    @staticmethod
    def get_student_groups_stats(db: Session, department_id: int | None = None):
        # Subquery: number of students per group
        subquery = (
            db.query(func.count(Student.id).label("student_count"))
            .join(Group,Student.group_id==Group.id)
            .join(FormationYear, Group.formation_year_id == FormationYear.id)
            .join(Formation, FormationYear.formation_id == Formation.id)
            .filter(Formation.department_id==department_id if department_id is not None else True)
            .group_by(Student.group_id)
            .subquery()
        )

        # Outer query: how many groups have same student count
        results = (
            db.query(
                subquery.c.student_count.label("studentPerGroup"),
                func.count().label("group_repetition")
            )
            .group_by(subquery.c.student_count)
            .order_by(subquery.c.student_count.desc())
            .all()
        )

        return [
            {"studentPerGroup": r.studentPerGroup, "group_repetition": r.group_repetition}
            for r in results
        ]

    @staticmethod
    def get_exams_stats(db: Session, department_id: int | None = None):

        # =========================
        # Base Exam Query (with joins)
        # =========================
        exam_query = (
            db.query(Exam)
            .join(
                FormationYearModule,
                Exam.module_id == FormationYearModule.module_id
            )
            .join(
                FormationYear,
                FormationYearModule.formation_year_id == FormationYear.id
            )
            .join(
                Formation,
                FormationYear.formation_id == Formation.id
            )
        )

        if department_id is not None:
            exam_query = exam_query.filter(Formation.department_id == department_id)

        exam_ids_subquery = exam_query.with_entities(Exam.id).subquery()

        # =========================
        # Total exams
        # =========================
        total_exams = db.query(func.count()).select_from(exam_ids_subquery).scalar() or 0

        # =========================
        # Total exam sessions
        # =========================
        total_exam_sessions = (
            db.query(func.count(ExamSession.id))
            .filter(ExamSession.exam_id.in_(exam_ids_subquery))
            .scalar() or 0
        )

        # =========================
        # Occupied classrooms per day
        # =========================
        used_classes = (
            db.query(func.count(ExamSession.classroom_id))
            .filter(ExamSession.exam_id.in_(exam_ids_subquery))
            .scalar() or 0
        )

        total_days = (
            db.query(func.count(func.distinct(Exam.exam_date)))
            .filter(Exam.id.in_(exam_ids_subquery))
            .scalar() or 1
        )

        occupied_classrooms_per_day = used_classes / total_days

        # =========================
        # Average sessions per professor
        # =========================
        subquery = (
            db.query(
                ExamSupervision.professor_id,
                func.count(ExamSupervision.id).label("sessions_count")
            )
            .join(
                ExamSession,
                ExamSupervision.exam_session_id == ExamSession.id
            )
            .filter(ExamSession.exam_id.in_(exam_ids_subquery))
            .group_by(ExamSupervision.professor_id)
            .subquery()
        )

        avg_sessions = (
            db.query(func.avg(subquery.c.sessions_count))
            .scalar() or 0
        )


        return {
            "total_exams": total_exams,
            "total_exam_sessions": total_exam_sessions,
            "salles_per_day": float(occupied_classrooms_per_day),
            "avg_sessions_per_prof": float(avg_sessions)
        }

    @staticmethod
    def get_most_used_hours(db: Session, department_id: int | None = None):
        # exams grouped by time
        query = (db.query(Exam.exam_time, func.count(Exam.id))
                   .join(FormationYearModule, Exam.module_id == FormationYearModule.module_id)
            .join(FormationYear, FormationYearModule.formation_year_id == FormationYear.id)
            .join(Formation, FormationYear.formation_id == Formation.id)
        .group_by(Exam.exam_time))

        
        if department_id is not None:
            query = query.filter(Formation.department_id == department_id)
        results = query.all()

        return [{"exam_time": r[0], "count": r[1]} for r in results]

    @staticmethod
    def get_exam_per_department(db: Session, department_id: int | None = None):
        query = (
            db.query(
                func.count(Exam.id).label("examPerDept"),
                Formation.department_id
            )
            .join(FormationYearModule, Exam.module_id == FormationYearModule.module_id)
            .join(FormationYear, FormationYearModule.formation_year_id == FormationYear.id)
            .join(Formation, FormationYear.formation_id == Formation.id)
            .group_by(Formation.department_id)            
        )
        if department_id is not None:
            query = query.filter(Formation.department_id == department_id)
        results = query.all()

        return [{"department_id": r[1], "examPerDept": r[0]} for r in results]