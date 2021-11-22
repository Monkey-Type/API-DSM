from wtforms import SelectField, SelectMultipleField
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.fields.core import SelectMultipleField
from wtforms.validators import EqualTo, InputRequired, Length, Regexp, Email, ValidationError
from app import *
from wtforms.fields.html5 import EmailField
import re
from ..database.models import User


message = 'Este campo é necessario'


def _add_chosen_class(kwargs):
    '''
    Add the class 'chosen-select' to the HTML elements, keeping any
    other specified render parameters or other classes.
    '''
    if 'render_kw' in kwargs:
        if 'class' in kwargs['render_kw']:
            kwargs['render_kw']['class'] += ' chosen-select'
        else:
            kwargs['render_kw']['class'] = 'chosen-select'
    else:
        kwargs['render_kw'] = {'class': 'chosen-select'}


class ChosenSelectField(SelectField):
    '''A select field rendered with chosen'''

    def __init__(self, *args, **kwargs):
        _add_chosen_class(kwargs)
        super(ChosenSelectField, self).__init__(*args, **kwargs)


class ChosenSelectMultipleField(SelectMultipleField):
    '''A multiple-select field rendered with chosen'''

    def __init__(self, *args, **kwargs):
        _add_chosen_class(kwargs)
        super(ChosenSelectMultipleField, self).__init__(*args, **kwargs)


def cpf_validate(form, field):
    #  Obtém os números do CPF e ignora outros caracteres
    cpf = re.sub("[.-]", "", field.data)
    cpf_existente = User.query.filter_by(cpf=cpf).first()

    if cpf_existente:
        raise ValidationError('CPF existente')

    #  Verifica se o CPF tem 11 dígitos
    if len(cpf) != 11:
        raise ValidationError('Não tem 11 digitos')

    #  Verifica se o CPF tem todos os números iguais, ex: 111.111.111-11
    #  Esses CPFs são considerados inválidos mas passam na validação dos dígitos
    #  Antigo código para referência: if all(cpf[i] == cpf[i+1] for i in range (0, len(cpf)-1))
    if cpf == cpf[::-1]:
        raise ValidationError('Não pode números iguais')

    #  Valida os dois dígitos verificadores
    for i in range(9, 11):
        value = sum((int(cpf[num]) * ((i+1) - num) for num in range(0, i)))
        print(value)
        digit = ((value * 10) % 11) % 10
        print(digit)
        print(type(cpf[i]))
        if int(digit) != int(cpf[i]):
            raise ValidationError('Dois digitos verificadores errados')


class RegisterForm(FlaskForm):
    email = EmailField(validators=[InputRequired(message=message), Email(message='Digite um email')], render_kw={
        "placeholder": "exemple@fatec.sv.gov.br"})

    # ra = StringField('RA / Matricula', validators=[InputRequired(message=message), Length(
    #    min=13, max=13, message="Digite um RA valido")], render_kw={"placeholder": "RA / Matricula"})

    cpf = StringField(validators=[InputRequired(message=message), Regexp(
        '^\d{3}\.\d{3}\.\d{3}\-\d{2}$',  message='Digite um CPF'), cpf_validate], render_kw={"placeholder": "Sem traços ou espaços"})

    nome = StringField(validators=[InputRequired(message=message), Regexp("^([a-zA-Z]{2,}\\s[a-zA-Z]{1,}'?-?[a-zA-Z]{2,}\\s?([a-zA-Z]{1,})?)$", message='Digite nome e sobrenome')], render_kw={
        "placeholder": "Nome completo"})

    senha = PasswordField('Senha', validators=[InputRequired(message=message), Length(min=5, max=70, message="Senha deve ter pelomenos 5 caracteres"), EqualTo(
        'confirm', message='Senha e corfimação não conferrem')], render_kw={"placeholder": "Mínimo de 5 caracteres"})
    confirm = PasswordField('Confirmar senha', render_kw={
        "placeholder": "Mínimo de 5 caracteres"},
        validators=[InputRequired(message=message), Length(min=5, max=70, message="Senha deve ter pelomenos 5 caracteres"), EqualTo('senha', message='Senha e corfimação não conferrem')])

    '''def validaçãoUser(self, cpf):
        usuarioExistente = User.query.filter_by(cpf=cpf.data).first()

        if usuarioExistente:
            raise ValidationError(
                "Este usuario ja existe!")'''


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
    select = ChosenSelectMultipleField("Enviar para", choices=[])
    curso = ChosenSelectMultipleField("Para o curso", choices=[])


class NovaSenhaForm(FlaskForm):
    senha = PasswordField('Senha', validators=[InputRequired(message=message), Length(min=5, max=70, message="Senha deve ter pelomenos 5 caracteres"), EqualTo(
        'confirm', message='Senha e corfimação não conferrem')], render_kw={"placeholder": "Mínimo de 5 caracteres"})
    confirm = PasswordField('Confirmar senha', render_kw={
        "placeholder": "Mínimo de 5 caracteres"},
        validators=[InputRequired(message=message), Length(min=5, max=70, message="Senha deve ter pelomenos 5 caracteres"), EqualTo('senha', message='Senha e corfimação não conferrem')])
