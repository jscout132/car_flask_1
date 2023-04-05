from flask import Blueprint, render_template
from models import CarInfo
# tying to the __name__ app in __init__
# these are all going to be related to how the website functions
# keep all of this in the site folder
# make the idea of the website- won't do much with it until 
# __init__ calls on it
site = Blueprint('site',__name__, template_folder = 'site_templates')

@site.route('/')
def home():
    car_names = CarInfo.query.all()
    print('made it to site.route in the home function')
    return render_template('index.html', car_names = car_names)

@site.route('/profile')
def profile():
    return render_template('profile.html')