from flask import redirect, render_template, request, url_for
from flask_login import login_required, current_user

from application import app, db
from application.recipes.models import Recipe
from application.recipes.forms import NewForm, EditForm

from application.auth.models import User

from sqlalchemy import update


@app.route("/recipes/<user_id>/", methods=["GET"])
@login_required
def recipes_index(user_id):

    return render_template("recipes/list.html", recipes = Recipe.query.filter(Recipe.account_id == user_id))

@app.route("/recipes/new/", methods=["GET", "POST"])
@login_required
def recipes_create():

    if request.method == "GET":
        return render_template("recipes/new.html", form = NewForm())

    form = NewForm(request.form)

    recipe = Recipe(form.header.data, form.category.data, form.description.data, form.ingredients.data, form.directions.data)
    recipe.account_id = current_user.id

    db.session().add(recipe)
    db.session().commit()
  
    return redirect(url_for("recipes_index", user_id = recipe.account_id))

@app.route("/recipes/<recipe_id>/", methods=["POST"])
@login_required
def recipes_remove(recipe_id):

    recipe = Recipe.query.get(recipe_id)
    db.session().delete(recipe)
    db.session().commit()
  
    return redirect(url_for("recipes_index", user_id = recipe.account_id))

@app.route("/recipes/edit/<recipe_id>/", methods=["GET", "POST"])
@login_required
def recipes_edit(recipe_id):

    recipe = Recipe.query.get(recipe_id)

    if request.method == "GET":
        form = EditForm()
        form.header.data = recipe.header
        form.category.data = recipe.category
        form.description.data = recipe.description
        form.ingredients.data = recipe.ingredients
        form.directions.data = recipe.directions
        return render_template("recipes/edit.html", recipe = recipe, form = form)

    recipe.header = request.form.get("header")
    recipe.category = request.form.get("category")
    recipe.description = request.form.get("description")
    recipe.ingredients = request.form.get("ingredients")
    recipe.directions = request.form.get("directions")

    db.session().commit()
  
    return redirect(url_for("recipes_index", user_id = recipe.account_id))







