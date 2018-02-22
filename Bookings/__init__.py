from flask import Flask

from .config import config_by_name
from flask_sqlalchemy import SQLAlchemy 
#from flask_login import LoginManager


db = SQLAlchemy()
#configure authentification
#login_manger = LoginManager()
#login_manger.session_protection = "strong"
#login_manger.init_app(app)


def create_app(config_name):
    #setup and configuration
    app = Flask(__name__)
    app.config.from_object(config_by_name[config_name])

    #extensions
    db.init_app(app)

    from Bookings.main import main as main_blueprint
    app.register_blueprint(main_blueprint, url_prefix='/')

    from Bookings.auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix='/auth')

    return app
