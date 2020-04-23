from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate
from flask_cors import CORS
import logging

db = SQLAlchemy()
ma = Marshmallow()
logging.basicConfig(filename='logging.log', level='DEBUG')


def create_app():
    """Construct the core application."""
    app = Flask(__name__, instance_relative_config=False)
    cors = CORS(app)
    app.config.from_object('config.Config')
    # app.config['JWT_SECRET_KEY'] = 'jwt-transit-project-key'
    db.init_app(app)
    ma.init_app(app)
    migrate = Migrate(app, db)

    with app.app_context():
        from . import routes

        # Create tables for our models
        db.create_all()
        app.logger.info("application started")

        return app
