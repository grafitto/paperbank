class Config(object):
    DEBUG = False
    TESTING = False
    DATABASE_URI = 'sqlite://:memory:'

class ProductionConfig(Config):
    DATABASE_URI = 'mysql+pymysql://be1a28832dc3d6:a4fda910@us-cdbr-iron-east-04.cleardb.net/heroku_0adc8d16ff6feca?reconnect=true'
    S3_BUCKET_NAME = "anu.pastpapers"
    AWS_ACCESS_KEY_ID = 'AKIAJVEPXVGPPURXOR3Q'
    AWS_SECRET_ACCESS_KEY = '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'

class DevelopmentConfig(Config):
    DEBUG = True
    S3_BUCKET_NAME = "anu.pastpapers"
    DATABASE_URI = "mysql+pymysql://root:@localhost:3306/pastpapers"
    AWS_ACCESS_KEY_ID = 'AKIAJVEPXVGPPURXOR3Q'
    AWS_SECRET_ACCESS_KEY = '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'

class TestingConfig(Config):
    TESTING = True
