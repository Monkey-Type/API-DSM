from flask_admin.contrib.sqla.view import ModelView
from sqlalchemy.orm import backref
from app import db
from datetime import datetime
from flask_login import UserMixin

# Relações
# Postagem e Usuario one to many
# Postagem e Papel Many to Many
postagem_papel_tabela = db.Table('postagem_papel',
                                 db.Column('postagem_id', db.Integer,
                                           db.ForeignKey('postagem.id')),
                                 db.Column('papel_id', db.Integer,
                                           db.ForeignKey('papel.id'))
                                 )
# Usuario e Papel Many to Many
user_papel_tabela = db.Table('user_papel',
                             db.Column('user_id', db.Integer,
                                       db.ForeignKey('user.id')),
                             db.Column('papel_id', db.Integer,
                                       db.ForeignKey('papel.id'))
                             )
# Tabelas Criadas


class User(db.Model, UserMixin):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(150), nullable=False)
    cpf = db.Column(db.Integer, unique=True, nullable=False)  # Mudar Depois
    email = db.Column(db.String(150), unique=True, nullable=False)
    senha = db.Column(db.String(150), nullable=False)
    # Chaves Estrangeiras
    postagem = db.relationship('Postagem')
    arquivado = db.relationship('Arquivadas', backref='user')
    papeis = db.relationship('Papel',
                             secondary=user_papel_tabela,
                             back_populates='user')
    confirmado = db.Column(db.Integer, nullable=True, default=0)  # adicionado
    # Funcão para ver o Nome

    def __repr__(self):
        return self.nome


class Postagem(db.Model):
    __tablename__ = "postagem"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    titulo = db.Column(db.String(150), nullable=False)
    texto = db.Column(db.String(150), nullable=False)
    data = db.Column(db.DateTime, default=datetime.now)
    # Chaves Estrangeiras
    postagem_arquivada = db.relationship('Arquivadas')
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    destinatario = db.relationship('Papel',
                                   secondary=postagem_papel_tabela,
                                   back_populates='postagem')
    # Funcão para ver o Nome

    def __repr__(self):
        return self.titulo


class Arquivadas(db.Model):
    __tablename__ = "arquivados"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    arquivada = db.Column(db.Integer, db.ForeignKey('postagem.id'))


class Papel(db.Model):
    __tablename__ = "papel"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(150), unique=True, nullable=False)
    pode_editar = db.Column(db.Boolean, default=0)
    # Alteração de dados e uso do /Admin
    admin = db.Column(db.Boolean, default=0)
    # Chaves Estrangeiras
    postagem = db.relationship('Postagem',
                               secondary=postagem_papel_tabela,
                               back_populates='destinatario')
    user = db.relationship('User',
                           secondary=user_papel_tabela,
                           back_populates='papeis')
    # Funcão para ver o Nome

    def __repr__(self):
        return self.nome


class PapelView(ModelView):
    column_list = ['nome', 'user', 'pode_editar', 'admin']
    form_columns = ['nome', 'user', 'pode_editar', 'admin']


class PostagemView(ModelView):
    column_list = ['titulo', 'texto', 'data', 'destinatario']
    form_columns = ['titulo', 'texto', 'data', 'destinatario']
    can_create = False


class UsuarioView(ModelView):
    column_list = ['nome', 'email', 'papeis']
    form_columns = ['nome', 'email', 'papeis']
    can_create = False
