from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base

class FormationYear(Base):
    __tablename__ = "formation_years"
    id = Column(Integer, primary_key=True, autoincrement=True)
    formation_id = Column(Integer, ForeignKey("formations.id"), nullable=False)
    year = Column(String(30), nullable=False)

    formation = relationship("Formation", back_populates="formation_years")
    groups = relationship("Group", back_populates="formation_year")
    formation_year_modules = relationship("FormationYearModule", back_populates="formation_year")