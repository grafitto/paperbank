import config
db = config.db

class Admin(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    email = db.Column(db.String(255))
    magic_word = db.Column(db.String(255))

    def __repr__(self):
        return self.email

    __str__ = __repr__