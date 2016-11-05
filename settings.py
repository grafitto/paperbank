class Config(object):
    DEBUG = False
    TESTING = False
    DATABASE_URI = 'sqlite://:memory:'

class ProductionConfig(Config):
    DATABASE_URI = 'mysql+pymysql://grafitto:1234567youtube@anu-paperbank.cuczdri4rcvf.us-west-2.rds.amazonaws.com:3306/gsayyicxj49vmbfo'
    S3_BUCKET_NAME = "anu.pastpapers"
    SECRET_KEY = "thisisthesecretkeypleasedonotread"

class DevelopmentConfig(Config):
    DEBUG = True
    S3_BUCKET_NAME = "anu.pastpapers"
    DATABASE_URI = "mysql+pymysql://root:@localhost:3306/pastpapers"
    SECRET_KEY = "thisisthesecretkeypleasedonotread"

class TestingConfig(Config):
    TESTING = True
