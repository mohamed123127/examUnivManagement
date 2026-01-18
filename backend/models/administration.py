from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base

class Administration(Base):
    __tablename__ = "administration"

    id = Column(Integer, primary_key=True, autoincrement=True)
    matricule = Column(String(100), ForeignKey("users.matricule"), nullable=False, unique=True)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    department_id = Column(Integer, ForeignKey("departments.id"), nullable=False)

    department = relationship("Department", back_populates="administration")
    user = relationship("User", uselist=False, viewonly=True, primaryjoin="Administration.matricule==User.matricule")

