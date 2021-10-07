from fatec import db
from datetime import datetime

class Postagem(db.Model):
    __tablename__ = "Postagem"
    id_postagem = db.Column(db.Integer, primary_key=True)
    assunto = db.Column(db.String, nullable=False)
    remetente = db.Column(db.String, nullable=False)
    data = db.Column(db.DateTime, default=datetime.now)
    texto = db.Column(db.String, nullable=False)
