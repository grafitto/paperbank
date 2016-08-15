from config import app
from config import db
from models import * 
import flask_restless as fl


db.create_all()

manager = fl.APIManager(app, flask_sqlalchemy_db = db)

manager.create_api(Paper, methods = ["GET", "POST", "PUT", "PATCH", "DELETE"])
manager.create_api(Course, methods = ["GET", "POST", "PUT", "PATCH"])
manager.create_api(Department, methods = ["GET", "PUT", "PATCH"])
manager.create_api(Unit, methods = ["GET", "PUT", "PATCH", "DELETE", "POST"])
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=4000, debug=True)