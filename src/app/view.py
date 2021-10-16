from os import remove
from flask import Blueprint, render_template, url_for, request, flash, jsonify, json
from flask_login.utils import login_user
from sqlalchemy.orm import session
from werkzeug.utils import redirect
from . import db, bcrypt, login_manager
from .database.models import Postagem
from .database.models import User
from .formulario.registerForm import RegisterForm, LoginFormulario
from flask_login import login_required, logout_user, current_user
from werkzeug.security import generate_password_hash

routes = Blueprint('view', __name__)
user = current_user


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


@routes.route('/', methods=["GET", "POST"])
@login_required
def inicio():
    posts = Postagem.query.filter_by(
        recebido=user.cargo).order_by(Postagem.data.desc()).all()
    return render_template("home.html", posts=posts, user=user)


@routes.route('/editar', methods=['POST', 'GET'])
@login_required
def edit():
    if not user.envia:
        return redirect(url_for('view.inicio'))
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
            return redirect(url_for('view.edit'))
    return render_template('editar.html', posts=posts, user=user)


# Deletar Post
@routes.route('/deletar-post', methods=['POST'])
@login_required
def deletar_post():
    post = json.loads(request.data)
    postId = post['postId']
    post = Postagem.query.get(postId)
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


@routes.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))
