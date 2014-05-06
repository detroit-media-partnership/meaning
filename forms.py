from flask_wtf import Form
from wtforms import IntegerField
from wtforms.validators import Required, NumberRange

class MeaningForm(Form):
	often = IntegerField('Often', validators=[NumberRange(min=0, max=100)])
	always = IntegerField('Always', validators=[NumberRange(min=0, max=100)])
	sometimes = IntegerField('Sometimes', validators=[NumberRange(min=0, max=100)])
	never = IntegerField('Never', validators=[NumberRange(min=0, max=100)])
	usually = IntegerField('Usually', validators=[NumberRange(min=0, max=100)])
	most_of_time = IntegerField('Most of the Time', validators=[NumberRange(min=0, max=100)])
	occasionally = IntegerField('Occasionally', validators=[NumberRange(min=0, max=100)])
	seldom = IntegerField('Seldom', validators=[NumberRange(min=0, max=100)])
	almost_always = IntegerField('Almost Always', validators=[NumberRange(min=0, max=100)])
	rarely = IntegerField('Rarely', validators=[NumberRange(min=0, max=100)])
	frequently = IntegerField('Frequently', validators=[NumberRange(min=0, max=100)])
	quite_often = IntegerField('Quite Often', validators=[NumberRange(min=0, max=100)])
