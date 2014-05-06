from sqlalchemy import Column, Integer, String, Text, Date, func
from database import Base

class Meaning(Base):
	__tablename__ = 'meaning'
	id = Column(Integer, primary_key=True)
	
