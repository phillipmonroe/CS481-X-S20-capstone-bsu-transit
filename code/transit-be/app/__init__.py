from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
# from flask_jwt_extended import JWTManager

db = SQLAlchemy()
ma = Marshmallow()

def create_app():
    """Construct the core application."""
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object('config.Config')
    # app.config['JWT_SECRET_KEY'] = 'jwt-transit-project-key'
    db.init_app(app)
    ma.init_app(app)
    # jwt = JWTManager(app)

    with app.app_context():
        from . import routes

        # Create tables for our models
        db.create_all()

        return app