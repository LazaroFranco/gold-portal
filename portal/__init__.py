import sys
import os

from flask import Flask, render_template, flash, request, Blueprint


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)

    from . import courses
    app.register_blueprint(courses.bp)
    app.add_url_rule('/', endpoint='index')

    app.config.from_mapping(
        SECRET_KEY='dev',
        DB_NAME='portal',
        DB_USER='portal_user',
    )

    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)

    from . import db
    db.init_app(app)

    @app.route('/', methods=('GET', 'POST'))
    def index():
        method = request.method
        return render_template('index.html', method=method)

    return app
