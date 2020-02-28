from application import db
from application.auth.models import User

from application.models import Base

from sqlalchemy.sql import text

class Recipe(Base):

    header = db.Column(db.String(50), nullable=False)
    category = db.Column(db.String(50), nullable=False)

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

    amount = db.Column(db.String(50), nullable=True)
    unit = db.Column(db.String(50), nullable=True)

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