from sqlalchemy import Column, ForeignKey, Integer, String, DateTime, func
from sqlalchemy.orm import relationship
from database import Base

class Sessions(Base):
	__tablename__ = 'sessions'
	id = Column(Integer, primary_key=True)
	name = Column(String(100), nullable=True)
	created = Column(DateTime, default=func.now())

	def __init__(self, name=None):
		self.name = name

	def __repr__(self):
		return '<Session %r>' % (self.name)	

class Submissions(Base):
	__tablename__ = 'submissions'
	id = Column(Integer, primary_key=True)
	session_id = Column(Integer, ForeignKey('sessions.id'))
	ip = Column(String(15))
	created = Column(DateTime, default=func.now())
	session = relationship('Sessions', foreign_keys='Submissions.session_id')

	def __init__(self, session_id=None, ip='0.0.0.0'):
		self.session_id = session_id
		self.ip = ip

	def __repr__(self):
		return '<Submission %r>' % (self.ip)

class Responses(Base):
	__tablename__ = 'responses'
	id = Column(Integer, primary_key=True)
	submission_id = Column(Integer, ForeignKey('submissions.id'))
	phrase = Column(String(50))
	value = Column(Integer)
	submission = relationship('Submissions', foreign_keys='Responses.submission_id')

	def __init__(self, submission_id=None, phrase=None, value=None):
		self.submission_id = submission_id
		self.phrase = phrase
		self.value = value

	def __repr__(self):
		return '<Response %r>' % (self.id)
