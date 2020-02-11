from application import db
from application.models import Base
from application.auth.models import User

from sqlalchemy.sql import text

class Recipe(Base):

    header = db.Column(db.String(200), nullable=False)
    category = db.Column(db.String(100), nullable=False)

    description = db.Column(db.String(1000), nullable=True)
    directions = db.Column(db.String(10000), nullable=False)

    account_id = db.Column(db.Integer, db.ForeignKey('account.id'),
                           nullable=False)

    def __init__(self, header, category, description, directions):
        self.header = header
        self.category = category
        self.description = description
        self.directions = directions


    @staticmethod
    def get_recipes_with_ingredients(user_id):
        stmt = text("SELECT Recipe.id, Recipe.header, Recipe.category, Recipe.description, Ingredient.name, Recipe_Ingredient.amount, Recipe_Ingredient.unit, Recipe.directions FROM Recipe"
                    " INNER JOIN Recipe_Ingredient ON Recipe.id = Recipe_Ingredient.recipe_id"
                    " INNER JOIN Ingredient ON Recipe_Ingredient.ingredient_id = Ingredient.id"
                    " WHERE Recipe.account_id = :user_id").params(user_id=user_id)
        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append({"id":row[0], "header":row[1], "category":row[2], "description":row[3], "name":row[4], "amount":row[5], "unit":row[6], "directions":row[7]})

        return response

    @staticmethod
    def count_my_recipes(user_id):
        stmt = text("SELECT COUNT(*) FROM Recipe WHERE account_id = :user_id").params(user_id=user_id)
        res = db.engine.execute(stmt)

        response = []

        for row in res:
            response.append(row[0])

        return response


    @staticmethod
    def list_how_many_recipes_per_user():
        stmt = text("SELECT Account.name, COUNT(Recipe.account_id)"
                    " FROM Account"
                    " LEFT JOIN Recipe ON Account.id = Recipe.account_id"
                    " GROUP BY Account.id, Recipe.account_id")
        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append({"name":row[0], "count":row[1]})

        return response
        

class RecipeIngredient(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    amount = db.Column(db.Float, nullable=True)
    unit = db.Column(db.String(200), nullable=True)

    recipe_id = db.Column(db.Integer, db.ForeignKey('recipe.id'),
                           nullable=False)

    ingredient_id = db.Column(db.Integer, db.ForeignKey('ingredient.id'),
                           nullable=False)

    def __init__(self, amount=None, unit=None):
        if amount is None:
            amount = {}
        elif unit is None:
            unit = {}
        else:
            self.amount = amount
            self.unit = unit