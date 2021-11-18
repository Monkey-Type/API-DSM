#from  import app
#from auth import request, url_for
from flask import url_for
from flask_mail import Message
from . import mail

from itsdangerous import URLSafeTimedSerializer
serial = URLSafeTimedSerializer('SENHASECRETA!') # app.config['SECRET_KEY']

class EmailService():
    def confirmaEmail(self, email):
        ema = email   
        tokenVai = serial.dumps(ema, salt='email-confirm') # .dumbs criará o token e salt irá usar tokens diferentes para diferentes tipos de uso, lembrar de esconder essa senha do salt

        mensagem = Message('Email de Confirmação', recipients=[ema])
        link = url_for('auth.confirma_email', token=tokenVai, _external=True) # _external=True faz com que a URL não seja apenas relativa
        mensagem.body = 'Seu link de confirmação é: {}'.format(link)

        mail.send(mensagem)
        return tokenVai
    
    def esqueceuSenha(self, email):
        emo = email
        tokenVao = serial.dumps(emo, salt='password-forgotten')
        mensagem = Message("Criação de nova senha", recipients=[emo])
        link = url_for('auth.esqueceu_senha', token=tokenVao, _external=True)
        
        mensagem.body = 'Esqueceu a sua senha? Após clicar no link crie uma nova senha: {}'.format(link)
        mail.send(mensagem)
        
        return tokenVao