from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

import logging

db = SQLAlchemy()
ma = Marshmallow()
logging.basicConfig(filename='logging.log', level='debug')


def create_app():
    """Construct the core application."""
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object('config.Config')
    db.init_app(app)
    ma.init_app(app)

    with app.app_context():
        from . import routes

        # Create tables for our models
        db.create_all()
        app.logger.info("application started")

        return app
