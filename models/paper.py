import config
import boto3
import urllib
db = config.db

class Paper(db.Model):  
    __tablename__ = 'paper'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), unique=True)
    year = db.Column(db.String(255))
    lecturer = db.Column(db.String(255))
    trimester = db.Column(db.String(255))

    unit_id = db.Column(db.Integer, db.ForeignKey("unit.id"))
    unit = db.relationship('Unit', backref = db.backref('paper', lazy='dynamic'))


    def __init__(self, title, lecturer, trimester, unit):
        self.title = title
        self.lecturer = lecturer
        self.trimester = trimester
        self.unit = unit

    def download_link(self):
        s3Client = boto3.client('s3')
        key = self.unit.course.department.title + "/" + self.unit.course.title + "/" + self.unit.title + "/" + self.title
        server = "http://s3-us-west-2.amazonaws.com/anu.pastpapers/";
        return server + key
        #return s3Client.generate_presigned_url('get_object', region = 'us-west-2', Params = {'Bucket': 'anu.pastpapers', 'Key': key}, ExpiresIn = 100000)
        

    def __repr__(self):
        return str(self.title)

    __str__ = __repr__
  
