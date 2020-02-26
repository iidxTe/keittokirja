from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, validators
  
class LoginForm(FlaskForm):
    name = StringField("Nimi", [validators.InputRequired])
    password = PasswordField("Salasana", [validators.InputRequired])
  
    class Meta:
        csrf = False

class RegisterForm(FlaskForm):
    name = StringField("Nimi", [validators.Length(min=2, max=20)])
    password = PasswordField("Salasana", [validators.Length(min=5, max=20)])
  
    class Meta:
        csrf = False