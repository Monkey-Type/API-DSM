#from  import app
#from auth import request, url_for
from flask import url_for
from flask_mail import Message
from . import mail

from itsdangerous import URLSafeTimedSerializer
serial = URLSafeTimedSerializer('SENHASECRETA!') # app.config['SECRET_KEY']

# identificador único universal (uuid) utilizo apenas os 5 primeiros digitos que ele gera
import uuid
def gerador_de_senhas(string_length=5):
    random = str(uuid.uuid4())
    random = random.upper()
    random = random.replace("-", "")
    return random[0:string_length]

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
        ema = gerador_de_senhas()
        fusao = emo + ";" + ema
        tokenVao = serial.dumps(fusao, salt='password-forgotten')
        
        mensagem = Message("Criação de nova senha", recipients=[fusao])
        link = url_for('auth.esqueceu_senha', token=tokenVao, _external=True)
        
        mensagem.body = 'Esqueceu a sua senha? Após clicar no link, use a senha "{}" para entrar: {}'.format(ema, link)
        mail.send(mensagem)
        
        return tokenVao