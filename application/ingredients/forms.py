from flask_wtf import FlaskForm
from wtforms import StringField, validators

#ADD MORE VALIDATORS

class IngredientForm(FlaskForm):
    ingredientName = StringField("Ainesosa")
    ingredientAmount = StringField("Määrä")
    ingredientUnit = StringField("Yksikkö")

    class Meta:
        csrf = False