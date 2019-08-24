from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, SelectField, FloatField, IntegerField, SelectMultipleField
from wtforms.validators import DataRequired

class pluForm(FlaskForm):
    search = IntegerField('Search', validators=[DataRequired()])
    submit = SubmitField('Show It')