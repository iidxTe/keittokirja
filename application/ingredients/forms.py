from flask_wtf import FlaskForm
from wtforms import StringField, validators

#ADD MORE VALIDATORS

class IngredientForm(FlaskForm):
    ingredientName = StringField("Ainesosa", [validators.InputRequired])
    ingredientAmount = StringField("Määrä", [validators.InputRequired])
    ingredientUnit = StringField("Yksikkö", [validators.InputRequired])

    class Meta:
        csrf = False