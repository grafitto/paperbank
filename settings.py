class Config(object):
    DEBUG = False
    TESTING = False
    DATABASE_URI = 'sqlite://:memory:'

class ProductionConfig(Config):
    DATABASE_URI = 'mysql://user@localhost/foo'
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