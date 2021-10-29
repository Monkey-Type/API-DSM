from flask import Blueprint, render_template, url_for, request, jsonify, json, request
from flask_login import login_required, current_user
import sqlalchemy
from sqlalchemy import sql
from wtforms.fields.core import SelectField
from .database.models import Postagem, User, Papel
from werkzeug.utils import redirect
from . import db
from .formulario.registerForm import *

routes = Blueprint('view', __name__)

user = current_user


def user_edit():
    user_edit = db.session.query(Papel.pode_editar).join(
        Papel.user).filter(User.id == user.id).all()
    for edit in user_edit:
        if edit:
            user_edit = edit[0]
        break
    return user_edit


@routes.route('/select', methods=["GET", "POST"])
def select():
    form = SelectForm()

    return render_template('formselect.html', form=form)


@routes.route('/', methods=["GET", "POST"])
@login_required
def inicio():
    print(user.papeis)
    cargo = request.args.get(User.query.filter_by(id=user.papeis))
    posts = db.session.query(Postagem).join(Postagem.destinatario).join(
        Papel.user).filter(User.id == user.id).all()
    print(posts)
    return render_template("home.html", user=user, posts=posts, cargo=cargo, user_edit=user_edit())


@ routes.route('/editar', methods=['POST', 'GET'])
@ login_required
def edit():
    papel = db.session.query(Papel).all()
    # print(user_edit())
    if not user_edit():
        return redirect(url_for('view.inicio'))
    posts = db.session.query(Postagem).filter(
        Postagem.user_id == user.id).all()
    if request.method == 'POST':
        titulo = request.form.get('titulo')
        texto = request.form.get('texto')
        if user_edit():
            informativo = Postagem(
                titulo=titulo, texto=texto, user_id=user.id)
            db.session.add(informativo)
            db.session.commit()
            return redirect(url_for('view.edit'))
    return render_template('editar.html', posts=posts, user=user, papel=papel, user_edit=user_edit())


# Deletar Post
@ routes.route('/deletar-post', methods=['POST'])
@ login_required
def deletar_post():
    post = json.loads(request.data)
    postId = post['postId']
    post = Postagem.query.get(postId)
    if user.id == post.user_id:
        db.session.delete(post)
        db.session.commit()
    return jsonify({})


@ routes.route('/arquivos')
@ login_required
def archive():
    return render_template('arquivos.html', user=user, user_edit=user_edit())


@ routes.route('/config')
@ login_required
def config():
    return render_template('config.html', user=user, user_edit=user_edit())
