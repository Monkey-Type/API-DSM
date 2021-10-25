from flask import Blueprint, render_template, url_for, request, jsonify, json, request
from flask_login import login_required, current_user
import sqlalchemy
from sqlalchemy import sql
from .database.models import Postagem, User, Papel
from werkzeug.utils import redirect
from . import db

routes = Blueprint('view', __name__)
user = current_user


@routes.route('/', methods=["GET", "POST"])
@login_required
def inicio():
    print(user.papeis)
    cargo = request.args.get(User.query.filter_by(id=user.papeis))
    print(db.session.query(Postagem.papeis))
    return render_template("home.html", user=user,  cargo=cargo)


@routes.route('/editar', methods=['POST', 'GET'])
@login_required
def edit():
    if not user.pode_editar:
        return redirect(url_for('view.inicio'))
    posts = db.session.query(Postagem).filter(
        Postagem.user_id == user.id).order_by(Postagem.data.desc()).all()
    if request.method == 'POST':
        recebido = request.form.get('recebido')
        assunto = request.form.get('assunto')
        texto = request.form.get('texto')
        if user.pode_editar == 1:
            informativo = Postagem(
                texto=texto, assunto=assunto, remetente=user.cargo, user_id=user.id)
            db.session.add(informativo)
            db.session.commit()
            return redirect(url_for('view.edit'))
    return render_template('editar.html', posts=posts, user=user, recebido=recebido)


# Deletar Post
@routes.route('/deletar-post', methods=['POST'])
@login_required
def deletar_post():
    post = json.loads(request.data)
    postId = post['postId']
    post = Postagem.query.get(postId)
    if user.id == post.user_id:
        db.session.delete(post)
        db.session.commit()
    return jsonify({})


@routes.route('/arquivos')
@login_required
def archive():
    return render_template('arquivos.html', user=user)


@routes.route('/config')
@login_required
def config():
    return render_template('config.html', user=user)
