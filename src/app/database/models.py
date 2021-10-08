from sqlalchemy.orm import backref
from app import db
from datetime import datetime

administra = db.Table('adiministra',
                      db.Column('funcionario_id', db.Integer,
                                db.ForeignKey('funcionario.id')),
                      db.Column('coordenador_id', db.Integer,
                                db.ForeignKey('coordenador.id'))
                      )

obtem = db.Table('obtem',
                 db.Column('postagem_id', db.Integer,
                           db.ForeignKey('postagem.id')),
                 db.Column('curso_id', db.Integer,
                           db.ForeignKey('curso.id'))
                 )

controla = db.Table('controla',
                    db.Column('funcionario_id', db.Integer,
                              db.ForeignKey('funcionario.id')),
                    db.Column('aluno_id', db.Integer,
                              db.ForeignKey('aluno.id'))
                    )

recebe = db.Table('recebe',
                  db.Column('postagem_id', db.Integer,
                            db.ForeignKey('postagem.id')),
                  db.Column('turma_id', db.Integer, db.ForeignKey('turma.id'))
                  )

remete = db.Table('remete',
                  db.Column('funcionario_id', db.Integer,
                            db.ForeignKey('funcionario.id')),
                  db.Column('postagem_id', db.Integer,
                            db.ForeignKey('postagem.id'))
                  )

gesta = db.Table('gesta',
                 db.Column('funcionario_id', db.Integer,
                           db.ForeignKey('funcionario.id')),
                 db.Column('professor_id', db.Integer,
                           db.ForeignKey('professor.id'))
                 )

gerencia = db.Table('gerencia',
                    db.Column('professor_id', db.Integer,
                              db.ForeignKey('professor.id')),
                    db.Column('turma_id', db.Integer,
                              db.ForeignKey('turma.id'))
                    )


class Postagem(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    assunto = db.Column(db.String, nullable=False)
    remetente = db.Column(db.String)
    data = db.Column(db.DateTime, default=datetime.now)
    texto = db.Column(db.String, nullable=False)
    recebido = db.Column(db.String, nullable=False)

    # Professor
    # id_professor = db.Column(db.Integer, db.ForeignKey('professor.id'))  # Adicionar o nullable=False dps
    # Coordenador
    # id_coordenador = db.Column(db.Integer, db.ForeignKey('coordenador.id'))  # Adicionar o nullable=False dps
    # obtem
    obtems = db.relationship(
        'Curso', secondary=obtem, backref=db.backref('obtem', lazy='dynamic'))
    recebes = db.relationship(
        'Turma', secondary=recebe, backref=db.backref('recebe', lazy='dynamic'))


class Turma(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    # Curso
    id_curso = db.Column(db.Integer, db.ForeignKey('curso.id'), nullable=False)
    # Aluno
    aluno = db.relationship('Aluno', backref='turma')


class Curso(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(100), nullable=False)

    # Turma
    turma = db.relationship('Turma', backref='curso')
    # Aluno
    aluno = db.relationship('Aluno', backref='curso')
    # Curso
    coordenador = db.relationship('Coordenador', backref='cursos')


class Aluno(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(100), nullable=False)
    cpf = db.Column(db.String(11), nullable=False)
    ra = db.Column(db.Integer, nullable=False)
    nome = db.Column(db.String(100), nullable=False)
    senha = db.Column(db.String(100), nullable=False)
    ciclo = db.Column(db.Integer, nullable=False)

    # Curso
    id_curso = db.Column(db.Integer, db.ForeignKey('curso.id'), nullable=False)
    # Turma
    id_turma = db.Column(db.Integer, db.ForeignKey('turma.id'), nullable=False)


class Professor(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(100), nullable=False)
    cpf = db.Column(db.String(11), nullable=False)
    nome = db.Column(db.String(100), nullable=False)
    senha = db.Column(db.String(100), nullable=False)

    # Postagem
    #postagem=db.relationship('Postagem', backref='professor')
    # Funcionario
    id_funcionario = db.Column(db.Integer, db.ForeignKey(
        'funcionario.id'), nullable=False)
    # Materia
    materia = db.relationship('Materia', backref='professor')
    # gerencia
    gerencias = db.relationship(
        'Turma', secondary=gerencia, backref=db.backref('gerencia', lazy='dynamic'))


class Materia(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(100), nullable=False)

    # Professor
    id_professor = db.Column(db.Integer, db.ForeignKey(
        'professor.id'), nullable=False)


class Funcionario(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(100), nullable=False)
    cpf = db.Column(db.String(11), nullable=False)
    nome = db.Column(db.String(100), nullable=False)
    senha = db.Column(db.String(100), nullable=False)
    cargo = db.Column(db.String(50), nullable=False)

    # Professor
    professor = db.relationship('Professor', backref='funcionario')
    # administra
    administras = db.relationship(
        'Coordenador', secondary=administra, backref=db.backref('administra', lazy='dynamic'))
    # controla
    controlas = db.relationship(
        'Aluno', secondary=controla, backref=db.backref('controla', lazy='dynamic'))
    # remete
    remetes = db.relationship(
        'Postagem', secondary=remete, backref=db.backref('remete', lazy='dynamic'))
    # gesta
    gestas = db.relationship(
        'Professor', secondary=gesta, backref=db.backref('gesta', lazy='dynamic'))


class Coordenador(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(100), nullable=False)
    cpf = db.Column(db.String(11), nullable=False)
    nome = db.Column(db.String(100), nullable=False)
    senha = db.Column(db.String(100), nullable=False)

    # Curso
    id_curso = db.Column(db.Integer, db.ForeignKey('curso.id'), nullable=False)
    # Postagem
    #postagem=db.relationship('Postagem', backref='coordenador')


db.create_all()
