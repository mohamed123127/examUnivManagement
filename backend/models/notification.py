from sqlalchemy import Column, Integer, String, Text
from .base import Base

class Notification(Base):
    __tablename__ = "notifications"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    message = Column(Text, nullable=True)
    type = Column(String(25), nullable=True)
