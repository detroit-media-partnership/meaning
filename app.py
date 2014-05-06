import os
from flask import Flask
from flask import render_template
from database import db_session
from forms import MeaningForm

app = Flask(__name__)
app.debug = True

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

@app.teardown_appcontext
def shutdown_session(exception=None):
	db_session.remove()

@app.route('/')
def intro():
	return render_template('intro.html')

@app.route('/submit')
def submit():
	form = MeaningForm()
	return render_template('submit.html', form=form)

@app.route('complete', methods=['GET', 'POST'])
def complete():
	form = MeaningForm()
	if not form.validate_on_submit():
		pass

if __name__ == '__main__':
	app.run()
