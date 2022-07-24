from sqlalchemy import Column, Integer, Date, Boolean
from .base import Base


class AssignmentPo(Base):

    __tablename__ = "assignment"

    id = Column(Integer, primary_key=True, autoincrement=True)
    date = Column(Date, unique=True, nullable=False)
    doctor_id = Column(Integer, nullable=True)
    holiday = Column(Boolean, nullable=False)
    ignore = Column(Boolean, nullable=False)
