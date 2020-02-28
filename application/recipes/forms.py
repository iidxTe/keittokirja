from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, FieldList, FormField, ValidationError, validators

from application.ingredients.forms import IngredientForm

class NewRecipeForm(FlaskForm):
    header = StringField("Otsikoi resepti", [validators.Length(min=1, max=40)])
    category = StringField("Lisää kategoria", [validators.Length(min=1, max=40)])
    description = TextAreaField("Kirjoita kuvaus", [validators.Length(max=900)])

    ingredients = FieldList(FormField(IngredientForm), [validators.Length(max=40)])

    directions = TextAreaField("Listaa työvaiheet", [validators.Length(min=1, max=9000)])
 
    class Meta:
        csrf = False


class EditRecipeForm(FlaskForm):
    header = StringField("Muokkaa otsikkoa", [validators.Length(min=1, max=40)])
    category = StringField("Muokkaa kategoriaa", [validators.Length(min=1, max=40)])
    description = TextAreaField("Muokkaa kuvausta", [validators.Length(max=900)])

    ingredients = FieldList(FormField(IngredientForm), [validators.Length(max=90)])

    directions = TextAreaField("Muokkaa työvaiheita", [validators.Length(min=1, max=9000)])
 
    class Meta:
        csrf = False