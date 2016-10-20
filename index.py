
from models import * 
import flask_restless as fl

import admin

admin.db.create_all()

#This serves all angular partials
@admin.app.route('/partials/<path:path>')
def serve_partial(path):
    return admin.render_template('/client/partials/{}'.format(path))

#This kickstarts the client app
@admin.app.route('/')
def index():
    return admin.render_template("client/index.html")

manager = fl.APIManager(admin.app, flask_sqlalchemy_db = admin.db)

manager.create_api(Paper, methods = ["GET"], include_methods = ["download_link"])

manager.create_api(Course, methods = ["GET"])
manager.create_api(Department, methods = ["GET"])
manager.create_api(Unit, methods = ["GET"])

#Fire that thing
if __name__ == "__main__":
    from os import environ
    arg_port = int(environ.get('PORT', 5000))
    print(arg_port)
    admin.app.run(host='localhost', port= arg_port, debug = True)