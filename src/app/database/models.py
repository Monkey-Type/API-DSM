from sqlalchemy.orm import backref
from app import db
from datetime import datetime
from flask_login import UserMixin

#Relações
#Postagem e Usuario one to many
#Postagem e Papel Many to Many
postagem_papel_tabela = db.Table('postagem_papel',
                             db.Column('postagem_id', db.Integer, db.ForeignKey('postagem.id')),
                             db.Column('papel_id', db.Integer, db.ForeignKey('papel.id'))
                             )
#Usuario e Papel Many to Many
user_papel_tabela = db.Table('user_papel',
                             db.Column('user_id', db.Integer, db.ForeignKey('user.id')),
                             db.Column('papel_id', db.Integer, db.ForeignKey('papel.id'))
                             )
#Tabelas Criadas
class User(db.Model, UserMixin):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(150), unique=True, nullable=False)
    cpf = db.Column(db.Integer, unique=True, nullable=False) # Mudar Depois
    email = db.Column(db.String(150), unique=True, nullable=False)
    senha = db.Column(db.String(150), unique=True, nullable=False)
    #Chaves Estrangeiras
    postagem = db.relationship('Postagem')
    papeis = db.relationship('Papel',
                               secondary=user_papel_tabela,
                               back_populates='user')
    #Funcão para ver o Nome
    def __repr__(self):
        return self.nome
class Postagem(db.Model):
    __tablename__ = "postagem"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    titulo = db.Column(db.String(150), unique=True, nullable=False)
    texto = db.Column(db.String(150), unique=True, nullable=False)
    #Chaves Estrangeiras
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    papeis = db.relationship('Papel',
                               secondary=postagem_papel_tabela,
                               back_populates='postagem')
    #Funcão para ver o Nome
    def __repr__(self):
        return self.titulo
class Papel(db.Model):
    __tablename__ = "papel"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(150), unique=True, nullable=False)
    pode_editar = db.Column(db.Boolean, default=0)
    admin = db.Column(db.Boolean, default=0) #Alteração de dados e uso do /Admin
    #Chaves Estrangeiras
    postagem = db.relationship('Postagem',
                               secondary=postagem_papel_tabela,
                               back_populates='papeis')
    user = db.relationship('User',
                               secondary=user_papel_tabela,
                               back_populates='papeis')
    #Funcão para ver o Nome
    def __repr__(self):
        return self.nome