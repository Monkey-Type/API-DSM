import os
from .database.models import *
from flask_login import login_required, current_user
from flask import current_app, request
from . import db
from .formulario.registerForm import FiltroForm

user = current_user


# Defs


# Função para salvar dentro do Diretorio
def save_photo(photo):
    # rand_hex  = secrets.token_hex(10)
    _, file_extention = os.path.splitext(photo.filename)
    file_name = photo.filename  # rand_hex
    file_path = os.path.join(current_app.root_path, 'static/images', file_name)
    photo.save(file_path)
    return file_name


def user_edit():
    user_edit = tupleToList(db.session.query(Papel.pode_editar).join(
        Papel.user).filter(User.id == user.id).all())
    for edit in user_edit:
        if edit:
            return True
    return False


def tupleToString(tupla):
    return ', '.join(map(str, tupla))


def remetente(userid):
    return tupleToString(db.session.query(Papel).join(
        Papel.user).filter(User.id == userid).filter(Papel.nome != 'Funcionario').all())


def remetente2(userid):
    return db.session.query(Papel.id).join(
        Papel.user).filter(User.id == userid).all()


def remetente_nome(userid):
    return tupleToString(db.session.query(User.nome).filter(User.id == userid).first())


def tupleToList(tupla):
    return [id for id, in tupla]

# filter(Postagem.id.not_in(arquivada))


def postConsulta(rota=None):
    user_curso = tupleToList(db.session.query(
        Curso.nome_curso).join(Curso.user).filter(User.id == user.id).all())
    arquivada = tupleToList(db.session.query(Arquivadas.arquivada).all())
    if user_curso == []:
        if rota == 'inicio':
            posts = db.session.query(Postagem) \
                .join(Postagem.destinatario).join(Papel.user).join(Arquivadas) \
                .filter(Postagem.id.not_in(arquivada)) \
                .filter(User.id == user.id) \
                .order_by(Postagem.data.desc())
        else:
            posts = db.session.query(Postagem) \
                .join(Postagem.destinatario).join(Papel.user) \
                .filter(User.id == user.id) \
                .order_by(Postagem.data.desc())
    else:
        if rota == 'inicio':
            posts = db.session.query(Postagem) \
                .join(Postagem.destinatario).join(Papel.user).join(Arquivadas).join(Postagem.curso) \
                .filter(Postagem.id.not_in(arquivada)) \
                .filter(Curso.nome_curso.in_(user_curso)) \
                .filter(User.id == user.id) \
                .order_by(Postagem.data.desc())
        else:
            posts = db.session.query(Postagem) \
                .join(Postagem.destinatario).join(Papel.user).join(Postagem.curso) \
                .filter(Curso.nome_curso.in_(user_curso)) \
                .filter(User.id == user.id) \
                .order_by(Postagem.data.desc())

    return posts


def filtrarPost(post, filtro_anexo, filtro_curso, filtro_papel, filtro_data):
    # def filtrarPost(post):
    if filtro_data:
        filtro_data = f"%{filtro_data}%"
        post = post.filter(Postagem.data.like(filtro_data))

    # print(filtro_data, filtro_papel,
    #       filtro_curso, filtro_anexo)

    if filtro_papel != None:
        filtro_papel = list(map(int, filtro_papel))
        papel_userid = tupleToList(db.session.query(User.id).join(
            Papel.user).filter(Papel.id.in_(filtro_papel)).all())
        print('oi')
        post = post.filter(Postagem.user_id.in_(papel_userid))

    if filtro_curso:
        filtro_curso = list(map(int, filtro_curso))
        post = post.filter(Curso.id.in_(filtro_curso))

    if filtro_anexo == '1':
        post = post.filter(Postagem.image != '')
    if filtro_anexo == '2':
        post = post.filter(Postagem.image == '')

    return post
