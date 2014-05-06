import os
from flask import Flask
from flask import render_template
from database import db_session
from forms import MeaningForm

app = Flask(__name__)
app.debug = True
app.secret_key ='\xa2\xf2\xa8\xdb/\xf3\xae\xdd\xf6\xe2u"Ph\x12:\xa8\xa2\xf8:\x8fTMr'

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

@app.teardown_appcontext
def shutdown_session(exception=None):
	db_session.remove()

@app.route('/')
def intro():
	return render_template('intro.html')

@app.route('/survey')
def submit():
	form = MeaningForm()
	return render_template('survey.html', form=form)

@app.route('/complete', methods=['GET', 'POST'])
def complete():
	form = MeaningForm()
	if not form.validate_on_submit():
		pass

@app.route('/results', methods=['GET', 'POST'])
def results():
	return render_template('results.html')

if __name__ == '__main__':
	app.run()
