from typing import Optional
from datetime import datetime, date, time
from sqlalchemy.orm import Session
from sqlalchemy import func, distinct
from models.formation_year import FormationYear
from models.formation import Formation
from models.department import Department
from models.group import Group
from models.formation_year_module import FormationYearModule
from models.module import Module
from models.classroom import Classroom
from models.professor import Professor
from models.exam_session import ExamSession
from models.exam import Exam
from models.exam_supervision import ExamSupervision


def getAllFormationYearsData(
    db: Session,
    department_id: Optional[int] = None,
    formation_id: Optional[int] = None,
    year: Optional[str] = None,
    page: int = 1,
    page_size: int = 10
):

    base_query = (
        db.query(
            FormationYear.id.label("formation_year_id"),
            Formation.name.label("formation_name"),
            FormationYear.year.label("formation_year"),
            func.count(distinct(Group.id)).label("total_groups"),
            func.count(distinct(FormationYearModule.module_id)).label("total_modules"),
            Department.name.label("dept_name"),
        )
        .join(Formation, FormationYear.formation_id == Formation.id)
        .join(Department, Formation.department_id == Department.id)
        .join(Group, FormationYear.id == Group.formation_year_id)
        .join(FormationYearModule, FormationYear.id == FormationYearModule.formation_year_id)
        .group_by(FormationYear.id)
        .order_by(Department.name.asc())  # <<< ORDER BY DEPARTMENT
    )

    if department_id is not None:
        base_query = base_query.filter(Department.id == department_id)

    if formation_id is not None:
        base_query = base_query.filter(Formation.id == formation_id)
    
    if year is not None:
        base_query = base_query.filter(FormationYear.year == year)

    total_items = base_query.count()

    offset = (page - 1) * page_size
    rows = base_query.offset(offset).limit(page_size).all()

    data = []
    for r in rows:
        data.append({
            "formation_year_id": r.formation_year_id,
            "formation_name": r.formation_name,
            "formation_year": r.formation_year,
            "total_groups": r.total_groups,
            "total_modules": r.total_modules,
            "department_name": r.dept_name,
        })

    return {
        "page": page,
        "page_size": page_size,
        "total_items": total_items,
        "total_pages": (total_items + page_size - 1) // page_size,
        "items": data
    }

def getModulesByFormationYear(db: Session, formation_year_id: int):
        rows = (
            db.query(
                Module.id.label("module_id"),
                Module.name.label("module_name")
            )
            .join(FormationYearModule, FormationYearModule.module_id == Module.id)
            .filter(FormationYearModule.formation_year_id == formation_year_id)
            .order_by(Module.name.asc())
            .all()
        )

        return [{"id": r.module_id, "name": r.module_name} for r in rows]

def getAvailableProfessors(db: Session, date: str):
    subquery = (
        db.query(ExamSupervision.professor_id)
        .join(ExamSession, ExamSession.id == ExamSupervision.exam_session_id)
        .join(Exam, Exam.id == ExamSession.exam_id)
        .filter(Exam.exam_date == date)
        .group_by(ExamSupervision.professor_id, Exam.exam_date)
        .having(func.count(ExamSession.exam_time) > 2)
    )

    rows = (
        db.query(
            Professor.id.label("id"),
            func.concat(Professor.first_name, " ", Professor.last_name).label("name")
        )
        .filter(~Professor.id.in_(subquery))
        .order_by(Professor.last_name.asc())
        .all()
    )

    return [{"id": r.id, "name": r.name} for r in rows]


def getAvailableClassrooms(db: Session, date: str, time: str):
    rows = (
        db.query(Classroom.id.label("id"), Classroom.name.label("name"))
        .filter(
            ~Classroom.id.in_(
                db.query(ExamSession.classroom_id)
                .join(Exam, Exam.id == ExamSession.exam_id)
                .filter(Exam.exam_date == date, Exam.exam_time == time)
            )
        )
        .order_by(Classroom.name.asc())
        .all()
    )
    return [{"id": r.id, "name": r.name} for r in rows]


def getExamsByFormationYear(db: Session, formation_year_id: int):
    rows = (
        db.query(
            Exam.id.label("exam_id"),
            Module.id.label("module_id"),
            Module.name.label("module_name"),
            Exam.exam_date,
            Exam.exam_time,
            func.count(distinct(ExamSession.classroom_id)).label("total_classrooms"),
            func.count(distinct(ExamSupervision.professor_id)).label("total_profs"),
        )
        .join(Module, Exam.module_id == Module.id)
        .join(FormationYearModule, FormationYearModule.module_id == Module.id)
        .join(ExamSession, Exam.id == ExamSession.exam_id)
        .join(ExamSupervision, ExamSession.id == ExamSupervision.exam_session_id)
        .filter(FormationYearModule.formation_year_id == formation_year_id)
        .group_by(
            Exam.id,
            Module.id,
            Module.name,
            Exam.exam_date,
            Exam.exam_time,
        )
        .order_by(Module.name.asc())
        .all()
    )

    return [
        {
            "exam_id": r.exam_id,
            "module_id": r.module_id,
            "module_name": r.module_name,
            "date": r.exam_date,
            "time": r.exam_time,
            "total_classrooms": r.total_classrooms,
            "total_profs": r.total_profs,
        }
        for r in rows
    ]
