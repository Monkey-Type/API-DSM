from flask import Blueprint, render_template, url_for, request
from werkzeug.utils import redirect
from . import db
from .database.models import Postagem

routes = Blueprint('main', __name__)


@routes.route('/config')
def config():
    return render_template('config.html')


@routes.route('/editar', methods=['POST', 'GET'])
def edit():
    posts = Postagem.query.order_by(Postagem.data.desc()).all()
    if request.method == 'POST':

        recebido = request.form.get('recebido')
        assunto = request.form.get('assunto')
        texto = request.form.get('texto')
        informativo = Postagem(
            texto=texto, assunto=assunto, recebido=recebido)
        db.session.add(informativo)
        db.session.commit()
        return redirect('/')
    return render_template('editar.html', posts=posts)


@routes.route('/')
def inicio():
    posts = Postagem.query.order_by(Postagem.data.desc()).all()
    return render_template("home.html", posts=posts)


@routes.route('/arquivos')
def archive():
    return render_template('arquivos.html')


@routes.route('/login')
def login():
    return render_template('login.html')


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


@routes.route('/register')
def register():
    return render_template('registrar.html')
