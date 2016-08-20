from config import app, db
from flask import render_template, request, flash, redirect, url_for
from utilities import Utilities
from models import *

@app.route("/admin", methods = ["GET", "POST"])
def admin_magic():
    if request.method == "POST":
        magic_word = request.form["magic_word"]
        admin = Admin.query.filter_by(email="nderitukelvin19@gmail.com").first();
        if Utilities.check_password(magic_word, admin.magic_word):
            return redirect(url_for("admin_index"))
        else:
            flash(Utilities.magic_word_random_flash())
            return redirect(url_for('admin_magic'))
    else:
        return render_template("login.html")

@app.route("/admin/index")
def admin_index():
    departments = Department.query.all()
    return render_template('index.html', deps = departments)

@app.route("/department/<int:id>")
def admin_get_department(id):
    departments = Department.query.all()
    return render_template('index.html', deps = departments)

@app.route("/admin/unit", methods = ["POST"])
def admin_create_unit():
    course_id = request.form["course_id"]
    #Fetch the course
    course = Course.query.get(course_id)

    unit_title = request.form["title"]
    unit_code = request.form["code"]
    #Create a unit and save
    unit = Unit(unit_title, unit_code, course)
    db.session.add(unit)
    db.session.commit()
    return redirect(url_for("admin_index"))

