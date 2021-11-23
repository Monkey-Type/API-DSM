from wtforms.validators import ValidationError
from ..database.models import User
import re

message = 'Este usuario já existe!'


def emailExistente(form, field):
    if User.query.filter_by(email=field.data).first():
        raise ValidationError(message)


def cpf_validate(form, field):
    #  Obtém os números do CPF e ignora outros caracteres
    cpf = re.sub("[.-]", "", field.data)
    cpf_existente = User.query.filter_by(cpf=cpf).first()

    if cpf_existente:
        raise ValidationError(message)

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
