from flask_wtf import FlaskForm
from wtforms import StringField, validators

class IngredientForm(FlaskForm):
    ingredientName = StringField("Ainesosa", [validators.Length(max=40)])
    ingredientAmount = StringField("Määrä", [validators.Length(max=40)])
    ingredientUnit = StringField("Yksikkö", [validators.Length(max=40)])

    class Meta:
        csrf = False