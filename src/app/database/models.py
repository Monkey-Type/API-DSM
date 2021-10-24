from sqlalchemy.orm import backref
from app import db
from datetime import datetime
from flask_login import UserMixin


class Postagem(db.Model):
    __tablename__ = "postagem"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    assunto = db.Column(db.String, nullable=False)
    data = db.Column(db.DateTime, default=datetime.now)
    texto = db.Column(db.String, nullable=False)
    recebido = db.Column(db.String, nullable=False)
    remetente = db.Column(db.String, nullable=False)
    user_id = db.relationship('User', backref='postagem')
    

association_table = db.Table('association',
                             db.Column('user_id', db.Integer, db.ForeignKey('user.id')),
                             db.Column('papel_id', db.Integer, db.ForeignKey('papel.id'))
                             )


class User(db.Model, UserMixin):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    cpf = db.Column(db.Integer, nullable=True, unique=True)
    nome = db.Column(db.String(100), nullable=False)
    senha = db.Column(db.String(100), nullable=False)
    ra = db.Column(db.Integer, nullable=False)
    email = db.Column(db.String, nullable=False)
    envia = db.Column(db.Boolean, default=0)

    postagem = db.Column(db.Integer, db.ForeignKey('postagem.id'))
    papel_fatec = db.relationship('Papel',
                               secondary=association_table,
                               back_populates='pessoa_papel')

    def __init__(self, nome, email, cpf, ra, senha):
        self.nome = nome
        self.ra = ra
        self.cpf = cpf
        self.email = email
        self.senha = senha
    def __repr__(self):
        return self.nome


class Papel(db.Model):
    __tablename__ = "papel"
    id = db.Column(db.Integer, primary_key=True)
    papel_nome = db.Column(db.String(70), unique=True)
    pessoa_papel = db.relationship('User',
                               secondary=association_table,
                               back_populates='papel_fatec')

    def __repr__(self):
        return self.papel_nome