import os
from flask_mail import Mail
from flask import Flask
# Flask SQLALCHEMY
from flask_sqlalchemy import SQLAlchemy
# Flask Login
from flask_login import LoginManager
# Flask Admin
from flask_admin import Admin
from flask_bcrypt import Bcrypt
# Flask Migrate
# Comandos para usar o Migrade
# "flask db migrate" - Fazer a Alteração
# "flask db upgrade" - Fazer a Alteração dentro do banco de dados
# "flask db stamp head" - Voltar a origem
from flask_migrate import Migrate
# Path
from os import path
import click
from flask.cli import with_appcontext

# Tentei usar database_exists para fazer a função no final do código


# Banco de dados config
db = SQLAlchemy()
DB_NAME = "fatec"  # COLOCAR O NOME DO BD QUE CRIAR NO POSTGRES

# Migrate
migrate = Migrate()
# Bcrypt
bcrypt = Bcrypt()

# App config

# Mail
mail = Mail()


@click.command(name='create_tables')
@with_appcontext
def create_tables():
    db.create_all()
    from app.database.models import insert_papel, insert_curso, insert_user
    insert_papel()
    insert_curso()
    insert_user()


def create_app():
    app = Flask(__name__)
    app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

    # App config Chaves de Segurança
    app.config['SECRET_KEY'] = 'Secreto'
    app.config['SECURITY_PASSWORD_SALT'] = 'muito seguro'
    app.config['SECURITY_PASSWORD_HASH'] = 'pbkdf2_sha512'

    # App config SQLALCHEMY
    # --> string de conexão do postgress, lembrar que 010298 é minha senha, colocar a sua f'sqlite:///database/{DB_NAME}'
    # f'postgresql://postgres:010298@localhost/{DB_NAME}'
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get(
        'DATABASE_URL').replace('postgres://', 'postgresql://')
    # app.config[
    #     'SQLALCHEMY_DATABASE_URI'] = f'postgresql://postgres:010298@localhost/{DB_NAME}'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Uso de Variável de Ambiente para esconder o Email e a Senha para quando subir esse código no GITHUB
    # os.environ.get('SERVER_EMAIL')
    app.config['MAIL_USERNAME'] = 'contato.monkey.type@gmail.com'
    # os.environ.get('SERVER_PASS')
    app.config['MAIL_PASSWORD'] = 'GPPRMMT0006'

    # Configuração para email gmail
    app.config['MAIL_SERVER'] = 'smtp.gmail.com'
    app.config['MAIL_PORT'] = 587
    app.config['MAIL_USE_TLS'] = True  # Para segurança
    # Para segurança, varia entre esse e o TLS
    app.config['MAIL_USE_SSL'] = False
    #app.config['MAIL_DEBUG'] = True
    app.config['MAIL_DEFAULT_SENDER'] = (
        'Monkey Type', 'contato.monkey.type@gmail.com')
    app.config['MAIL_MAX_EMAILS'] = None
    #app.config['MAIL_SUPPRESS_SEND'] = False
    app.config['MAIL_ASCII_ATTACHMENTS'] = False

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
    from .database.models import Postagem, User, Papel, Curso, PapelView, PostagemView, UsuarioView, ModelView, CursoView
    from .database.models import AdminIndexView
    admin = Admin(app, index_view=AdminIndexView(),
                  name='FATEC SJC', template_mode='bootstrap4')
    admin.add_view(PostagemView(Postagem, db.session))
    admin.add_view(PapelView(Papel, db.session))
    admin.add_view(UsuarioView(User, db.session))
    admin.add_view(CursoView(Curso, db.session))

    # Login Maneger
    login_manager = LoginManager()
    login_manager.login_view = "auth.login"
    login_manager.login_message = 'Você deve logar-se para acessar essa página'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    from sqlalchemy import create_engine
    from sqlalchemy_utils.functions import database_exists, create_database

    engine = create_engine(app.config[
        'SQLALCHEMY_DATABASE_URI'])

    with app.app_context():
        if not database_exists(app.config[
                'SQLALCHEMY_DATABASE_URI']):
            create_database(app.config[
                'SQLALCHEMY_DATABASE_URI'])
            db.create_all()
            from app.database.models import insert_papel, insert_curso, insert_user
            insert_papel()
            insert_curso()
            insert_user()

    app.cli.add_command(create_tables)

    return app


# - Executar uma vez para gerar o banco de dados.


# - Tentei criar algo que check se o bd já está criado sem se basear na string de conexão modelo sqlite
# def create_database(app):
#     if not database_exists(app.config['SQLALCHEMY_DATABASE_URI']):
#         db.create_all(app=app)

# def create_database(app):
#     if not path.exists('app/database/' + DB_NAME):
#         db.create_all(app=app)
#         print('Created Database!')
