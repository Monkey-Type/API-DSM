from sqlalchemy.orm import backref, defaultload
from app import db
from datetime import datetime
from flask_login import UserMixin


class Postagem(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    assunto = db.Column(db.String, nullable=False)
    data = db.Column(db.DateTime, default=datetime.now)
    texto = db.Column(db.String, nullable=False)
    recebido = db.Column(db.String, nullable=False)
    remetente = db.Column(db.String, nullable=False)

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    cpf = db.Column(db.Integer, nullable=False)
    nome = db.Column(db.String(100), nullable=False)
    senha = db.Column(db.String(100), nullable=False)
    ra = db.Column(db.Integer, nullable=False)
    email = db.Column(db.String, nullable=False)
    envia = db.Column(db.Boolean, default=0)
    cargo = db.Column(db.String(100), nullable=True, default="Aluno")

    postagem = db.relationship('Postagem', backref='user')

    def __init__(self, nome, email, cpf, ra, senha):
        self.nome = nome
        self.ra = ra
        self.cpf = cpf
        self.email = email
        self.senha = senha


db.create_all()
