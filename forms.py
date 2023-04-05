from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email

# class UserLoginForm(FlaskForm):
#     email = StringField('Email', validators = [DataRequired(), Email()])
#     password = PasswordField('Password',validators = [DataRequired()])
#     submit_button = SubmitField()

class CreateUser(FlaskForm):
    fname = StringField('First Name', validators=[DataRequired()])
    lname = StringField('Last Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(),Email()])
    password = PasswordField('Password',validators=[DataRequired()])
    submit_button = SubmitField()