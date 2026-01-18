from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base

class Group(Base):
    __tablename__ = "groups"
    id = Column(Integer, primary_key=True, autoincrement=True)
    group_number = Column(Integer, nullable=False)
    formation_year_id = Column(Integer, ForeignKey("formation_years.id"), nullable=False)

    formation_year = relationship("FormationYear", back_populates="groups")
    students = relationship("Student", back_populates="group")
    exam_sessions = relationship("ExamSession", back_populates="group")