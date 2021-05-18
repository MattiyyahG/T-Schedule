from flask.templating import render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired()])
    password = PasswordField("Senha", validators=[DataRequired()])
    remember_me = BooleanField("Recordar registro")
    submit = SubmitField("Acessar")


class CadastroForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired()])
    password = PasswordField("Senha", validators=[DataRequired()])
    submit = SubmitField("Submeter")   