from flask_wtf import FlaskForm
from wtforms import StringField, validators

#ADD VALIDATORS

class IngredientForm(FlaskForm):
    ingredientName = StringField("Ainesosa", [validators.Length(max=20)])
    ingredientAmount = StringField("Määrä")
    ingredientUnit = StringField("Yksikkö")

    class Meta:
        csrf = False