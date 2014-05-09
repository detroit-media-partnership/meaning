from __future__ import division
import os
from flask import Flask, render_template, request
from database import db_session
from models import Submissions, Responses
from forms import MeaningForm

app = Flask(__name__)
app.debug = True
app.secret_key ='\xa2\xf2\xa8\xdb/\xf3\xae\xdd\xf6\xe2u"Ph\x12:\xa8\xa2\xf8:\x8fTMr'
#app.config['SQLALCHEMY_POOL_RECYCLE'] = 40

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
		return render_template('survey.html', form=form)
	
	submission = Submissions(ip=request.remote_addr)
	db_session.add(submission)
	db_session.commit()
	
	for field in form:
		if field.name == "csrf_token":
			continue
		response = Responses(
			submission_id=submission.id,
			phrase=field.label.text,
			value=field.data
		)
		db_session.add(response)
		db_session.commit()
	
	return render_template('survey.html', success=True)		

@app.route('/results', defaults={"date": None})
@app.route('/results/<date>')
def results(date):
	from time import strftime
	if date == "overall":
		responses = Responses.query.all()
	else:
		responses = Responses.query.filter(Responses.submission.has(Submissions.created==strftime("%Y-%m-%d"))).all()
	
	aggregate_phrases = []
	for res in responses:
		found = False
		for phrase in aggregate_phrases:
			if res.phrase == phrase['phrase']:
				found = True
				phrase['values'].append(res.value)
				break		
		if not found:
			aggregate_phrases.append({
				"phrase": res.phrase,
				"values": [res.value]
			})
	# get min, max, and average of all values within a phrase
	for phrase in aggregate_phrases:
		phrase['min'] = min(phrase['values'])
		phrase['max'] = max(phrase['values'])
		phrase['avg'] = format(sum(phrase['values']) / len(phrase['values']), '.2f')
		phrase['count'] = len(phrase['values'])
	
	return render_template('results.html', phrases=aggregate_phrases)

if __name__ == '__main__':
	app.run()
