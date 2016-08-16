import config 
db = config.db

class Unit(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(255), unique = True)
    code = db.Column(db.String(10))

    course_id = db.Column(db.Integer, db.ForeignKey('course.id'))
    course = db.relationship("Course", backref = db.backref('unit', lazy = 'dynamic'))

    def __init__(self, title, code, course):
        self.title = str(title).capitalize()
        self.code = str(code).upper()
        self.course = course

    def __repr__(self):
        return self.title

    __str__ = __repr__