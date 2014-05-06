from flask_wtf import Form
from wtforms import TextField
from wtforms.validators import Required, NumberRange

class MeaningForm(Form):
	often = TextField('often', validators=[NumberRange(min=0, max=100)])
	always = TextField('always', validators=[NumberRange(min=0, max=100)])
	sometimes = TextField('sometimes', validators=[NumberRange(min=0, max=100)])
	never = TextField('never', validators=[NumberRange(min=0, max=100)])
	usually = TextField('usually', validators=[NumberRange(min=0, max=100)])
	most_of_time = TextField('most_of_time', validators=[NumberRange(min=0, max=100)])
	occasionally = TextField('occasionally', validators=[NumberRange(min=0, max=100)])
	seldom = TextField('seldom', validators=[NumberRange(min=0, max=100)])
	almost_always = TextField('almost_always', validators=[NumberRange(min=0, max=100)])
	rarely = TextField('rarely', validators=[NumberRange(min=0, max=100)])
	frequently = TextField('frequently', validators=[NumberRange(min=0, max=100)])
	quite_often = TextField('quite_often', validators=[NumberRange(min=0, max=100)])
