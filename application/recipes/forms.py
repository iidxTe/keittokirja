from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, validators

class NewForm(FlaskForm):
    header = StringField("Otsikoi resepti", [validators.InputRequired])
    category = StringField("Lisää kategoria", [validators.InputRequired])
    description = TextAreaField("Kirjoita kuvaus")
    ingredients = TextAreaField("Listaa ainekset", [validators.InputRequired])
    directions = TextAreaField("Listaa työvaiheet", [validators.InputRequired])
 
    class Meta:
        csrf = False


class EditForm(FlaskForm):
    header = StringField("Muokkaa otsikkoa", [validators.InputRequired])
    category = StringField("Muokkaa kategoriaa", [validators.InputRequired])
    description = TextAreaField("Muokkaa kuvausta")
    ingredients = TextAreaField("Muokkaa aineslistaa", [validators.InputRequired])
    directions = TextAreaField("Muokkaa työvaiheita", [validators.InputRequired])
 
    class Meta:
        csrf = False