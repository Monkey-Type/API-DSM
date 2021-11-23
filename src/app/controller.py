import os
from .database.models import User, Papel
from flask_login import login_required, current_user
from flask import current_app
from . import db

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
