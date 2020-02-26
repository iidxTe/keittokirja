from flask_wtf import FlaskForm
from wtforms import StringField, ValidationError, validators

#LISÄÄ VALIDAATTOREITA

class EditUserForm(FlaskForm):
    name = StringField("Muokkaa nimeä", [validators.InputRequired])
    password = StringField("Muokkaa salasanaa", [validators.InputRequired])
 
    class Meta:
        csrf = False

