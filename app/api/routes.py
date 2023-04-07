from flask import Blueprint, request, jsonify, render_template

from helpers import token_required
from models import db, User, CarInfo, car_schema, cars_schema

api = Blueprint('api',__name__, url_prefix='/api')

@api.route('/car', methods = ['POST'])
@token_required
def add_cars(current_user_token):
    serial_number = request.json['serial_number']
    car_make = request.json['car_make']
    car_model = request.json['car_model']
    cost_ = request.json['cost_']
    mileage = request.json['mileage']
    year_ = request.json['year_']
    car_color = request.json['car_color']
    token = current_user_token.token

    print(f'testing:{token}')

    new_car = CarInfo(serial_number=serial_number,
                      car_make=car_make, 
                      car_model=car_model,
                      cost_=cost_,
                      mileage=mileage,
                      year_=year_,
                      car_color=car_color,
                      token=token)

    db.session.add(new_car)
    db.session.commit()

    response = car_schema.dump(new_car)
    return jsonify(response)

@api.route('/car', methods =['GET'])
@token_required
def get_cars(current_user_token):
    user = current_user_token.token
    cars = CarInfo.query.filter_by(token = user).all()
    print(cars)
    response = cars_schema.dump(cars)
    return jsonify(response)


@api.route('/car/<id>', methods = ['POST','PUT'])
@token_required
def update_car(current_user_token, id):
    car = CarInfo.query.get(id)
    car.car_make = request.json['car_make']
    car.car_model = request.json['car_model']
    car.cost_ = request.json['cost_']
    car.mileage = request.json['mileage']
    car.year_ = request.json['year_']
    car.car_color = request.json['car_color']
    car.token = current_user_token.token

    db.session.commit()
    response = car_schema.dump(car)
    return jsonify(response)

@api.route('/car/<id>',methods = ['DELETE'])
@token_required
def del_car(current_user_token, id):
    car = CarInfo.query.get(id)
    db.session.delete(car)
    db.session.commit()
    response = car_schema.dump(car)
    return jsonify(response)

