from flask import Blueprint, render_template, url_for, request
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
user = User.query.filter_by(nome="UserAluno").first()


@routes.route('/config')
@login_required
def config():
    return render_template('config.html')


@routes.route('/editar', methods=['POST', 'GET'])
@login_required
def edit():
    '''userid = db.session.query(User.id).filter(User.nome == user.nome).one()
    posts = db.session.query(Postagem).filter(
        Postagem.user_id == userid[0]).order_by(Postagem.data.desc()).all()
    remetente = db.session.query(User.area).filter(
        User.nome == user.nome).one()
    #posts = Postagem.query.order_by(Postagem.data.desc()).all()
    print(user)
    if request.method == 'POST':

        recebido = request.form.get('recebido')
        assunto = request.form.get('assunto')
        texto = request.form.get('texto')
        if user.cargo == 1:
            informativo = Postagem(
                texto=texto, assunto=assunto, recebido=recebido, remetente=remetente[0], user_id=userid[0])
            db.session.add(informativo)
            db.session.commit()
            return redirect(url_for('main.edit'))'''
    posts = Postagem.query.order_by(Postagem.data.desc()).all()
    return render_template('editar.html', posts=posts)


@routes.route('/', methods=["GET", "POST"])
@login_required
def inicio():
    #area = db.session.query(User.area).filter(User.nome == user.nome).first()
    #posts = db.session.query(Postagem).filter(Postagem.recebido == area[0]).order_by(Postagem.data.desc()).all()
    # posts = Postagem.query.order_by(Postagem.data.desc()).all()
    # posts = Postagem.query.filter_by( recebido=area).order_by(Postagem.data.desc()).all()
    posts = Postagem.query.order_by(Postagem.data.desc()).all()
    return render_template("home.html", posts=posts)


@routes.route('/arquivos')
@login_required
def archive():
    return render_template('arquivos.html')


@routes.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginFormulario(request.form)
    if request.method == 'POST' and form.validate():
        user = User.query.filter_by(email=form.email.data).first()
        if user:
            if bcrypt.check_password_hash(user.senha,form.senha.data):
                login_user(user)
                #session['email'] = form.email.data
                return redirect(url_for('main.inicio'))
    return render_template('login.html', form=form, title='Logue-se')


@routes.route('/esqueceu-senha')
@login_required
def password():
    return render_template('esqueceu-senha.html')


@routes.route('/senha-codigo')
@login_required
def password_code():
    return render_template('senha-codigo.html')


@routes.route('/codigo-correto')
@login_required
def right_code():
    return render_template('codigo-correto.html')


@routes.route('/sucesso')
@login_required
def success():
    return render_template('sucesso.html')


@routes.route('/register', methods=["GET", "POST"])
def register():
    form = RegisterForm(request.form)
    if request.method == "POST":
        hashed_password = bcrypt.generate_password_hash(
            form.senha.data).decode("utf-8")
        novoUsuario= User(email=form.email.data, ra=form.ra.data, 
            cpf=form.cpf.data, nome=form.nome.data.lower(), senha=hashed_password)
        db.session.add(novoUsuario)
        db.session.commit()
        return redirect(url_for('main.login'))
    return render_template("registrar.html", form=form)

@routes.route("/logout", methods=["GET"])
@login_required
def logout():
    user = current_user
    user.authenticated = False
    db.session.add(user)
    db.session.commit()
    logout_user()
    return render_template("login.html")

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)
