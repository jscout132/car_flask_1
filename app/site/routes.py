from flask import Blueprint, render_template, request, redirect, url_for, flash
from models import CarInfo, db, User
from forms import AddCar
from helpers import token_required
# tying to the __name__ app in __init__
# these are all going to be related to how the website functions
# keep all of this in the site folder
# make the idea of the website- won't do much with it until 
# __init__ calls on it
site = Blueprint('site',__name__, template_folder = 'site_templates')

@site.route('/')
def home():
    car_names = CarInfo.query.all()
    return render_template('index.html', car_names = car_names)

@site.route('/profile')
def profile():
    current_token = User.query.filter_by(token = 'token').first()
    print(current_token)
    form = AddCar()
    try:
        if request.method == 'POST' and form.validate_on_submit():
            car_make = form.car_make.data
            car_model = form.car_color.data
            cost_ = form.cost_.data
            mileage = form.mileage.data
            year_ = form.year_.data
            car_color = form.car_color.data
            token = current_token

            car = CarInfo(car_make = car_make, 
                          car_model = car_model, 
                          cost_ = cost_, 
                          mileage = mileage,
                          year_ = year_,
                          car_color = car_color)

            db.session.add(car)
            db.session.commit()
            print(car)

            flash('added a car', 'User-created')
            return redirect(url_for('site.home'))
    except:
        raise Exception('Invalid form data: please check your form')
    return render_template('profile.html', form = form)


# @site.route('/add_car', methods = ['GET','POST'])
# def add_car():
#     print('into site.route add car function')
#     form = AddCar()
#     try:
#         print('into the try statement')
#         if request.method == 'POST' and form.validate_on_submit():
#             print('into the if statement')
#             car_make = form.car_make.data
#             car_model = form.car_color.data
#             cost_ = form.cost_.data
#             mileage = form.mileage.data
#             year_ = form.year_.data
#             car_color = form.car_color.data

#             car = CarInfo(car_make = car_make, 
#                           car_model = car_model, 
#                           cost_ = cost_, 
#                           mileage = mileage,
#                           year_ = year_,
#                           car_color = car_color)

#             db.session.add(car)
#             db.session.commit()
#             print(car)

#             flash('created a user account', 'User-created')
#             return redirect(url_for('site.home'))
#     except:
#         raise Exception('Invalid form data: please check your form')
#     return render_template('sign_up.html', form = form)