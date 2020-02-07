from flask import redirect, render_template, request, url_for
from flask_login import login_required, current_user

from application import app, db
from application.recipes.models import Recipe, Ingredient, RecipeIngredient
from application.recipes.forms import NewForm, EditForm, IngredientForm

from application.auth.models import User

from sqlalchemy import update


@app.route("/recipes/<user_id>/", methods=["GET"])
@login_required
def recipes_index(user_id):

    recipes = Recipe.get_recipes_with_ingredients(user_id)
    
    return render_template("recipes/list.html", recipes = recipes)

@app.route("/recipes/new/", methods=["GET", "POST"])
@login_required
def recipes_create():

    if request.method == "GET":
        form = NewForm()
        form.ingredients.append_entry({})
        return render_template("recipes/new.html", form = form)

    form = NewForm(request.form)

    recipe = Recipe(form.header.data, form.category.data, form.description.data, form.directions.data)
    recipe.account_id = current_user.id

    db.session().add(recipe)
    db.session().flush()

    for ingredientForm in form.ingredients.data:

        ingredient = Ingredient.query.filter_by(name=ingredientForm['ingredientName']).first()

        if not ingredient:
            ingredient = Ingredient(ingredientForm['ingredientName'])
            db.session().add(ingredient)
            db.session().flush()

        recipeIngredient = RecipeIngredient(ingredientForm['ingredientAmount'], ingredientForm['ingredientUnit'])
        recipeIngredient.recipe_id = recipe.id
        recipeIngredient.ingredient_id = ingredient.id

        db.session().add(recipeIngredient)

    db.session().commit()
  
    return redirect(url_for("recipes_index", user_id = recipe.account_id))


@app.route("/recipes/edit/<recipe_id>/", methods=["GET", "POST"])
@login_required
def recipes_edit(recipe_id):

    recipe = Recipe.query.get(recipe_id)
    recipeIngredient = RecipeIngredient.query.filter_by(recipe_id=recipe.id).first()
    ingredient = Ingredient.query.filter_by(id=recipeIngredient.ingredient_id).first()

    if request.method == "GET":
        form = EditForm()
        form.ingredients.append_entry({})

        form.header.data = recipe.header
        form.category.data = recipe.category
        form.description.data = recipe.description

        """ TO BE FIXED
        form.ingredients.ingredientName.data = ingredient.name
        form.ingredients.ingredientAmount.data = recipeIngredient.amount
        form.ingredients.ingredientUnit.data = recipeIngredient.unit
        """

        form.directions.data = recipe.directions
        return render_template("recipes/edit.html", recipe = recipe, form = form)

    form = EditForm(request.form)

    recipe.header = request.form.get("header")
    recipe.category = request.form.get("category")
    recipe.description = request.form.get("description")


    for ingredientForm in form.ingredients.data:

        ingr = Ingredient.query.filter_by(name=ingredientForm['ingredientName']).first()

        if not ingr:
            ingr = Ingredient(ingredientForm['ingredientName'])
            db.session().add(ingr)
            db.session().flush()

    ingredient.name = Ingredient(ingredientForm['ingredientName']).name
    recipeIngredient.amount = RecipeIngredient(ingredientForm['ingredientAmount']).amount
    recipeIngredient.unit = RecipeIngredient(ingredientForm['ingredientUnit']).unit
    
    #ingredient.name = request.form.get("ingredientName")
    #recipeIngredient.amount = request.form.get("ingredientAmount")
    #recipeIngredient.unit = request.form.get("ingredientUnit")

    recipe.directions = request.form.get("directions")

    db.session().commit()
  
    return redirect(url_for("recipes_index", user_id = recipe.account_id))


@app.route("/recipes/<recipe_id>/", methods=["POST"])
@login_required
def recipes_remove(recipe_id):

    recipe = Recipe.query.get(recipe_id)

    recipeIngredient = RecipeIngredient.query.filter_by(recipe_id=recipe.id).first()
    db.session().delete(recipeIngredient)

    db.session().delete(recipe)
    db.session().commit()
  
    return redirect(url_for("recipes_index", user_id = recipe.account_id))







