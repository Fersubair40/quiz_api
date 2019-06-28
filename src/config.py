import os


class Development(object):
    
    # Development environment configuration

    DEBUG = True
    TESTING = False
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL")
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class Production(object):

    # Production environment configuration

    DEBUG = False
    TESTING = False
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL")



app_config = {
    'development': Development,
    'production': Production,
}


