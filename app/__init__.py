# python modules
import os

# third-party imports
from flask import Flask, request, current_app
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_bootstrap import Bootstrap
from flask_bcrypt import Bcrypt

# import config file
from config import Config

# db variable initialization
db = SQLAlchemy()
migrate = Migrate()
bootstrap = Bootstrap()
login = LoginManager()
login.login_view = 'auth.login'
bcrypt = Bcrypt()


def create_app(config_class=Config):
    # initialize Flask into application
    app = Flask(__name__)
    # get all information from Class Config
    app.config.from_object(config_class)

    # initialize app into variables
    db.init_app(app)
    migrate.init_app(app, db)
    login.init_app(app)
    bootstrap.init_app(app)
    bcrypt.init_app(app)

    from app.main import bp as main_bp
    app.register_blueprint(main_bp)

    from app.auth import bp as auth_bp
    app.register_blueprint(auth_bp, url_prefix='/auth')

    return app
