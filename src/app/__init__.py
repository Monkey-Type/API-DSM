from flask import Flask
from flask_security.core import Security
from flask_sqlalchemy import SQLAlchemy
from flask_security import UserMixin, RoleMixin
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
#from flask_security import SQLAlchemyUserDatastore
#from flask_security import Security

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database/fatec.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'Secreto'
app.config['SECURITY_PASSWORD_SALT'] = 'muito seguro'
app.config['SECURITY_PASSWORD_HASH'] = 'pbkdf2_sha512'
db = SQLAlchemy(app)
#Flask Admin Config
from .database.models import *
admin = Admin(app, name='FATEC SJC')
admin.add_view(ModelView(Postagem, db.session))
admin.add_view(ModelView(Aluno, db.session))
admin.add_view(ModelView(Turma, db.session))
admin.add_view(ModelView(Curso, db.session))
admin.add_view(ModelView(Professor, db.session))
admin.add_view(ModelView(Materia, db.session))
admin.add_view(ModelView(Coordenador, db.session))
admin.add_view(ModelView(Funcionario, db.session))

from .routes import routes as main_blueprint
app.register_blueprint(main_blueprint)