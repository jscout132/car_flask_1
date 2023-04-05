from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS

from .site.routes import site
from .authentication.routes import auth
from .api.routes import api
from config import Config
from helpers import JSONEncoder

from models import db, login_manager, ma

#this is where flask runs from
app = Flask(__name__)
# CORS is a security feature
# cross site request forgery
# can be a pain if it isn't set up properly
CORS(app)

app.register_blueprint(site)
app.register_blueprint(auth)
app.register_blueprint(api)

app.json_encoder = JSONEncoder

app.config.from_object(Config)
db.init_app(app)
login_manager.init_app(app)
ma.init_app(app)
migrate = Migrate(app, db)