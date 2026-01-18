from sqlalchemy.orm import Session,joinedload
from models.exam_session import ExamSession
from models.exam import Exam
from models.exam_supervision import ExamSupervision
from models.module import Module
from models.classroom import Classroom


def getExamsSchedule(professor_id: int, db: Session):
    subq = (
        db.query(ExamSupervision.exam_session_id)
        .filter(ExamSupervision.professor_id == professor_id)
        .subquery()
    )

    sessions = (
        db.query(ExamSession)
        .join(Exam, ExamSession.exam_id == Exam.id)
        .join(Module, Exam.module_id == Module.id)
        .join(Classroom, ExamSession.classroom_id == Classroom.id)
        .filter(ExamSession.id.in_(subq))
        .all()
    )

    result = []
    for s in sessions:
        result.append({
            "module_name": s.exam.module.name,
            "classroom": s.classroom.name,
            "date": str(s.exam.exam_date),
            "time": str(s.exam.exam_time),
        })
        
    return result