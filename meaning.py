import os
from sqlalchemy import func
from flask import Flask, render_template, request
from database import db_session
from models import Submissions, Responses
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

@app.route('/results')
def results():
	from time import strftime
	responses = Responses.query.filter(Responses.submission.has(Submissions.created==strftime("%Y-%m-%d"))).all()
	
	aggregate_phrases = []
	for res in responses:
		if len(aggregate_phrases) == 0:
			aggregate_phrases.append({ 
				"phrase": res.phrase, 
				"values": [res.value] 
			})
			continue
		for record in aggregate_phrases:
			if res.phrase == record.phrase:
				record['values'].append(res.value)
				break		
	
	return render_template('results.html')

if __name__ == '__main__':
	app.run()
