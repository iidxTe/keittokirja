from flask import render_template, request, redirect, url_for
from flask_login import login_user, logout_user

from application import app, db
from application.auth.models import User
from application.auth.forms import LoginForm, RegisterForm

@app.route("/auth/login", methods = ["GET", "POST"])
def auth_login():
    if request.method == "GET":
        return render_template("auth/login.html", form = LoginForm())

    form = LoginForm(request.form)

    user = User.query.filter_by(name=form.name.data, password=form.password.data).first()
    if not user:
        return render_template("auth/login.html", form = form,
                               error = "Väärä nimi tai salasana")

    login_user(user)
    return redirect(url_for("index"))

@app.route("/auth/logout")
def auth_logout():
    logout_user()
    return redirect(url_for("index"))


@app.route("/auth/register", methods = ["GET", "POST"])
def auth_register():
    if request.method == "GET":
        return render_template("auth/register.html", form = RegisterForm())
  
    form = RegisterForm(request.form)
    if not form.validate():
        return render_template("auth/register.html", form = form)
       
    user = User.query.filter_by(name=form.name.data).first()

    if not user:
        user = User(form.name.data, form.password.data)
        db.session().add(user)
        db.session().commit()
        
        return redirect(url_for("index"))
    
    return render_template("auth/register.html", form = form,
                               error = "Nimi jo käytössä")


