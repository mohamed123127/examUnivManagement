from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from .base import Base

class Department(Base):
    __tablename__ = "departments"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)

    classrooms = relationship("Classroom", back_populates="department")
    formations = relationship("Formation", back_populates="department")
    professors = relationship("Professor", back_populates="department")
    administration = relationship("Administration", back_populates="department")
