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
    if request.method == 'POST':

        remetente = request.form.get('remetente')
        assunto = request.form.get('assunto')
        texto = request.form.get('texto')
        informativo = Postagem(
            texto=texto, assunto=assunto, remetente=remetente)
        db.session.add(informativo)
        db.session.commit()
        return redirect('/')
    return render_template('editar.html')


@routes.route('/')
def inicio():
    posts = Postagem.query.order_by(Postagem.data.desc()).all()
    return render_template("home.html", posts=posts)


@routes.route('/arquivos')
def archive():
    return render_template('arquivos.html')
