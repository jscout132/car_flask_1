from flask import Blueprint, request, jsonify, render_template

from helpers import token_required
from models import db, User, Contact, CarInfo, contact_schema, contacts_schema

api = Blueprint('api',__name__, url_prefix='/api')


@api.route('/getdata')
def getdata():
    return {'yee': 'haw'}

# @api.route('/addcar')
# def addcar():


# @api.route('/cars', methods = ['GET'])
# def getCars():
#     car_name = CarInfo.car_make
#     response = contacts_schema.dump(car_name)
#     for i in car_name:
#         print(i)
#     return jsonify(response)

#I think i need to do something here to pull in the CreateUser class

