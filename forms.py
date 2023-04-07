from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, FloatField, IntegerField
from wtforms.validators import DataRequired, Email

class UserLoginForm(FlaskForm):
    email = StringField('Email', validators = [DataRequired(), Email()])
    password = PasswordField('Password',validators = [DataRequired()])
    submit_button = SubmitField()

class CreateUser(FlaskForm):
    fname = StringField('First Name', validators=[DataRequired()])
    lname = StringField('Last Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(),Email()])
    password = PasswordField('Password',validators=[DataRequired()])
    submit_button = SubmitField()


class AddCar(FlaskForm):
    serial_number = StringField('Serial Number', validators=[DataRequired()])
    car_make = StringField('Car Make', validators=[DataRequired()])
    car_model = StringField('Car Model', validators=[DataRequired()])
    cost_ = StringField('Car Cost', validators=[DataRequired()])
    mileage = StringField('Car Mileage', validators=[DataRequired()])
    year_ = StringField('Car Year', validators=[DataRequired()])
    car_color = StringField('Car Color', validators=[DataRequired()])
    submit_button = SubmitField()
