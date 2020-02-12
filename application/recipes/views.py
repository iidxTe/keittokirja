from flask import redirect, render_template, request, url_for
from flask_login import login_required, current_user

from application import app, db
from application.recipes.models import Recipe, RecipeIngredient
from application.recipes.forms import NewForm, EditForm
from application.ingredients.forms import IngredientForm
from application.ingredients.models import Ingredient

from application.auth.models import User

from sqlalchemy import update


@app.route("/recipes/<user_id>/", methods=["GET"])
@login_required
def recipes_index(user_id):

    recipes = Recipe.get_recipes_with_ingredients(user_id)

    recipeCount = Recipe.count_my_recipes(user_id)

    recipesPerUser = Recipe.list_how_many_recipes_per_user()
    
    return render_template("recipes/list.html", recipes = recipes, recipeCount = recipeCount, recipesPerUser = recipesPerUser)

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
        #form.ingredients.append_entry({})

        form.header.data = recipe.header
        form.category.data = recipe.category
        form.description.data = recipe.description

        ingredients = []
        ingredientForm = IngredientForm()

        ingredientForm.ingredientName.data = ingredient.name
        ingredientForm.ingredientAmount.data = recipeIngredient.amount
        ingredientForm.ingredientUnit.data = recipeIngredient.unit

        ingredients.append(ingredientForm)

        form.ingredients = ingredients

        form.directions.data = recipe.directions

        return render_template("recipes/edit.html", recipe = recipe, form = form)


    form = EditForm(request.form)

    recipe.header = form.header.data
    recipe.category = form.category.data
    recipe.description = form.description.data

    ingredientForm = IngredientForm(ingredientName=ingredient.name, ingredientAmount=recipeIngredient.amount, ingredientUnit=recipeIngredient.unit)

    ingredient = Ingredient.query.filter_by(name=ingredientForm.data['ingredientName']).first()

    if not ingredient:
        ingredient = Ingredient(ingredientForm.data['ingredientName'])
        db.session().add(ingredient)
        db.session().flush()


    recipeIngredientNew = RecipeIngredient(ingredientForm.data['ingredientAmount'], ingredientForm.data['ingredientUnit'])

    recipeIngredientNew.recipe_id = recipe.id

    recipeIngredientNew.ingredient_id = ingredient.id

    db.session().add(recipeIngredientNew)

    db.session().delete(recipeIngredient)

    recipe.directions = form.directions.data

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







