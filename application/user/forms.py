from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, ValidationError, validators

class EditUserForm(FlaskForm):
    name = StringField("Muokkaa nimeä", [validators.Length(min=2, max=20)])
    password = PasswordField("Muokkaa salasanaa", [validators.Length(min=5, max=20)])
 
    class Meta:
        csrf = False

