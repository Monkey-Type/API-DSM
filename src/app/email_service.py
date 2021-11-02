#from  import app
#from auth import request, url_for
import os
from flask import url_for

from flask_mail import Message

from . import mail

from itsdangerous import URLSafeTimedSerializer, SignatureExpired
serial = URLSafeTimedSerializer('SENHASECRETA!') # app.config['SECRET_KEY']

class EmailService():
    def confirmaEmail(self, email):
        ema = email   
        tokenVai = serial.dumps(ema, salt='email-confirm') # .dumbs criará o token e salt irá usar tokens diferentes para diferentes tipos de uso, para evitar duplicação

        mensagem = Message('Email de Confirmação', recipients=[ema])
        link = url_for('auth.confirma_email', token=tokenVai, _external=True) # _external=True faz com que a URL não seja apenas relativa
        mensagem.body = 'Seu link de confirmação é: {}'.format(link)

        mail.send(mensagem)
        return '<h1>O email que você entrou é este: {}. O seu Token é:</h1><h2 style="color: blue"><b> {}</b></h2>'.format(ema, tokenVai)
    