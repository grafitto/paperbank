import config
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

    def getDownloadLink():
        pass

    def __repr__(self):
        return str(self.title)

    __str__ = __repr__
  
