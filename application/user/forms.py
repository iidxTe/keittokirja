from flask_wtf import FlaskForm
from wtforms import StringField, ValidationError, validators

#LISÄÄ VALIDAATTOREITA

class EditUserForm(FlaskForm):
    header = StringField("Muokkaa nimeä", [validators.InputRequired])
    category = StringField("Muokkaa salasanaa", [validators.InputRequired])
 
    class Meta:
        csrf = False

