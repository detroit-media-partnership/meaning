import os
from flask import Flask
from flask import render_template
from database import db_session

app = Flask(__name__)
app.debug = True

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

@app.teardown_appcontext
def shutdown_session(exception=None):
	db_session.remove()

@app.route('/')
def intro():
	return 'Hello!'

if __name__ == '__main__':
	app.run()
