from application import db

class Recipe(db.Model):
    id = db.Column(db.Integer, primary_key=True)

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


class Ingredient(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(200), unique=True, nullable=False)

    def __init__(self, name):
        self.name = name


class RecipeIngredient(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    amount = db.Column(db.Float, nullable=True)
    unit = db.Column(db.String(200), nullable=True)

    recipe_id = db.Column(db.Integer, db.ForeignKey('recipe.id'),
                           nullable=False)

    ingredient_id = db.Column(db.Integer, db.ForeignKey('ingredient.id'),
                           nullable=False)

    def __init__(self, amount, unit):
        self.amount = amount
        self.unit = unit