from wtforms import StringField, PasswordField, SubmitField, IntegerField, validators
from wtforms.form import Form
from wtforms.validators import InputRequired, Length, ValidationError
from app import *
# from flask_wtf.form import FlaskForm
from wtforms.fields.html5 import EmailField

class RegisterForm(Form):
    nome = StringField(validators=[InputRequired(), Length(
        min=4, max=100)], render_kw={"placeholder": "nome"})

    senha = PasswordField('senha', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message='senha e corfimação não conferrem')
    ] )
    confirm = PasswordField('Digite sua senha')

    ra = IntegerField(validators=[InputRequired(), Length(
        min=4, max=50)], render_kw={"placeholder": "RA / Matricula"})

    cpf = IntegerField(validators=[InputRequired(), Length(
        min=4, max=50)], render_kw={"placeholder": "cpf"})

    email = EmailField(validators=[InputRequired(), Length(
        min=5, max=70)], render_kw={"placeholder": "email"})

    enviar = SubmitField()

    def validaçãoUser(self, cpf):
        usuarioExistente = User.query.filter_by(cpf=cpf.data).first()

        if usuarioExistente:
            raise ValidationError(
                "Este usuario ja existe!")

class LoginFormulario(Form):
    email = StringField('Email',[validators.length(min=6, max=35)])
    senha = PasswordField('Sua senha', [validators.DataRequired()])