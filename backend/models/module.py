from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from .base import Base

class Module(Base):
    __tablename__ = "modules"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)

    exams = relationship("Exam", back_populates="module")
    formation_year_modules = relationship("FormationYearModule", back_populates="module")