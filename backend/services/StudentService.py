from sqlalchemy.orm import Session,joinedload
from models.exam_session import ExamSession
from models.exam import Exam
from models.exam_supervision import ExamSupervision
from models.module import Module

def getExamsSchedule(group_id, db):
        exams = db.query(ExamSession).options(
            joinedload(ExamSession.exam).joinedload(Exam.module),
            joinedload(ExamSession.exam_supervisions).joinedload(ExamSupervision.professor),
            joinedload(ExamSession.classroom)
            ).filter(ExamSession.group_id == group_id).all()
        exams.sort(key=lambda x: x.exam.exam_date)
        result = []
        for session in exams:
            result.append({
                "id": session.exam_id,
                "module_name": session.exam.module.name,
                "classroom": session.classroom.name,
                "date": str(session.exam.exam_date),
                "time": str(session.exam.exam_time),
                "supervisions": [
                    s.professor.last_name
                    
                    for s in session.exam_supervisions
                ]
            })
        return result