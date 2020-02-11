from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, FieldList, FormField, validators

from application.ingredients.forms import IngredientForm

#ADD MORE VALIDATORS

class NewForm(FlaskForm):
    header = StringField("Otsikoi resepti", [validators.InputRequired])
    category = StringField("Lisää kategoria", [validators.InputRequired])
    description = TextAreaField("Kirjoita kuvaus")

    ingredients = FieldList(FormField(IngredientForm))

    directions = TextAreaField("Listaa työvaiheet", [validators.InputRequired])
 
    class Meta:
        csrf = False


class EditForm(FlaskForm):
    header = StringField("Muokkaa otsikkoa", [validators.InputRequired])
    category = StringField("Muokkaa kategoriaa", [validators.InputRequired])
    description = TextAreaField("Muokkaa kuvausta")

    ingredients = FieldList(FormField(IngredientForm))

    directions = TextAreaField("Muokkaa työvaiheita", [validators.InputRequired])
 
    class Meta:
        csrf = False