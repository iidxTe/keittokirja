from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, validators
  
class LoginForm(FlaskForm):
    name = StringField("Name", [validators.InputRequired])
    password = PasswordField("Password", [validators.InputRequired])
  
    class Meta:
        csrf = False

class RegisterForm(FlaskForm):
    name = StringField("Name", [validators.Length(min=2)])
    password = PasswordField("Password", [validators.Length(min=5)])
  
    class Meta:
        csrf = False