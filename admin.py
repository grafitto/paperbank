from config import app, db
from flask import render_template, request, flash, redirect, url_for, Markup
from utilities import Utilities
from models import *
from werkzeug.utils import secure_filename
import boto3
from settings import *
import threading

@app.route("/admin", methods = ["GET", "POST"])
def admin_magic():
    if request.method == "POST":
        magic_word = request.form["magic_word"]
        admin = Admin.query.filter_by(email="nderitukelvin19@gmail.com").first();
        if Utilities.check_password(magic_word, admin.magic_word):
            return redirect(url_for("admin_upload_paper"))
        else:
            flash(Utilities.magic_word_random_flash())
            return redirect(url_for('admin_magic'))
    else:
        return render_template("admin/login.html")

@app.route("/admin/upload")
def admin_upload_paper():
    departments = Department.query.all()
    return render_template('admin/paper.html', deps = departments)

@app.route("/admin/course", methods = ["POST", "GET"])
def admin_create_course():
    if request.method == "POST":
        department_id = request.form["department_id"]
        course_title = request.form["course_title"]
        department = Department.query.get_or_404(department_id)
        course = Course(course_title, department)
        db.session.add(course)
        db.session.commit()
        text = Markup('Course added successifully. Now you can <a href="/admin/unit">Create</a> units under this course')
        flash({'type': 'success', 'message':text})
        return redirect(url_for("admin_create_course"))
        
    else:
        departments = Department.query.all()
        return render_template('admin/course.html', deps = departments)

@app.route("/admin/unit", methods = ["POST", "GET"])
def admin_create_unit():
    if request.method == "POST":
        department_id = request.form["department_id"]
        course_id = request.form["course_id"]
        unit_code = request.form["unit_code"]
        unit_title = request.form["unit_title"]

        course = Course.query.get_or_404(course_id)
        unit = Unit(unit_title, unit_code, course)
        db.session.add(unit)
        db.session.commit()
        text = Markup('Unit added successifully. Now you can <a href="/admin/upload">Upload</a> papers under this unit')
        flash({'type': 'success', 'message': text})
        return redirect(url_for("admin_create_unit"))
    else:
        departments = Department.query.all()
        return render_template("admin/unit.html", deps = departments)

@app.route("/upload/paper", methods=["POST"])
def upload_paper():
    # check if the post request has the file part
    if 'paper' not in request.files:
        flash('No file uploaded. Please select file')
        return redirect(request.url)
    file = request.files['paper']
    # if user does not select file, browser also
    # submit a empty part without filename
    if file.filename == '':
        flash('No selected file to upload')
        return redirect(url_for("admin_upload_paper"))
    if file and Utilities.allowed_file(file.filename):
        rename = request.form.get("rename")
        unit_id = request.form.get("unit_id")
        department_id = request.form.get("department_id")
        course_id = request.form.get("course_id")

        trimester = request.form.get("trimester")
        lecturer = request.form.get("lecturer")
        year = request.form.get("year")

        unit = Unit.query.get_or_404(unit_id)
        department = Department.query.get_or_404(department_id)
        course = Course.query.get_or_404(course_id)

        final_filename = secure_filename(file.filename)

        if rename is not None:
            final_filename = unit.code + " " + unit.title + "(" + trimester[:3] + " " + year + ") - " + lecturer + "." + file.filename.rsplit('.', 1)[1]

        paper = Paper(final_filename, lecturer, trimester, unit)
        db.session.add(paper)
        db.session.commit()

        key = department.title + "/" + course.title + "/" + unit.title + "/" + final_filename

        s3 = boto3.resource("s3")
        
        #Upload to amazon s3
        s3.Bucket(ProductionConfig.S3_BUCKET_NAME).put_object(Key = key, Body = file.read())

        flash({"type":"success", "message":"Paper '{t}' uploaded successfully".format(t = final_filename)}) 
        return redirect(url_for("admin_upload_paper"))
    else:
        flash("File type not allowed. Upload 'pdf', 'txt' or 'docs' only")
        return redirect(url_for("admin_upload_paper"))