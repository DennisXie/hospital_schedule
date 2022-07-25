from sqlalchemy import Column, Integer, String, Boolean
from base import Base


class DoctorPo(Base):

    __tablename__ = "doctor"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, unique=True, nullable=False)
    schedule = Column(Boolean, nullable=False)
    enabled = Column(Boolean, nullable=False)
