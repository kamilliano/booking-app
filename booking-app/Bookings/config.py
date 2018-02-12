import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = "\x94'#\xe8\xdc\xd1I\x8f\x0b+\x053\xd2=Ef\xf4d\xbd&\xcb\xf11\xac"
    DEBUG = False

class DevConfig(Config):
    DEBUG = True
    #MYSQL_DATABASE_URI = 'mysql+mysqldb:///' + os.path.join(basedir, 'bookings-dev.db')
    

class TestConfig(Config):
    TESTING = True
    #MYSQL_DATABASE_URI = 'mysql+mysqldb:///' + os.path.join(basedir, 'bookings-test.db')
    WTF_CSRF_ENABLED = False #unit testing forms

class ProdConfig(Config):
    DEBUG = False
    #MYSQL_DATABASE_URI = 'mysql+mysqldb:///' + os.path.join(basedir, 'bookings-prod.db')

#map keys to config object
config_by_name = dict(
    dev = DevConfig,
    test = TestConfig,
    prod = ProdConfig
)