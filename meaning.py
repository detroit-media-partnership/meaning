from __future__ import division
import os.path
from flask import Flask, render_template, request
from sqlalchemy import func
from database import db_session
from models import Submissions, Responses
from forms import MeaningForm

app = Flask(__name__)
app.config['DEBUG'] = True
# import settings from settings file
settings_file = 'settings.py'
if os.path.isfile(settings_file):
	app.config.from_pyfile(settings_file)

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
	# find data based on total, 
	# specified date in GET, or today's records
	from time import strftime
	if date == "overall":
		responses = Responses.query.all()
	elif date is not None:
		responses = Responses.query.filter(
						Responses.submission.has(
							func.date(Submissions.created)==func.date(date)
						)
					).all()
	else:
		responses = Responses.query.filter(
						Responses.submission.has(
							func.date(Submissions.created)==func.date(strftime("%Y-%m-%d"))
						)
					).all()
	
	# add up totals by phrase and store them
	# in an array of dictionaries
	agg_phrases = []
	for res in responses:
		found = False
		for phrase_item in agg_phrases:
			if res.phrase == phrase_item['phrase']:
				found = True
				phrase_item['values'].append(res.value)
				break		
		if not found:
			agg_phrases.append({
				"phrase": res.phrase,
				"values": [res.value]
			})
	# get min, max, and average of all values within a phrase
	for phrase_item in agg_phrases:
		phrase_item['min'] = min(phrase_item['values'])
		phrase_item['max'] = max(phrase_item['values'])
		phrase_item['avg'] = format(sum(phrase_item['values']) / len(phrase_item['values']), '.3f')
		phrase_item['count'] = len(phrase_item['values'])
	
	return render_template('results.html', phrases=agg_phrases)

if __name__ == '__main__':
	app.run()
