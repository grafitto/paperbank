import config
db = config.db

class Department(db.Model):
    __tablename__ = 'department'
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(255), unique = True)

    def __init__(self, title):
        self.title = title

    def __repr__(self):
        return self.title

    __str__ = __repr__