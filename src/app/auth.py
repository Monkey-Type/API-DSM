from flask import Blueprint, render_template, url_for, flash
from flask_login.utils import login_user
from werkzeug.utils import redirect
from . import db, bcrypt
from .database.models import User
from .formulario.registerForm import *
from flask_login import login_required, logout_user, current_user
import re

routes = Blueprint('auth', __name__)
user = current_user


@routes.route('/register', methods=["GET", "POST"])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        cpfExistente = User.query.filter_by(cpf=form.cpf.data).first()
        #raExistente = User.query.filter_by(ra=form.ra.data).first()
        cpf = re.sub("[.-]", "", form.cpf.data)
        cpf = int(cpf)
        emailExistente = User.query.filter_by(email=form.email.data).first()
        #if cpfExistente or raExistente or emailExistente:
        if cpfExistente or emailExistente:
            flash("Este usuario ja existe!")
        else:
            hashed_password = bcrypt.generate_password_hash(
                form.senha.data).decode("utf-8")
            """ novoUsuario = User(email=form.email.data, ra=form.ra.data,
                               cpf=form.cpf.data, nome=form.nome.data.lower(), senha=hashed_password)"""
            novoUsuario = User(email=form.email.data,
                               cpf=cpf, nome=form.nome.data.lower(), senha=hashed_password)
            db.session.add(novoUsuario)
            db.session.commit()
            return redirect(url_for('auth.login'))
    return render_template("registrar.html", form=form)


@routes.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginFormulario()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user:
            if bcrypt.check_password_hash(user.senha, form.senha.data):
                login_user(user)
                return redirect(url_for('view.inicio'))
            else:
                flash('Senha ou email incorreto', 'danger')
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
        return redirect(url_for('auth.login'))
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
