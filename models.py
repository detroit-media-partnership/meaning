from sqlalchemy import Column, ForeignKey, Integer, String, Date, func
from sqlalchemy.orm import relationship
from database import Base

class Submissions(Base):
	__tablename__ = 'submissions'
	id = Column(Integer, primary_key=True)
	ip = Column(String(15))
	created = Column(Date, default=func.now())

	def __init__(self, ip='0.0.0.0'):
		self.ip = ip

	def __repr__(self):
		return '<Submission %r>' % (self.ip)

class Responses(Base):
	__tablename__ = 'responses'
	id = Column(Integer, primary_key=True)
	submission_id = Column(Integer, ForeignKey('submissions.id'))
	word = Column(String(50))
	value = Column(Integer)
	submission = relationship('Submissions', foreign_keys='Responses.submission_id')

	def __init__(self, submission_id=None, word=None, value=None):
		self.submission_id = submission_id
		self.word = word
		self.value = value

	def __repr__(self):
		return '<Response %r>' % (self.id)
