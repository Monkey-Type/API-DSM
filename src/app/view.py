from operator import pos
from os import name
from flask import Blueprint, render_template, url_for, request, jsonify, json, request, Response, current_app, send_from_directory
from flask_login import login_required, current_user
import sqlalchemy
from sqlalchemy import *
from .database.models import Arquivadas, Postagem, User, Papel, Curso
from werkzeug.utils import redirect, secure_filename, send_file
from . import db
from .formulario.registerForm import *
import io
import secrets
from io import BytesIO
from .controller import *

routes = Blueprint('view', __name__)
user = current_user


@routes.route('/', methods=["GET", "POST"])
@login_required
def inicio():
    filtro = FiltroForm()
    cargo = request.args.get(User.query.filter_by(id=user.papeis))
    user_arquivados = tupleToList(db.session.query(Arquivadas.user_id).all())

    if user.id in user_arquivados:
        post = postConsulta('inicio')
        posts = post.all()
    else:
        post = postConsulta()
        posts = post.all()

    busca = request.form.get("busca")
    if busca:
        busca = f"%{busca}%"
        search_post = post.filter(Postagem.titulo.like(busca)).all()
        posts = search_post

    filtro_data = request.form.get("data")
    if filtro_data:
        filtro_data = f"%{filtro_data}%"
        filtro_data = post.filter(Postagem.data.like(filtro_data)).all()
        posts = filtro_data

    filtro_papel = filtro.filtro_papel.data
    if filtro_papel:
        filtro_papel = list(map(int, filtro_papel))
        papel_userid = tupleToList(db.session.query(User.id).join(
            Papel.user).filter(Papel.id.in_(filtro_papel)).all())
        filtro_papel = post.filter(Postagem.user_id.in_(papel_userid)).all()
        posts = filtro_papel

    filtro_curso = filtro.filtro_curso.data
    if filtro_curso:
        filtro_curso = list(map(int, filtro_curso))
        print(filtro_curso)
        filtro_curso = post.filter(Curso.id.in_(filtro_curso)).all()
        posts = filtro_curso

    filtro_anexo = request.form.get("anexos")
    if filtro_anexo == '1':
        posts = post.filter(Postagem.image != '').all()
    if filtro_anexo == '2':
        posts = post.filter(Postagem.image == '').all()

    return render_template("home.html", user=user, posts=posts, cargo=cargo, user_edit=user_edit(), remetente=remetente, filtro=filtro, remetente_nome=remetente_nome)


# Baixar Imagens
IMAGEMS = "static/images"


@ routes.route('/editar/<nome_do_arquivo>', methods=['GET'])
def get_arquivo(nome_do_arquivo):
    return send_from_directory(IMAGEMS, nome_do_arquivo, as_attachment=True)


# Edição
@ routes.route('/editar', methods=['POST', 'GET'])
@ login_required
def edit():
    form = SelectForm()
    filtro = FiltroForm()
    papel = db.session.query(Papel.nome).all()
    user_papel = tupleToString(user.papeis)

    if not user_edit():
        return redirect(url_for('view.inicio'))
    posts = db.session.query(Postagem).filter(
        Postagem.user_id == user.id).order_by(Postagem.data.desc()).all()

    if request.method == 'POST':
        if not request.files.get("photo").filename:
            file_teste = ''
        else:
            file_teste = save_photo(request.files.get('photo'))
        file = request.files['photo']
        mimetype = file.mimetype
        titulo = request.form.get('titulo')
        texto = request.form.get('texto')
        destinatarios = db.session.query(Papel).filter(
            Papel.id.in_(form.papel.data)).all()
        cursos = db.session.query(Curso).filter(
            Curso.id.in_(form.curso.data)).all()

        if user_edit():
            informativo = Postagem(titulo=titulo, texto=texto, user_id=user.id,
                                   destinatario=destinatarios, image=file_teste, mimetype=mimetype, curso=cursos)
            db.session.add(informativo)
            db.session.commit()
            return redirect(url_for('view.edit'))
    return render_template('editar.html', posts=posts, user=user, user_papel=user_papel, papel=papel, user_edit=user_edit(), filtro=filtro, form=form)


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
    arquivos = db.session.query(Arquivadas.arquivada).filter(
        Arquivadas.user_id == user.id).all()
    if postId not in arquivos:
        arquivar = Arquivadas(arquivada=postId, user_id=user.id)
        db.session.add(arquivar)
        db.session.commit()
    return jsonify({})


@ routes.route('/arquivos', methods=['POST', 'GET'])
@ login_required
def archive():
    filtro = FiltroForm()
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
    return render_template('arquivos.html', user=user, posts=posts, user_edit=user_edit(), remetente=remetente, remetente_nome=remetente_nome, filtro=filtro)


@ routes.route('/config')
@ login_required
def config():
    filtro = FiltroForm()
    return render_template('config.html', user=user, user_edit=user_edit(), filtro=filtro)
