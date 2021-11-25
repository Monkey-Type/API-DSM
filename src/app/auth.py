from .email_service import EmailService
from flask import Blueprint, render_template, url_for, flash
from flask_login.utils import login_user
from sqlalchemy.orm import session
from werkzeug.utils import redirect
from werkzeug.wrappers import request

#from app import email_service
from .import db, bcrypt
from .database.models import User, Papel
from .formulario.registerForm import *
from flask_login import login_required, logout_user, current_user
import re
from .controller import tupleToString

# imports para token
from itsdangerous import URLSafeTimedSerializer, SignatureExpired
serial = URLSafeTimedSerializer('SENHASECRETA!')  # app.config['SECRET_KEY']

routes = Blueprint('auth', __name__)
user = current_user


@routes.route('/register', methods=["GET", "POST"])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        #raExistente = User.query.filter_by(ra=form.ra.data).first()

        hashed_password = bcrypt.generate_password_hash(
            form.senha.data).decode("utf-8")
        novoUsuario = User(email=form.email.data,
                           nome=form.nome.data.lower(), senha=hashed_password, confirmado=0)  # setando novos cadastro para 0
        db.session.add(novoUsuario)
        db.session.commit()
        ServiceEmail = EmailService()
        ServiceEmail.confirmaEmail(novoUsuario.email)
        flash('Clique no Link enviado no seu email para confirmá-lo!', 'info')
        return redirect(url_for('auth.login'))
    return render_template("registrar.html", form=form)


@routes.route('/registrar2', methods=['GET', 'POST'])
def registrar2():
    form = InfoForm()
    if form.validate_on_submit():
        registro = form.ra.data
        aluno_papel = Papel.query.filter_by(nome='Aluno').first()
        funcionario_papel = Papel.query.filter_by(nome='Funcionário').first()
        cpf = int(re.sub("[.-]", "", form.cpf.data))
        user.cpf = cpf
        if len(registro) == 7:
            user.papeis = [funcionario_papel]
            db.session.commit()
            return redirect(url_for('auth.cursofuncionario'))
        elif len(registro) == 13:
            user.papeis = [aluno_papel]
            db.session.commit()
            return redirect(url_for('auth.cursoaluno'))
        else:
            flash('Você não existe', 'danger')
    return render_template('registrar-2.html', form=form)


@routes.route('/conclusaoregistro', methods=['GET', 'POST'])
def cursoaluno():
    form = SelectForm()
    curso_list = form.curso.data

    if curso_list:
        curso_list = list(map(int, curso_list))
        curso = Curso.query.filter(Curso.id.in_(curso_list)).all()
        print(curso)
        user.cursos = curso
        db.session.commit()
        print(user)
        return redirect(url_for('view.inicio'))

    return render_template('curso-aluno.html', form=form)

# @routes.route('/conclusaoregistro2', methods=['GET', 'POST'])
# def cursofuncionario():
    form = InfoForm()
    return render_template('curso-funcionario.html', form=form)


@routes.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginFormulario()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user:
            if user.confirmado == 1:  # Verificando se ele confirmou email
                if bcrypt.check_password_hash(user.senha, form.senha.data):
                    login_user(user)
                    cpf = tupleToString(db.session.query(
                        User.cpf).filter_by(cpf=user.cpf).first())
                    print(cpf)
                    if cpf == '':
                        return redirect(url_for('auth.registrar2'))
                    else:
                        return redirect(url_for('view.inicio'))
                else:
                    flash('Senha ou email incorreto', 'danger')
            else:
                # Mensagem para caso não
                flash('Confirme o email enviado!', 'danger')
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
            # HTML aqui para essa mensagem
            flash(
                'Clique no Link enviado no seu email e acesse com a nova senha!', 'info')
            return redirect(url_for('auth.password'))
        else:
            flash('Use um e-mail válido!', 'danger')
    return render_template('esqueceu-senha.html', form=form)


@routes.route('/senha-codigo')
def password_code():
    return render_template('senha-codigo.html')


@routes.route('/codigo-correto', methods=['GET', 'POST'])
def codigo_correto():
    form = NovaSenhaForm()
    if form.validate_on_submit():
        user = User.query.filter_by(id=current_user.id).first()
        hashed_password = bcrypt.generate_password_hash(
            form.senha.data).decode("utf-8")
        user.senha = hashed_password
        db.session.commit()
    return render_template('sucesso.html', form=form)


@routes.route('/sucesso')
def success():
    return render_template('sucesso.html')


@routes.route('/confirma_email/<token>')
# se usar uma variável na URL utilize também como parâmetro na função
def confirma_email(token):
    form = RegisterForm()
    try:
        # loads carrega o que tem no token para essa variável tokenVem, neste caso o email do usuário
        tokenVem = serial.loads(token, salt='email-confirm', max_age=3600)
        emailUsuario = User.query.filter_by(email=tokenVem).first()
        emailUsuario.confirmado = 1
        db.session.commit()

    except SignatureExpired:
        tokenVencido = serial.loads(token, salt='email-confirm')
        Confirmado = User.query.filter_by(email=tokenVencido).first()
        if Confirmado.confirmado == 1:
            flash('Você já se cadastrou!', 'danger')
            return render_template('login.html', form=form)

        else:
            Deletador = User.query.filter_by(email=tokenVencido).first()
            db.session.delete(Deletador)
            db.session.commit()
            flash('Seu link expirou, cadastre-se novamente', 'erro')
        # aqui html para o token expirado
        return render_template('registrar.html', form=form)
    flash('Cadastro feito com sucesso!', 'info')
    return render_template('login.html', form=form)


@routes.route('/esqueceu_senha/<token>')
def esqueceu_senha(token):
    form = RegisterForm()
    try:
        # nesse tokenVem tem o email concatenado com a senha, separados por um ;
        tokenVem = serial.loads(token, salt='password-forgotten', max_age=3600)
        emailUsuario = User.query.filter_by(email=tokenVem).first()
        login_user(emailUsuario)

    except SignatureExpired:
        serial.loads(token, salt='password-forgotten')
        flash('Link expirado! Tente novamente.')  # HTML aqui caso necessário
        return render_template('esqueceu-senha.html', form=form)
    return render_template('codigo-correto.html', form=form)
