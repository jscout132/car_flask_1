
from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user, LoginManager, current_user, login_required

from forms import CreateUser
from models import User, db, check_password_hash

auth = Blueprint('auth',__name__, template_folder='auth_templates')

@auth.route('/sign_up', methods = ['GET','POST'])
def sign_up():
    form = CreateUser()
    try:
        print('into the try statement')
        if request.method == 'POST' and form.validate_on_submit():
            print('into the if statement')
            fname = form.fname.data
            lname = form.lname.data
            email = form.email.data
            password = form.password.data

            print(fname, lname, email, password)

            user = User(fname, lname, email, password = password)

            db.session.add(user)
            db.session.commit()
            print(email)
            flash('created a user account', 'User-created')
            return redirect(url_for('site.home'))
    except:
        raise Exception('Invalid form data: please check your form')
    return render_template('sign_up.html', form = form)

@auth.route('/sign_in', methods = ['GET','POST'])
def sign_in():
    form = CreateUser()
    try:
        if request.method == 'POST' and form.validate_on_submit():
            email = form.email.data
            password = form.password.data

            logged_user = User.query.filter(User.email == email).first()
            if logged_user and check_password_hash(logged_user.password, password):
                login_user(logged_user)
                print(f'{email} logged in now')
                flash('logged in now','auth-success')
                return redirect(url_for('site.profile'))
            else:
                flash('did not log in','auth-failed')
                return redirect(url_for('auth.sign_in', form = form))
    except:
        raise Exception('Invalid form data, please check your information')
    
    return render_template('sign_in.html', form = form)

@auth.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('site.home'))