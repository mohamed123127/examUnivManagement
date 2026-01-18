from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base

class Classroom(Base):
    __tablename__ = "classrooms"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    capacity = Column(Integer, nullable=False)
    type = Column(String(50))
    department_id = Column(Integer, ForeignKey("departments.id"))

    department = relationship("Department", back_populates="classrooms")
    exam_sessions = relationship("ExamSession", back_populates="classroom")