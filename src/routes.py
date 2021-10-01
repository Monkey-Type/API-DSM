from flask import Blueprint, render_template

routes = Blueprint('routes', __name__)


@routes.route('/')
def main():
    return render_template('base.html')
