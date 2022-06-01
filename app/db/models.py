from sqlalchemy import Column, Float, String

from .database import Base

class AIResult(Base):
    __tablename__ = "results"

    digest = Column(String, primary_key=True, index=True)
    plant = Column(String)
    accuracy = Column(Float)