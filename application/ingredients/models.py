from application import db

class Ingredient(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(200), nullable=False)
    #unique=True

    def __init__(self, name):
        self.name = name