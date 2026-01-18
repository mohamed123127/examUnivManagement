from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base

class FormationYearModule(Base):
    __tablename__ = "formation_year_modules"
    id = Column(Integer, primary_key=True, autoincrement=True)
    formation_year_id = Column(Integer, ForeignKey("formation_years.id"), nullable=False)
    module_id = Column(Integer, ForeignKey("modules.id"), nullable=False)

    formation_year = relationship("FormationYear", back_populates="formation_year_modules")
    module = relationship("Module", back_populates="formation_year_modules")