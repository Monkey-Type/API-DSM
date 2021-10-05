from flask import Blueprint, render_template

routes = Blueprint('routes', __name__)


@routes.route('/')
def main():
    return render_template('home.html')

@routes.route('/config')
def config():
    return render_template('config.html')
