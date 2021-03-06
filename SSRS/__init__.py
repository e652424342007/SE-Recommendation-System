from flask import Flask, render_template, g, request, Response, jsonify, redirect, url_for

from SSRS.model import db


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.cfg')

    db.init_app(app)

    from .referee import send_reminding_mail

    @app.route('/')
    def index():
        return redirect(url_for('auth.login'))

    from . import auth
    app.register_blueprint(auth.bp)

    from . import referrer
    app.register_blueprint(referrer.bp)

    from . import referee
    app.register_blueprint(referee.bp)

    print(app.url_map)

    return app
