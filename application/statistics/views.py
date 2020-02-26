from flask import render_template, url_for
from flask_login import login_required

from application import app, db

from application.recipes.models import Recipe
from application.ingredients.models import Ingredient


@app.route("/statistics/", methods=["GET"])
@login_required
def go_to_statistics():

    recipesPerUser = Recipe.list_how_many_recipes_per_user()

    ingredientsPerRecipe = Ingredient.list_ingredients_per_recipe()
    
    return render_template("statistics/statistics.html", recipesPerUser = recipesPerUser, ingredientsPerRecipe=ingredientsPerRecipe)