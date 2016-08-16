from config import app
from config import db
from models import * 
import flask_restless as fl

#This creates default departments
@app.route('/departments/default')
def departments():
    department_titles = ["Religion Department", "Mass Communication Department", "Computer and Information Technology Department", "Education Department", "Environment and Natural Resource Management", "PUP Department", "Counseling Department"]
    for title in department_titles:
        d = Department(title)
        db.session.add(d)
    db.session.commit()
    return "Done"

#This creates default courses
@app.route("/courses/default")
def courses():
    courses = {"Computer and Information Technology Department":["Masters of Science in Applied IT", "Bachalor of Computer Science","Diploma in Information Technology", "Diploma in Mobile Computing", "Bachelor of Business and Information Technology", "Cisco Certified Network Associate, Level 1 - 4", "Certificate in information Technology"]}
    departments = Department.query.all()
    h = ""
    for department in departments:
        if courses[department.title] is not None:
            for course in courses[department.title]:
                c = Course(course, department)
                db.session.add(c)
        db.session.commit()
    return "Done"

db.create_all()

manager = fl.APIManager(app, flask_sqlalchemy_db = db)

manager.create_api(Paper, methods = ["GET", "POST", "PUT", "PATCH", "DELETE"])
manager.create_api(Course, methods = ["GET", "POST", "PUT", "PATCH"])
manager.create_api(Department, methods = ["GET", "PUT", "POST", "PATCH"])
manager.create_api(Unit, methods = ["GET", "PUT", "PATCH", "DELETE", "POST"])

#Fire that thing
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=4000, debug=True)