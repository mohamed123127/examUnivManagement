from sqlalchemy import Column, Integer, String, ForeignKey, Date, Time
from sqlalchemy.orm import relationship
from .base import Base

class Exam(Base):
    __tablename__ = "exams"
    id = Column(Integer, primary_key=True, autoincrement=True)
    module_id = Column(Integer, ForeignKey("modules.id"), nullable=False)
    exam_date = Column(Date, nullable=False)
    exam_time = Column(Time, nullable=False)

    module = relationship("Module", back_populates="exams")
    exam_sessions = relationship("ExamSession", back_populates="exam")