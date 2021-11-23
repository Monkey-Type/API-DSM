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
    role = Postagem.destinatario
    print(role)
    # papeis = db.session.query(Papel).join(Papel.user).filter(User.id == Postagem.user_id).all()
    cargo = request.args.get(User.query.filter_by(id=user.papeis))

    user_arquivados = db.session.query(Arquivadas.user_id).all()
    user_arquivados = [id for id, in user_arquivados]
    print(user_arquivados)
    subquery = db.session.query(Arquivadas.arquivada).all()
    subquery = [id for id, in subquery]

    user_curso = db.session.query(
        Curso.nome_curso).join(Curso.user).filter(User.id == user.id).all()
    user_curso = [id for id, in user_curso]

    if user.id in user_arquivados:
        posts = db.session.query(Postagem).join(Postagem.destinatario).join(
            Papel.user).join(Arquivadas).join(
                Postagem.curso).filter(Postagem.id.not_in(subquery)).filter(Curso.nome_curso.in_(user_curso)).filter(User.id == user.id).order_by(Postagem.data.desc()).all()

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
        posts = db.session.query(Postagem).join(
            Postagem.destinatario).join(
            Papel.user).join(
                Postagem.curso).filter(User.id == user.id).filter(Curso.nome_curso.in_(user_curso)).order_by(Postagem.data.desc()).all()

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

    return render_template("home.html", user=user, posts=posts, cargo=cargo, user_edit=user_edit(), remetente=remetente, form=form, remetente_nome=remetente_nome)


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
    papel = db.session.query(Papel.nome).all()
    print(papel)
    user_papel = papel_postagem(user.papeis)
    if not user_edit():
        return redirect(url_for('view.inicio'))
    posts = db.session.query(Postagem).filter(
        Postagem.user_id == user.id).order_by(Postagem.data.desc()).all()
    if request.method == 'POST':
        alo = str(request.files.get("photo"))
        print(request.files.get("photo").filename)
        print(request.files.get("photo"))
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
            # informativo = Postagem(titulo=titulo, texto=texto, user_id=user.id, destinatario=destinatarios, data_file=file.read(), image=filename)
            informativo = Postagem(titulo=titulo, texto=texto, user_id=user.id,
                                   destinatario=destinatarios, image=file_teste, mimetype=mimetype, curso=cursos)
            db.session.add(informativo)
            db.session.commit()
            return redirect(url_for('view.edit'))
    return render_template('editar.html', posts=posts, user=user, user_papel=user_papel, papel=papel, user_edit=user_edit(), form=form)
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
