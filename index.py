from config import app
from config import db
from models import * 
import flask_restless as fl

import admin

@app.route("/debug")
def debug():
    admin = Admin.query.filter_by(email = "nderitukelvin19@gmail.com").first()
    return str(admin)

db.create_all()

manager = fl.APIManager(app, flask_sqlalchemy_db = db)

manager.create_api(Paper, methods = ["GET", "POST", "PUT", "PATCH", "DELETE"])
manager.create_api(Course, methods = ["GET", "POST", "PUT", "PATCH"])
manager.create_api(Department, methods = ["GET", "PUT", "POST", "PATCH"])
manager.create_api(Unit, methods = ["GET", "PUT", "PATCH", "DELETE", "POST"])

#Fire that thing
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=4000, debug=True)