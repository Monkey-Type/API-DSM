from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, IntegerField, validators
from wtforms.validators import InputRequired, Length, ValidationError, Email
from app import *
# from flask_wtf.form import FlaskForm
from wtforms.fields.html5 import EmailField


class RegisterForm(FlaskForm):
    email = EmailField(validators=[InputRequired(), Email()], render_kw={
                       "placeholder": "exemple@fatec.sv.gov.br"})

    ra = StringField('RA / Matricula', validators=[InputRequired(), Length(
        min=4, max=50, message="Digite um RA valido")], render_kw={"placeholder": "RA / Matricula"})

    cpf = StringField(validators=[InputRequired(), Length(
        min=4, max=50, message="Digite um CPF valido")], render_kw={"placeholder": "Sem traços ou espaços"})

    nome = StringField(validators=[InputRequired(),  Length(
        min=5, max=70)], render_kw={
        "placeholder": "Nome completo"})

    senha = PasswordField('Senha', [
        validators.DataRequired(),
        validators.EqualTo(
            'confirm', message='Senha e corfimação não conferrem'),
        validators.Length(
            min=5, max=70, message="Senha deve ter pelomenos 5 caracteres")
    ], render_kw={
        "placeholder": "Mínimo de 5 caracteres"})
    confirm = PasswordField('Confirmar senha', render_kw={
        "placeholder": "Mínimo de 5 caracteres"},
        validators=[InputRequired(), Length(min=5, max=70, message="Senha deve ter pelomenos 5 caracteres")])

    '''def validaçãoUser(self, cpf):
        usuarioExistente = User.query.filter_by(cpf=cpf.data).first()

        if usuarioExistente:
            raise ValidationError(
                "Este usuario ja existe!")'''


class LoginFormulario(FlaskForm):
    email = StringField('Email', validators=[InputRequired(), Email(message='Digite um email valido')], render_kw={
                        "placeholder": "exemple@fatec.sp.gov.br"})
    senha = PasswordField('Senha', validators=[InputRequired(), Length(
        min=2, max=100, message='Senha deve ter pelomenos 5 caracteres')], render_kw={
        "placeholder": "Mínimo de 5 caracteres"})
