from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base

class Professor(Base):
    __tablename__ = "professors"

    id = Column(Integer, primary_key=True, autoincrement=True)
    matricule = Column(String(100), ForeignKey("users.matricule"), nullable=False, unique=True)  # <-- LINK HERE
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    department_id = Column(Integer, ForeignKey("departments.id"), nullable=False)

    department = relationship("Department", back_populates="professors")
    exam_supervisions = relationship("ExamSupervision", back_populates="professor")
    user = relationship("User", uselist=False, viewonly=True, primaryjoin="Professor.matricule==User.matricule")

