from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, validators

class NewForm(FlaskForm):
    header = StringField("Otsikoi resepti")
    category = StringField("Lisää kategoria")
    description = TextAreaField("Kirjoita kuvaus")
    ingredients = TextAreaField("Listaa ainekset")
    directions = TextAreaField("Listaa työvaiheet")
 
    class Meta:
        csrf = False


class EditForm(FlaskForm):
    header = StringField("Muokkaa otsikkoa")
    category = StringField("Muokkaa kategoriaa")
    description = TextAreaField("Muokkaa kuvausta")
    ingredients = TextAreaField("Muokkaa aineslistaa")
    directions = TextAreaField("Muokkaa työvaiheita")
 
    class Meta:
        csrf = False