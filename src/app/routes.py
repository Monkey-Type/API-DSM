from flask import Blueprint, render_template, url_for, request
from sqlalchemy.orm import session
from werkzeug.utils import redirect
from . import db
from .database.models import Postagem
from .database.models import User

routes = Blueprint('main', __name__)
user = User.query.filter_by(nome="UserAluno").first()


@routes.route('/config')
def config():
    return render_template('config.html')


@routes.route('/editar', methods=['POST', 'GET'])
def edit():
    userid = db.session.query(User.id).filter(User.nome == user.nome).one()
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
            return redirect(url_for('main.edit'))
    return render_template('editar.html', posts=posts, user=user)


@ routes.route('/')
def inicio():
    area = db.session.query(User.area).filter(User.nome == user.nome).first()
    posts = db.session.query(Postagem).filter(
        Postagem.recebido == area[0]).order_by(Postagem.data.desc()).all()
    # posts = Postagem.query.order_by(Postagem.data.desc()).all()
    # posts = Postagem.query.filter_by( recebido=area).order_by(Postagem.data.desc()).all()
    return render_template("home.html", posts=posts, user=user)


@ routes.route('/arquivos')
def archive():
    return render_template('arquivos.html', user=user)


@ routes.route('/login')
def login():
    return render_template('login.html')


@ routes.route('/esqueceu-senha')
def password():
    return render_template('esqueceu-senha.html')


@ routes.route('/senha-codigo')
def password_code():
    return render_template('senha-codigo.html')


@ routes.route('/codigo-correto')
def right_code():
    return render_template('codigo-correto.html')


@ routes.route('/sucesso')
def success():
    return render_template('sucesso.html')


@ routes.route('/register')
def register():
    return render_template('registrar.html')
