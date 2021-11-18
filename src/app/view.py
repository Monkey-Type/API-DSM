from operator import pos
from flask import Blueprint, render_template, url_for, request, jsonify, json, request, Response
from flask_login import login_required, current_user
import sqlalchemy
from sqlalchemy import *
from wtforms.fields.core import SelectField
from .database.models import Arquivadas, Postagem, User, Papel, Curso
from werkzeug.utils import redirect, secure_filename, send_file
from . import db
from .formulario.registerForm import *
import io
from io import BytesIO

routes = Blueprint('view', __name__)
user = current_user

# Defs
def user_edit():
    user_edit = db.session.query(Papel.pode_editar).join(
        Papel.user).filter(User.id == user.id).all()
    for edit in user_edit:
        if edit:
            user_edit = edit[0]
        break
    return user_edit


def papel_postagem(papel):
    return ', '.join(map(str, papel))


def remetente(userid):
    return papel_postagem(db.session.query(Papel).join(
        Papel.user).filter(User.id == userid).all())


def remetente_nome(userid):
    return papel_postagem(db.session.query(User.nome).filter(User.id == userid).first())


@routes.route('/select', methods=["GET", "POST"])
def select():
    form = SelectForm()
    return render_template('formselect.html', form=form)


@routes.route('/', methods=["GET", "POST"])
@login_required
def inicio():
    role = Postagem.destinatario
    print(role)
    # papeis = db.session.query(Papel).join(Papel.user).filter(User.id == Postagem.user_id).all()
    cargo = request.args.get(User.query.filter_by(id=user.papeis))

    user_arquivados = db.session.query(Arquivadas.user_id).all()
    user_arquivados = [id for id, in user_arquivados]
    print(user_arquivados)
    subquery = db.session.query(Arquivadas.arquivada).all()
    subquery = [id for id, in subquery]
    if user.id in user_arquivados:
        posts = db.session.query(Postagem).join(Postagem.destinatario).join(
            Papel.user).join(Arquivadas).filter(Postagem.id.not_in(subquery)).filter(User.id == user.id).order_by(Postagem.data.desc()).all()

        busca = request.form.get("busca")
        if busca:
            busca = f"%{busca}%"
            search_post = db.session.query(Postagem).join(Postagem.destinatario).join(
                Papel.user).join(Arquivadas).filter(Postagem.id.not_in(subquery)).filter(User.id == user.id).filter(Postagem.titulo.like(
                    busca)).order_by(Postagem.data.desc()).all()
            posts = search_post
        filtro_data = request.form.get("data")
        if filtro_data:
            filtro_data = f"%{filtro_data}%"
            filtro_data = db.session.query(Postagem).join(Postagem.destinatario).join(
                Papel.user).join(Arquivadas).filter(Postagem.id.not_in(subquery)).filter(User.id == user.id).filter(Postagem.data.like(
                    filtro_data)).order_by(Postagem.data.desc()).all()
            posts = filtro_data

    else:
        posts = db.session.query(Postagem).join(Postagem.destinatario).join(
            Papel.user).filter(User.id == user.id).order_by(Postagem.data.desc()).all()

        busca = request.form.get("busca")
        if busca:
            busca = f"%{busca}%"
            search_post = db.session.query(Postagem).join(Postagem.destinatario).join(
                Papel.user).filter(User.id == user.id).filter(Postagem.titulo.like(
                    busca)).order_by(Postagem.data.desc()).all()
            posts = search_post
        filtro_data = request.form.get("data")
        if filtro_data:
            filtro_data = f"%{filtro_data}%"
            filtro_data = db.session.query(Postagem).join(Postagem.destinatario).join(
                Papel.user).filter(User.id == user.id).filter(Postagem.data.like(
                    filtro_data)).order_by(Postagem.data.desc()).all()
            posts = filtro_data

    # print(posts)

    form = SelectForm()
    form.select.choices = [(select.id, select.nome)
                           for select in Papel.query.join(Papel.user).filter(User.id != user.id).all()]

    return render_template("home.html", user=user, posts=posts, cargo=cargo, user_edit=user_edit(), remetente=remetente, form=form, remetente_nome=remetente_nome)


@ routes.route('/editar', methods=['POST', 'GET'])
@ login_required
def edit():
    form = SelectForm()
    form.select.choices = [(select.id, select.nome)
                           for select in Papel.query.join(Papel.user).filter(User.id != user.id).all()]
    papel = db.session.query(Papel.nome).all()
    print(papel)
    user_papel = papel_postagem(user.papeis)
    print(form.select.data)
    # destinatarios = db.session.query.filter(Papel.nome.in_((form.select.data))).all()
    # print(user_edit())
    if not user_edit():
        return redirect(url_for('view.inicio'))
    posts = db.session.query(Postagem).filter(
        Postagem.user_id == user.id).order_by(Postagem.data.desc()).all()
    if request.method == 'POST':
        file = request.files['imagem']
        db.session.commit()
        filename = secure_filename(file.filename)
        mimetype = file.mimetype
        titulo = request.form.get('titulo')
        texto = request.form.get('texto')
        destinatarios = db.session.query(Papel).filter(
            Papel.id.in_(form.select.data)).all()
        if user_edit():
            informativo = Postagem(
                titulo=titulo, texto=texto, user_id=user.id, destinatario=destinatarios, data_file=file.read(), name=filename, mimetype=mimetype)
            db.session.add(informativo)
            db.session.commit()
            return redirect(url_for('view.edit'))
    return render_template('editar.html', posts=posts, user=user, user_papel=user_papel, papel=papel, user_edit=user_edit(), form=form)

# Donwload Arquivo
@routes.route('/baixar/<int:id>', methods=['GET'])
@ login_required
def baixar(id):
    posts = Postagem().query.filter_by(id=id).first()
    return send_file(BytesIO(posts.data_file), mimetype=posts.mimetype, download_name=posts.name, attachment_filename=posts.titulo)
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


@ routes.route('/arquivar-post', methods=['POST'])
@ login_required
def arquivar_post():
    post = json.loads(request.data)
    postId = post['postId']
    # Arquivadas.arquivada = PostId arquivadas
    arquivos = db.session.query(Arquivadas.arquivada).filter(
        Arquivadas.user_id == user.id).all()
    print(postId)
    if postId not in arquivos:
        arquivar = Arquivadas(arquivada=postId, user_id=user.id)
        db.session.add(arquivar)
        db.session.commit()
    return jsonify({})


@ routes.route('/arquivos', methods=['POST', 'GET'])
@ login_required
def archive():
    posts = db.session.query(Postagem).join(Postagem.destinatario).join(
        Papel.user).join(Arquivadas).filter(User.id == user.id).filter(Postagem.id == Arquivadas.arquivada).order_by(Postagem.data.desc()).all()

    busca = request.form.get("busca")
    if busca:
        busca = f"%{busca}%"
        search_post = db.session.query(Postagem).join(Postagem.destinatario).join(
            Papel.user).join(Arquivadas).filter(User.id == user.id).filter(Postagem.id == Arquivadas.arquivada).filter(Postagem.titulo.like(
                busca)).order_by(Postagem.data.desc()).all()
        posts = search_post
    filtro_data = request.form.get("data")
    if filtro_data:
        filtro_data = f"%{filtro_data}%"
        filtro_data = db.session.query(Postagem).join(Postagem.destinatario).join(
            Papel.user).join(Arquivadas).filter(User.id == user.id).filter(Postagem.id == Arquivadas.arquivada).filter(Postagem.data.like(
                filtro_data)).order_by(Postagem.data.desc()).all()
        posts = filtro_data
    return render_template('arquivos.html', user=user, posts=posts, user_edit=user_edit(), remetente=remetente, remetente_nome=remetente_nome)


@ routes.route('/config')
@ login_required
def config():
    return render_template('config.html', user=user, user_edit=user_edit())
