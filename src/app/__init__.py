import os
from flask_mail import Mail
from flask import Flask
# Flask SQLALCHEMY
from flask_sqlalchemy import SQLAlchemy
# Flask Login
from flask_login import LoginManager
# Flask Admin
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_bcrypt import Bcrypt
# Flask Migrate
# Comandos para usar o Migrade
# "flask db migrate" - Fazer a Alteração
# "flask db upgrade" - Fazer a Alteração dentro do banco de dados
# "flask db stamp head" - Voltar a origem
from flask_migrate import Migrate
# Path
from os import path

# Banco de dados config
db = SQLAlchemy()
DB_NAME = "fatec.db"

# Migrate
migrate = Migrate()
# Bcrypt
bcrypt = Bcrypt()

# App config

# Mail
mail = Mail()


def create_app():
    app = Flask(__name__)

    # App config Chaves de Segurança
    app.config['SECRET_KEY'] = 'Secreto'
    app.config['SECURITY_PASSWORD_SALT'] = 'muito seguro'
    app.config['SECURITY_PASSWORD_HASH'] = 'pbkdf2_sha512'

    # App config SQLALCHEMY
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///database/{DB_NAME}'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#
    # Uso de Variável de Ambiente para esconder o Email e a Senha para quando subir esse código no GITHUB
    app.config['MAIL_USERNAME'] = os.environ.get('SERVER_EMAIL')
    app.config['MAIL_PASSWORD'] = os.environ.get('SERVER_PASS')

    # Configuração para email gmail
    app.config['MAIL_SERVER'] = 'smtp.gmail.com'
    app.config['MAIL_PORT'] = 587
    app.config['MAIL_USE_TLS'] = True  # Para segurança
    # Para segurança, varia entre esse e o TLS
    app.config['MAIL_USE_SSL'] = False
    #app.config['MAIL_DEBUG'] = True
    app.config['MAIL_DEFAULT_SENDER'] = (
        'Monkey Type', 'contato.monkey.type@gm-ail.com')
    app.config['MAIL_MAX_EMAILS'] = None
    #app.config['MAIL_SUPPRESS_SEND'] = False
    app.config['MAIL_ASCII_ATTACHMENTS'] = False
#

    # Init
    db.init_app(app)
    bcrypt.init_app(app)
    migrate.init_app(app, db)
    mail.init_app(app)  # init para mail

    # Importação de Rotas atraves da BluePrint
    from .auth import routes as auth_blueprint
    from .view import routes as view_blueprint

    app.register_blueprint(auth_blueprint)
    app.register_blueprint(view_blueprint)

    # Flask Admin Config
    from .database.models import Postagem, User, Papel
    admin = Admin(app, name='FATEC SJC')
    admin.add_view(ModelView(Postagem, db.session))
    admin.add_view(ModelView(Papel, db.session))
    admin.add_view(ModelView(User, db.session))

    # Login Maneger
    login_manager = LoginManager()
    login_manager.login_view = "auth.login"
    login_manager.login_message = 'Você deve logar-se para acessar essa página'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    return app


def create_database(app):
    if not path.exists('app/database/' + DB_NAME):
        db.create_all(app=app)
        print('Created Database!')
