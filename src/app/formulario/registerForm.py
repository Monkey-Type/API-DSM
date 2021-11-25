from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import EqualTo, InputRequired, Length, Regexp, Email
from app import *
from wtforms.fields.html5 import EmailField
from .chosenSelect import *
from .customValidators import *
from ..database.models import Papel, Curso
from flask_login import current_user

message = 'Este campo é necessario'


class RegisterForm(FlaskForm):
    email = EmailField(validators=[InputRequired(message=message), Email(message='Digite um email'), emailExistente], render_kw={
        "placeholder": "exemple@fatec.sv.gov.br"})

    nome = StringField(validators=[InputRequired(message=message)], render_kw={
        "placeholder": "Nome completo"})

    senha = PasswordField('Senha', validators=[InputRequired(message=message), Length(min=5, max=70, message="Senha deve ter pelomenos 5 caracteres"), EqualTo(
        'confirm', message='Senha e corfimação não conferrem')], render_kw={"placeholder": "Mínimo de 5 caracteres"})
    confirm = PasswordField('Confirmar senha', render_kw={
        "placeholder": "Mínimo de 5 caracteres"},
        validators=[InputRequired(message=message), Length(min=5, max=70, message="Senha deve ter pelomenos 5 caracteres"), EqualTo('senha', message='Senha e corfimação não conferrem')])


class InfoForm(FlaskForm):
    ra = StringField('RA / Matrícula', validators=[InputRequired(message=message), Length(
        min=7, max=13, message="Digite um RA/Matrícula valido")], render_kw={"placeholder": "RA / Matrícula"})

    cpf = StringField(validators=[InputRequired(message=message), Regexp(
        '^\d{3}.\d{3}.\d{3}-\d{2}$',  message='Digite um CPF'), cpf_validate], render_kw={"placeholder": "Sem traços ou espaços"})


class LoginFormulario(FlaskForm):
    email = EmailField('Email', validators=[InputRequired(message=message), Email(message='Digite um email')], render_kw={
        "placeholder": "exemple@fatec.sp.gov.br"})
    senha = PasswordField('Senha', validators=[InputRequired(message=message), Length(
        min=5, max=100, message='Senha deve ter pelomenos 5 caracteres')], render_kw={
        "placeholder": "Mínimo de 5 caracteres"})


class EsqueceuFormulario(FlaskForm):
    email = EmailField('Email', validators=[InputRequired(message=message), Email(message='Digite um email')], render_kw={
        "placeholder": "exemple@fatec.sp.gov.br"})


class SelectForm(FlaskForm):
    papel = ChosenSelectMultipleField("Enviar para", choices=[])
    curso = ChosenSelectMultipleField("Para o curso", choices=[])

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.papel.choices = [(papel.id, papel.nome)
                              for papel in Papel.query.join(Papel.user).all()]
        self.curso.choices = [(curso.id, curso.nome_curso)
                              for curso in Curso.query.join(Curso.user).filter(User.id != current_user.id).all()]


class FiltroForm(FlaskForm):
    filtro_papel = ChosenSelectMultipleField("Enviar para", choices=[])
    filtro_curso = ChosenSelectMultipleField("Para o curso", choices=[])

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.filtro_papel.choices = [(papel.id, papel.nome)
                                     for papel in Papel.query.join(Papel.user).all()]
        self.filtro_curso.choices = [(curso.id, curso.nome_curso)
                                     for curso in Curso.query.join(Curso.user).filter(User.id != current_user.id).all()]


class NovaSenhaForm(FlaskForm):
    senha = PasswordField('Senha', validators=[InputRequired(message=message), Length(min=5, max=70, message="Senha deve ter pelomenos 5 caracteres"), EqualTo(
        'confirm', message='Senha e corfimação não conferrem')], render_kw={"placeholder": "Mínimo de 5 caracteres"})
    confirm = PasswordField('Confirmar senha', render_kw={
        "placeholder": "Mínimo de 5 caracteres"},
        validators=[InputRequired(message=message), Length(min=5, max=70, message="Senha deve ter pelomenos 5 caracteres"), EqualTo('senha', message='Senha e corfimação não conferrem')])
