from application import db

from sqlalchemy.sql import text

class Ingredient(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(50), nullable=False)

    def __init__(self, name):
        self.name = name



    @staticmethod
    def list_ingredients_per_recipe():
        stmt = text("SELECT Ingredient.name, COUNT(Recipe_Ingredient.ingredient_id) AS amount"
                    " FROM Ingredient"
                    " LEFT JOIN Recipe_Ingredient ON Ingredient.id = Recipe_Ingredient.ingredient_id"
                    " GROUP BY Ingredient.id, Recipe_Ingredient.ingredient_id"
                    " ORDER BY amount DESC")
        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append({"name":row[0], "incidence":row[1]})

        return response