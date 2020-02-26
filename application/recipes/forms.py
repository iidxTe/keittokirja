from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, FieldList, FormField, ValidationError, validators

from application.ingredients.forms import IngredientForm

#ADD MORE VALIDATORS

class NewRecipeForm(FlaskForm):
    header = StringField("Otsikoi resepti", [validators.Length(min=1, max=30)])
    category = StringField("Lisää kategoria", [validators.InputRequired])
    description = TextAreaField("Kirjoita kuvaus")

    ingredients = FieldList(FormField(IngredientForm))

    directions = TextAreaField("Listaa työvaiheet", [validators.InputRequired])
 
    class Meta:
        csrf = False


class EditRecipeForm(FlaskForm):
    header = StringField("Muokkaa otsikkoa", [validators.InputRequired])
    category = StringField("Muokkaa kategoriaa", [validators.InputRequired])
    description = TextAreaField("Muokkaa kuvausta")

    ingredients = FieldList(FormField(IngredientForm))

    directions = TextAreaField("Muokkaa työvaiheita", [validators.InputRequired])
 
    class Meta:
        csrf = False