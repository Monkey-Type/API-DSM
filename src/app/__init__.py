from flask import Flask
#Flask Security
from flask_security.core import Security
from flask_security import SQLAlchemyUserDatastore, Security
#Flask SQLALCHEMY
from flask_sqlalchemy import SQLAlchemy
#Flask Login
from flask_login import LoginManager
#Flask Formularios (WTForms)
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Length, ValidationError
#Flask Admin
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
#Flask Bcrypt
from flask_bcrypt import Bcrypt
#App config
app = Flask(__name__)
#App config SQLALCHEMY
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database/fatec.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#App config Chaves de Segurança
app.config['SECRET_KEY'] = 'Secreto'
app.config['SECURITY_PASSWORD_SALT'] = 'muito seguro'
app.config['SECURITY_PASSWORD_HASH'] = 'pbkdf2_sha512'
#Banco de Dados Config
db = SQLAlchemy(app)
#App Bcrypt
bcrypt = Bcrypt(app)
# Flask Admin Config
from .database.models import *
admin = Admin(app, name='FATEC SJC')
admin.add_view(ModelView(Postagem, db.session))
admin.add_view(ModelView(User, db.session))
#Login Maneger
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "auth.login"
#Importação de Rotas atraves da BluePrint
<<<<<<< HEAD
from .views import routes as main_blueprint
app.register_blueprint(main_blueprint)
=======
from .auth import routes as auth_blueprint
app.register_blueprint(auth_blueprint)
from .view import routes as view_blueprint
app.register_blueprint(view_blueprint)
>>>>>>> 76f28d9bbdba9f48b6085bbca029318b47735d5f
