from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired
 
class LoginForm(FlaskForm):
    input = StringField('City Name', validators=[DataRequired()])
    submit = SubmitField('Submit')
