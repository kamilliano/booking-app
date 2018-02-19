from flask import Flask

from .config import config_by_name

def create_app(config_name):
    #setup and configuration
    app = Flask(__name__)
    app.config.from_object(config_by_name[config_name])

    from Bookings.main import main as main_blueprint
    app.register_blueprint(main_blueprint, url_prefix='/')

    from Bookings.auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix='/auth')

    return app
