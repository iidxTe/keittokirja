from application import app, db
from flask import redirect, render_template, request, url_for
from application.recipes.models import Recipe
from sqlalchemy import update


@app.route("/recipes", methods=["GET"])
def recipes_index():
    return render_template("recipes/list.html", recipes = Recipe.query.all())

@app.route("/recipes/new/")
def recipes_form():
    return render_template("recipes/new.html")

@app.route("/recipes/", methods=["POST"])
def recipes_create():
    r = Recipe(request.form.get("header"), request.form.get("category"), request.form.get("description"), request.form.get("ingredients"), request.form.get("directions"))

    db.session().add(r)
    db.session().commit()
  
    return redirect(url_for("recipes_index"))

@app.route("/recipes/<recipe_id>/", methods=["POST"])
def recipes_remove(recipe_id):

    r = Recipe.query.get(recipe_id)
    db.session().delete(r)
    db.session().commit()
  
    return redirect(url_for("recipes_index"))


@app.route("/recipes/edit/<recipe_id>/", methods=["GET"])
def recipes_render_edit_form(recipe_id):

    return render_template("recipes/edit.html", recipe = Recipe.query.get(recipe_id))


@app.route("/recipes/updated/<recipe_id>/", methods=["POST"])
def recipes_edit(recipe_id):

    r = Recipe.query.get(recipe_id)

    r.header = request.form.get("header")
    r.category = request.form.get("category")
    r.description = request.form.get("description")
    r.ingredients = request.form.get("ingredients")
    r.directions = request.form.get("directions")

    db.session().commit()
  
    return redirect(url_for("recipes_index"))





