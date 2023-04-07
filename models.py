# imports 
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import uuid 
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from flask_login import LoginManager
from flask_marshmallow import Marshmallow 
import secrets
import random

# set variables for class instantiation
login_manager = LoginManager()
ma = Marshmallow()
db = SQLAlchemy()

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


# i might have to make a new table for car info to allow sales people to add cars and actually have
# some generated ids as primary keys
class CarInfo(db.Model):
    serial_number = db.Column(db.String(3), primary_key=True)
    car_make = db.Column(db.String(150), nullable=True, default='')
    car_model = db.Column(db.String(150))
    cost_ = db.Column(db.String(20))
    mileage = db.Column(db.String(20))
    year_ = db.Column(db.String(20))
    car_color = db.Column(db.String(50))
    token = db.Column(db.String, db.ForeignKey('user.token'), nullable = False)


    def __init__(self, serial_number, car_make, car_model, cost_, mileage, year_, car_color, token):
        self.serial_number = serial_number
        self.car_make = car_make
        self.car_model = car_model
        self.cost_ = cost_
        self.mileage = mileage
        self.year_ = year_
        self.car_color = car_color
        self.token = token
    
    def __repr__(self):
        return f'The following car has been added to the database: {self.serial_number, self.car_make}'


class User(db.Model, UserMixin):
    id = db.Column(db.String, primary_key=True)
    fname = db.Column(db.String(150), nullable=True, default='')
    lname = db.Column(db.String(150), nullable = True, default = '')
    email = db.Column(db.String(150), nullable = False)
    password = db.Column(db.String, nullable = True, default = '')
    g_auth_verify = db.Column(db.Boolean, default = False)
    token = db.Column(db.String, default = '', unique = True )
    date_created = db.Column(db.DateTime, nullable = False, default = datetime.utcnow)

    def __init__(self, email, fname='', lname='', password='', token='', g_auth_verify=False):
        self.id = self.set_id()
        self.fname = fname
        self.lname = lname
        self.password = self.set_password(password)
        self.email = email
        self.token = self.set_token(6)
        self.g_auth_verify = g_auth_verify

    def set_token(self, length):
        return secrets.token_hex(length)

    def set_id(self):
        return str(uuid.uuid4())
    
    def set_password(self, password):
        self.pw_hash = generate_password_hash(password)
        return self.pw_hash

    def __repr__(self):
        return f'User {self.email} has been added to the database'

# this is what i'll base the new car info on to add to the database
class Contact(db.Model):
    id = db.Column(db.String, primary_key = True)
    name = db.Column(db.String(150), nullable = False)
    email = db.Column(db.String(200))
    phone_number = db.Column(db.String(20))
    address = db.Column(db.String(200))
    # this foreign key gets pulled from a different location as in not the class created above
    # i'll have to make sure the naming is consistent if i'm making it so the sales person can add cars
    user_token = db.Column(db.String, db.ForeignKey('user.token'), nullable = False)

    def __init__(self, name, email, phone_number, address, user_token, id = ''):
        self.id = self.set_id()
        self.name = name
        self.email = email
        self.phone_number = phone_number
        self.address = address
        self.user_token = user_token

    def __repr__(self):
        return f'The following contact has been added to the database: {self.name, self.email}'

    def set_id(self):
        return (secrets.token_urlsafe())
    
class CarSchema(ma.Schema):
    class Meta:
        fields = ['serial_number', 
                  'car_make',
                  'car_model',
                  'cost_', 
                  'mileage',
                  'year_',
                  'car_color',
                  'token']

car_schema = CarSchema()
cars_schema = CarSchema(many=True)