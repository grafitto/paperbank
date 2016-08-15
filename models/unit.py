import config 
db = config.db

class Unit(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(255), unique = True)
    code = db.Column(db.String(10))

    course_id = db.Column(db.Integer, db.ForeignKey('course.id'))
    course = db.relationship("Course", backref = db.backref('unit', lazy = 'dynamic'))

    def __init__(self, title, code):
        self.title = str(title).capitalize();
        self.code = str(code).upper();

    def __repr__(self):
        return self.title