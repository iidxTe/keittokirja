from flask import render_template, url_for
from flask_login import login_required

from application import app, db

from application.auth.models import User
from application.user.forms import EditUserForm


@app.route("/user/<user_id>/", methods=["GET"])
@login_required
def go_to_user_info(user_id):
    
    return render_template("user/userinfo.html")


