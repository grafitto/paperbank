from config import app
from config import db
from models import * 
import flask_restless as fl

import admin

db.create_all()

#This serves all angular partials
@app.route('/partials/<path:path>')
def serve_partial(path):
    return admin.render_template('/client/partials/{}'.format(path))

#This kickstarts the client app
@app.route('/')
def index():
    return admin.render_template("client/index.html")

manager = fl.APIManager(app, flask_sqlalchemy_db = db)

manager.create_api(Paper, methods = ["GET", "POST", "PUT", "PATCH", "DELETE"])
manager.create_api(Course, methods = ["GET", "POST", "PUT", "PATCH"])
manager.create_api(Department, methods = ["GET", "PUT", "POST", "PATCH"])
manager.create_api(Unit, methods = ["GET", "PUT", "PATCH", "DELETE", "POST"])

#Fire that thing
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=4000, debug=True)