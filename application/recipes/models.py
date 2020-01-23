from application import db

class Recipe(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    header = db.Column(db.String(60), nullable=False)
    category = db.Column(db.String(30), nullable=False)
    content = db.Column(db.String(144), nullable=False)

    def __init__(self, header, category, content):
        self.header = header
        self.category = category
        self.content = content