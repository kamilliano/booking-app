

def _db_string_builder(username, password,conn):
    return 'mysql://' + username + ':' + password + '@' + conn


class Config:
    #secret key for session signing, use following to generate new 
    # >>> import os
    # >>> os.urandom(24)
    SECRET_KEY = "\x94'#\xe8\xdc\xd1I\x8f\x0b+\x053\xd2=Ef\xf4d\xbd&\xcb\xf11\xac"
    DEBUG = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    #RECAPTCHA_PUBLIC_KEY = '6LevTEcUAAAAAHGIOVvam9tMbwslKfVHVB6lqop2'
    #RECAPTCHA_PRIVATE_KEY = '6LevTEcUAAAAAEFY2PKoL7Ndo5M74BPDThTZ7EM-'
    MYSQL_USERNAME = r'sqlalchemy'
    MYSQL_PASSWORD = r'sn@pp333!wow'
    MYSQL_NET = r'127.0.0.1:3306'
    MYSQL_CONN = _db_string_builder(MYSQL_USERNAME, MYSQL_PASSWORD, MYSQL_NET)
    
    dbs = { 'dev_db' : 'bookings-dev', 'test_db' : 'bookings-test', 'prod_db' : 'bookings-prod' }

class DevConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = Config.MYSQL_CONN + '/' + Config.dbs['dev_db']
    

class TestConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = Config.MYSQL_CONN + '/' + Config.dbs['test_db']
    WTF_CSRF_ENABLED = False #unit testing forms

class ProdConfig(Config):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = Config.MYSQL_CONN + '/' + Config.dbs['prod_db']

#map keys to config object
config_by_name = dict(
    dev = DevConfig,
    test = TestConfig,
    prod = ProdConfig
)