class Configuration(object):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///blog.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = '2281337'
    SECURITY_PASSWORD_SALT = 'salt'
    SECURITY_PASSWORD_HASH = 'sha512_crypt'
    JSON_AS_ASCII = False