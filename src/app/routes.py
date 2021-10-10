from os import remove
from flask import Blueprint, render_template, url_for, request, flash
from flask_login.utils import login_user
from sqlalchemy.orm import session
from werkzeug.utils import redirect
from . import db, bcrypt, login_manager
from .database.models import Postagem
from .database.models import User
from .formulario.registerForm import RegisterForm, LoginFormulario
from flask_login import login_required, logout_user, current_user
from werkzeug.security import generate_password_hash


routes = Blueprint('main', __name__)
user = current_user


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


@routes.route('/register', methods=["GET", "POST"])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        cpfExistente = User.query.filter_by(cpf=form.cpf.data).first()
        raExistente = User.query.filter_by(ra=form.ra.data).first()
        emailExistente = User.query.filter_by(email=form.email.data).first()
        if cpfExistente or raExistente or emailExistente:
            flash("Este usuario ja existe!")
        else:
            hashed_password = bcrypt.generate_password_hash(
                form.senha.data).decode("utf-8")
            novoUsuario = User(email=form.email.data, ra=form.ra.data,
                               cpf=form.cpf.data, nome=form.nome.data.lower(), senha=hashed_password)
            db.session.add(novoUsuario)
            db.session.commit()
            return redirect(url_for('main.login'))
    return render_template("registrar.html", form=form)


@routes.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginFormulario()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user:
            if bcrypt.check_password_hash(user.senha, form.senha.data):
                login_user(user)
                # session['email'] = form.email.data
                return redirect(url_for('main.inicio'))
            else:
                flash('Senha ou email incorreto', 'danger')
        else:
            flash('Senha ou email incorreto', 'danger')
    return render_template('login.html', form=form, title='Logue-se')


@routes.route('/esqueceu-senha')
def password():
    return render_template('esqueceu-senha.html')


@routes.route('/senha-codigo')
def password_code():
    return render_template('senha-codigo.html')


@routes.route('/codigo-correto')
def right_code():
    return render_template('codigo-correto.html')


@routes.route('/sucesso')
def success():
    return render_template('sucesso.html')


@routes.route('/', methods=["GET", "POST"])
@login_required
def inicio():
    # area = db.session.query(User.area).filter(User.nome == user.nome).first()
    # posts = db.session.query(Postagem).filter(Postagem.recebido == area[0]).order_by(Postagem.data.desc()).all()
    # posts = Postagem.query.order_by(Postagem.data.desc()).all()
    posts = Postagem.query.filter_by(
        recebido=user.cargo).order_by(Postagem.data.desc()).all()
    return render_template("home.html", posts=posts, user=user)


@routes.route('/arquivos')
@login_required
def archive():
    return render_template('arquivos.html', user=user)


@routes.route('/config')
@login_required
def config():
    return render_template('config.html', user=user)


@routes.route('/editar', methods=['POST', 'GET'])
@login_required
def edit():
    if not user.envia:
        return redirect(url_for('main.inicio'))
    posts = db.session.query(Postagem).filter(
        Postagem.user_id == user.id).order_by(Postagem.data.desc()).all()
    if request.method == 'POST':
        recebido = request.form.get('recebido')
        assunto = request.form.get('assunto')
        texto = request.form.get('texto')
        if user.envia == 1:
            informativo = Postagem(
                texto=texto, assunto=assunto, recebido=recebido, remetente=user.cargo, user_id=user.id)
            db.session.add(informativo)
            db.session.commit()
            return redirect(url_for('main.edit'))
    return render_template('editar.html', posts=posts, user=user)


@routes.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.inicio'))
