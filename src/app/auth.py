from flask import Blueprint, render_template, url_for, flash
from flask_login.utils import login_user
from werkzeug.utils import redirect

#from app import email_service
from . import db, bcrypt
from .database.models import User
from .formulario.registerForm import *
from flask_login import login_required, logout_user, current_user
import re

# imports para token
from itsdangerous import URLSafeTimedSerializer, SignatureExpired
serial = URLSafeTimedSerializer('SENHASECRETA!') # app.config['SECRET_KEY']

from .email_service import EmailService
routes = Blueprint('auth', __name__)
user = current_user


@routes.route('/register', methods=["GET", "POST"])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        #print(form.cpf.data)
        cpf = int(re.sub("[.-]", "", form.cpf.data))
        #cpfExistente = User.query.filter_by(cpf=cpf).first()
        #raExistente = User.query.filter_by(ra=form.ra.data).first()
        emailExistente = User.query.filter_by(email=form.email.data).first()
        # if cpfExistente or raExistente or emailExistente:
        if emailExistente:
            flash("Este usuario ja existe!")
        else:
            hashed_password = bcrypt.generate_password_hash(
                form.senha.data).decode("utf-8")
            """ novoUsuario = User(email=form.email.data, ra=form.ra.data,
                               cpf=form.cpf.data, nome=form.nome.data.lower(), senha=hashed_password)"""
            novoUsuario = User(email=form.email.data,
                               cpf=cpf, nome=form.nome.data.lower(), senha=hashed_password, confirmado=0) ### setando novos cadastro para 0
            db.session.add(novoUsuario)
            db.session.commit()
            ServiceEmail = EmailService()
            ServiceEmail.confirmaEmail(novoUsuario.email)
            return redirect(url_for('auth.login'))
    return render_template("registrar.html", form=form)


@routes.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginFormulario()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user:
            if user.confirmado == 1: ## Verificando se ele confirmou email
                if bcrypt.check_password_hash(user.senha, form.senha.data):
                    login_user(user)
                    return redirect(url_for('view.inicio'))
                else:
                    flash('Senha ou email incorreto', 'danger')
            else:
                flash('Confirme o email enviado!', 'danger') # Mensagem para caso não
        else:
            flash('Senha ou email incorreto', 'danger')
    return render_template('login.html', form=form, title='Logue-se')


@routes.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))


@routes.route('/esqueceu-senha',  methods=['GET', 'POST'])
def password():
    form = EsqueceuFormulario()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user:
            user = User.query.filter_by(email=form.email.data).first()
            ServiceEmail = EmailService()
            ServiceEmail.esqueceuSenha(user.email)
            flash('Clique no Link enviado no seu email e acesse com a nova senha!') # HTML aqui para essa mensagem
            return redirect(url_for('auth.login'))
        else:
            flash('Use um e-mail válido!', 'info')
            return render_template('esqueceu-senha.html', form=form)
    return render_template('esqueceu-senha.html', form=form)


@routes.route('/senha-codigo')
def password_code():
    return render_template('senha-codigo.html')


@routes.route('/codigo-correto')
def right_code():
    return render_template('codigo-correto.html')


@routes.route('/sucesso')
def success():
    return render_template('sucesso.html')

@routes.route('/confirma_email/<token>') 
def confirma_email(token):   # se usar uma variável na URL utilize também como parâmetro na função
    form = RegisterForm()
    try:
        tokenVem = serial.loads(token, salt='email-confirm', max_age=30) # loads carrega o que tem no token para essa variável tokenVem, neste caso o email do usuário
        emailUsuario = User.query.filter_by(email=tokenVem).first()
        emailUsuario.confirmado=1
        db.session.commit()

    except SignatureExpired:
        tokenVencido = serial.loads(token, salt='email-confirm')
        Confirmado = User.query.filter_by(email=tokenVencido).first()
        if Confirmado.confirmado == 1:
            flash('Você já se cadastrou!')
            return render_template('login.html', form=form)
            
        else:
            Deletador = User.query.filter_by(email=tokenVencido).first()
            db.session.delete(Deletador)
            db.session.commit()
            flash('Cadastre-se Novamente')
        return render_template('registrar.html', form=form) # aqui html para o token expirado
    return render_template('login.html', form=form)


@routes.route('/esqueceu_senha/<token>') 
def esqueceu_senha(token):
    form = RegisterForm()
    try:
        tokenVem = serial.loads(token, salt='password-forgotten', max_age=60) # nesse tokenVem tem o email concatenado com a senha, separados por um ;
        emailToken = tokenVem.split(";")[0] # usando um split eu consigo separar o email da senha para usar em diferentes partes
        senhaToken = tokenVem.split(";")[1]
        emailUsuario = User.query.filter_by(email=emailToken).first()
        hashed_password = bcrypt.generate_password_hash(senhaToken).decode("utf-8") 
        emailUsuario.senha = hashed_password
        db.session.commit()

    except SignatureExpired:
        serial.loads(token, salt='password-forgotten')
        flash('Link expirado! Tente novamente.') # HTML aqui caso necessário
        return render_template('login.html', form=form)
    return render_template('login.html', form=form)


