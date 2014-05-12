from __future__ import division, print_function
import os.path
from time import strftime
from flask import Flask, render_template, request
from sqlalchemy import func, desc
from database import db_session
from models import Sessions, Submissions, Responses
from forms import MeaningForm, SessionForm

BASE_DIR = os.path.dirname(os.path.realpath(__file__))

app = Flask(__name__)
app.config['DEBUG'] = True
# import settings from settings file
settings_file = os.path.join(BASE_DIR, 'settings.py')
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
	
	# check if session exists
	today = strftime("%Y-%m-%d")
	sesh = Sessions.query.filter(
			func.date(Sessions.created)==func.date(today)
		).order_by(desc(Sessions.created)).first()
	# create a new session if one does not exist
	# for today
	if sesh is None:
		sesh = Sessions()
		db_session.add(sesh)
		db_session.commit()

	submission = Submissions(session_id=sesh.id, ip=request.remote_addr)
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
	sesh_name = None
	responses = []
	# find data based on total, 
	# specified date in GET, or today's records
	sesh_date = strftime("%Y-%m-%d")	
	if date == "overall":
		responses = Responses.query.all()
		sesh_date = "Overall"	
	else:		
		sesh = Sessions.query.\
			filter(func.date(Sessions.created)==func.date(sesh_date)).\
			order_by(desc(Sessions.created)).first()
		if sesh is not None:
			sesh_name = sesh.name
			subs = Submissions.query.\
				filter(Submissions.session==sesh)
			responses = Responses.query.\
				filter(Responses.submission_id.in_([sub.id for sub in subs]))

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
		phrase_item['avg'] = format(sum(phrase_item['values']) / len(phrase_item['values']), '.2f')
		phrase_item['count'] = len(phrase_item['values'])
	
	return render_template('results.html', phrases=agg_phrases, date=sesh_date, sesh_name=sesh_name)

@app.route('/sessions')
def sessions():
	seshs = Sessions.query.order_by(desc(Sessions.created)).all()
	for sesh in seshs:
		sesh.count = Submissions.query.filter(Submissions.session==sesh).count()

	return render_template('seshs.html', sessions=seshs)

@app.route('/sessions/new')
def session_new():
	form = SessionForm()
	return render_template('sesh_new.html', form=form)

@app.route('/sessions/new/complete', methods=['GET', 'POST'])
def session_new_complete():
	form = SessionForm()
	if not form.validate_on_submit():
		return render_template('sesh_new.html', form=form)
		
	sesh = Sessions(name=form.name.data)
	db_session.add(sesh)
	db_session.commit()

	return render_template('sesh_new.html', success=True)

if __name__ == '__main__':
	app.run()
