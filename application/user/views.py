from flask import render_template, url_for, redirect, request
from flask_login import login_required, current_user

from application import app, db

from application.recipes.models import Recipe, RecipeIngredient
from application.auth.models import User
from application.user.forms import EditUserForm


@app.route("/user/<user_id>/", methods=["GET"])
@login_required
def go_to_user_info(user_id):

    user = User.query.get(user_id)

    recipeSum = Recipe.count_my_recipes(user_id)
    
    return render_template("user/userinfo.html", user=user, recipeSum=recipeSum)


@app.route("/user/edit/<user_id>/", methods=["GET", "POST"])
@login_required
def edit_user(user_id):

    user = User.query.get(user_id)

    if request.method == "GET":
        form = EditUserForm()

        form.name.data = user.name
        form.password.data = user.password
    
        return render_template("user/edit.html", form=form, user=user)


    form = EditUserForm(request.form)
    user.account_id = current_user.id

    if not form.validate():
        return render_template("user/edit.html", form = form, user=user)

    userWithSameName = User.query.filter_by(name=form.name.data).first()

    if not userWithSameName:
        user.name = form.name.data
        user.password = form.password.data
        db.session().add(user)
        db.session().commit()
        
        return redirect(url_for("go_to_user_info", user_id = user.account_id))
    
    return render_template("user/edit.html", form = form, user=user,
                               error = "Nimi jo käytössä")


@app.route("/user/userinfo/<user_id>/", methods=["POST"])
@login_required
def delete_user(user_id):

    #logout_user() TARVIIKO?
    #tuhoa RecipeIngredientit
    #tuhoa Recipet
    #tuhoa käyttäjä

    user = User.query.get(user_id)

    recipes = Recipe.query.filter_by(account_id=user.id).all()

    for recipe in recipes:
        recipeIngredients = RecipeIngredient.query.filter_by(recipe_id=recipe.id).all()

        for recipeIngredient in recipeIngredients:
            db.session().delete(recipeIngredient)

        db.session().delete(recipe)

    db.session().delete(user)
    db.session().commit()

    return redirect(url_for("index"))