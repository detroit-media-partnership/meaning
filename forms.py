from flask_wtf import Form
from wtforms import IntegerField
from wtforms.validators import Required, NumberRange

class MeaningForm(Form):
	often = IntegerField('Often', default=50, validators=[NumberRange(min=0, max=100)])
	always = IntegerField('Always', default=50, validators=[NumberRange(min=0, max=100)])
	sometimes = IntegerField('Sometimes', default=50, validators=[NumberRange(min=0, max=100)])
	never = IntegerField('Never', default=50, validators=[NumberRange(min=0, max=100)])
	usually = IntegerField('Usually', default=50, validators=[NumberRange(min=0, max=100)])
	most_of_time = IntegerField('Most of the Time', default=50, validators=[NumberRange(min=0, max=100)])
	occasionally = IntegerField('Occasionally', default=50, validators=[NumberRange(min=0, max=100)])
	seldom = IntegerField('Seldom', default=50, validators=[NumberRange(min=0, max=100)])
	almost_always = IntegerField('Almost Always', default=50, validators=[NumberRange(min=0, max=100)])
	rarely = IntegerField('Rarely', default=50, validators=[NumberRange(min=0, max=100)])
	frequently = IntegerField('Frequently', default=50, validators=[NumberRange(min=0, max=100)])
	quite_often = IntegerField('Quite Often', default=50, validators=[NumberRange(min=0, max=100)])