class Config(object):
    DEBUG = False
    TESTING = False
    DATABASE_URI = 'sqlite://:memory:'

class ProductionConfig(Config):
    DATABASE_URI = 'mysql+pymysql://atlj17scn7w3v8qp:r146i5gq1aq7umid@uoa25ublaow4obx5.cbetxkdyhwsb.us-east-1.rds.amazonaws.com:3306/gsayyicxj49vmbfo'
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
