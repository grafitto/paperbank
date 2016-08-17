from config import app
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

