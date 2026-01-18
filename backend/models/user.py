from sqlalchemy import Column, Integer, String, Enum, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base
import enum

class RoleEnum(str, enum.Enum):
    doyen = "Doyen"
    vice_doyen = "Vice-doyen"
    admin_exam = "Administrateur examens"
    chef_dept = "Chef de département"
    etudiant = "Étudiant"
    professeur = "Professeur"

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True)
    matricule = Column(String(100), nullable=False, unique=True)
    password = Column(String(256), nullable=False)

    role_id = Column(Integer, ForeignKey("roles.id"), nullable=False)

    role = relationship("Role", back_populates="users")
