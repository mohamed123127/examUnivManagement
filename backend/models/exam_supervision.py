from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base

class ExamSupervision(Base):
    __tablename__ = "exam_supervisions"
    id = Column(Integer, primary_key=True, autoincrement=True)
    exam_session_id = Column(Integer, ForeignKey("exam_sessions.id"), nullable=False)
    professor_id = Column(Integer, ForeignKey("professors.id"), nullable=False)

    exam_session = relationship("ExamSession", back_populates="exam_supervisions")
    professor = relationship("Professor", back_populates="exam_supervisions")