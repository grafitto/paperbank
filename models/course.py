import config
db = config.db

class Course(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(255), unique = True)

    department_id = db.Column(db.Integer, db.ForeignKey('department.id'))
    department = db.relationship('Department', backref = db.backref('course', lazy = 'dynamic')) 

    def __init__(self, title):
        self.title = title

    def __repr__(self):
        return self.title