from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, validators

class NewForm(FlaskForm):
    header = StringField("Otsikoi resepti", [validators.InputRequired])
    category = StringField("Lisää kategoria", [validators.InputRequired])
    description = TextAreaField("Kirjoita kuvaus")

    ingredientName = TextAreaField("Lisää ainesosa", [validators.InputRequired])
    ingredientAmount = TextAreaField("Lisää määrä")
    ingredientUnit = TextAreaField("Lisää yksikkö")

    directions = TextAreaField("Listaa työvaiheet", [validators.InputRequired])
 
    class Meta:
        csrf = False


class EditForm(FlaskForm):
    header = StringField("Muokkaa otsikkoa", [validators.InputRequired])
    category = StringField("Muokkaa kategoriaa", [validators.InputRequired])
    description = TextAreaField("Muokkaa kuvausta")

    ingredientName = TextAreaField("Muokkaa ainesosaa", [validators.InputRequired])
    ingredientAmount = TextAreaField("Muokkaa määrää")
    ingredientUnit = TextAreaField("Muokkaa yksikköä")

    directions = TextAreaField("Muokkaa työvaiheita", [validators.InputRequired])
 
    class Meta:
        csrf = False