from application import db

class Recipe(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    header = db.Column(db.String(200), nullable=False)
    category = db.Column(db.String(100), nullable=False)

    description = db.Column(db.String(1000), nullable=True)
    ingredients = db.Column(db.String(10000), nullable=False)
    directions = db.Column(db.String(10000), nullable=False)

    def __init__(self, header, category, description, ingredients, directions):
        self.header = header
        self.category = category
        self.description = description
        self.ingredients = ingredients
        self.directions = directions