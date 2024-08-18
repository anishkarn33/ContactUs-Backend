from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from database import Base

class ContactRequest(Base):
    __tablename__ = "contact_request"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)
    message = Column(String)