import os

#basedir = os.path.abspath(os.path.dirname(__file__))

def _db_string_builder(username, password,conn, db):
    return 'mysql://' + username + ':' + password + '@' + conn + '/' + db


class Config:
    #secret key for session signing, use following to generate new 
    # >>> import os
    # >>> os.urandom(24)
    SECRET_KEY = "\x94'#\xe8\xdc\xd1I\x8f\x0b+\x053\xd2=Ef\xf4d\xbd&\xcb\xf11\xac"
    DEBUG = False
    #RECAPTCHA_PUBLIC_KEY = '6LevTEcUAAAAAHGIOVvam9tMbwslKfVHVB6lqop2'
    #RECAPTCHA_PRIVATE_KEY = '6LevTEcUAAAAAEFY2PKoL7Ndo5M74BPDThTZ7EM-'
    MYSQL_USERNAME = r'sqlalchemy'
    MYSQL_PASSWORD = r'sn@pp333!wow'
    MYSQL_CONN = r'127.0.0.1:3306'



class DevConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = _db_string_builder(Config.MYSQL_USERNAME, Config.MYSQL_PASSWORD, Config.MYSQL_CONN, 'bookings-dev.db')
    

class TestConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = _db_string_builder(Config.MYSQL_USERNAME, Config.MYSQL_PASSWORD, Config.MYSQL_CONN, 'bookings-test.db')
    WTF_CSRF_ENABLED = False #unit testing forms

class ProdConfig(Config):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = _db_string_builder(Config.MYSQL_USERNAME, Config.MYSQL_PASSWORD, Config.MYSQL_CONN, 'bookings-prod.db')

#map keys to config object
config_by_name = dict(
    dev = DevConfig,
    test = TestConfig,
    prod = ProdConfig
)