import os
import meaning
from database import init_db
import unittest
import tempfile

class MeaningTestCase(unittest.TestCase):
	
	def setUp(self):
		self.db_fd, meaning.app.config['DATABASE'] = tempfile.mkstemp()
		meaning.app.config['TESTING'] = True
		self.app = meaning.app.test_client()
		init_db()

	def tearDown(self):
		os.close(self.db_fd)
		os.unlink(meaning.app.config['DATABASE'])

	def test_empty_db(self):
		rv = self.app.get('/')
		print rv.data
		#assert 'No entries here so far' in rv.data

if __name__ == '__main__':
	unittest.main()
