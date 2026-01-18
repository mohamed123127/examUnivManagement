from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base

class ExamSession(Base):
    __tablename__ = "exam_sessions"
    id = Column(Integer, primary_key=True, autoincrement=True)
    exam_id = Column(Integer, ForeignKey("exams.id"), nullable=False)
    classroom_id = Column(Integer, ForeignKey("classrooms.id"), nullable=False)
    group_id = Column(Integer, ForeignKey("groups.id"), nullable=False)
    part = Column(Integer, default=1)

    exam = relationship("Exam", back_populates="exam_sessions")
    classroom = relationship("Classroom", back_populates="exam_sessions")
    group = relationship("Group", back_populates="exam_sessions")
    exam_supervisions = relationship("ExamSupervision", back_populates="exam_session")