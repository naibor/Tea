from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import data_required, input_required
from wtforms.fields.html5 import EmailField
class SignupForm(FlaskForm):
    name = StringField("enter your name", validators=[data_required()])
    username = StringField("username",validators=[data_required(),input_required()])
    email = EmailField ("email", validators=[data_required(), input_required()])
    password = PasswordField ("password", validators=[data_required(), input_required()])
    confirm_password = PasswordField ("confirm password", validators=[data_required(), input_required()])
    submit = SubmitField("send")