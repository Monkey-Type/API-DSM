from sqlalchemy.orm import backref
from app import db
from datetime import datetime


class Postagem(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    assunto = db.Column(db.String, nullable=False)
    data = db.Column(db.DateTime, default=datetime.now)
    texto = db.Column(db.String, nullable=False)
    recebido = db.Column(db.String, nullable=False)
    remetente = db.Column(db.String, nullable=False)

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    cpf = db.Column(db.Integer, nullable=False)
    nome = db.Column(db.String(100), nullable=False)
    senha = db.Column(db.String(100), nullable=False)
    ra = db.Column(db.Integer, nullable=False)
    cargo = db.Column(db.Boolean)
    area = db.Column(db.String(100), nullable=True)

    postagem = db.relationship('Postagem', backref='user')


db.create_all()
