from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField
  
class LoginForm(FlaskForm):
    name = StringField("Name")
    password = PasswordField("Password")
  
    class Meta:
        csrf = False