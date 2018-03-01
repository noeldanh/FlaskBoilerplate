# python modules
import os

# third-party imports
from flask import Flask, request, current_app
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_bootstrap import Bootstrap
from flask_bcrypt import Bcrypt
from flask_wtf import CSRFProtect

# import config file
from config import Config

# db variable initialization
db = SQLAlchemy()
# csrf = CSRFProtect()
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
    # csrf.init_app(app)
    migrate.init_app(app, db)
    login.init_app(app)
    bootstrap.init_app(app)
    bcrypt.init_app(app)

    from app.main import bp as main_bp
    app.register_blueprint(main_bp)

    from app.auth import bp as auth_bp
    app.register_blueprint(auth_bp, url_prefix='/auth')

    from app.book import bp as book_bp
    app.register_blueprint(book_bp, url_prefix='/books')

    from app.zapier import bp as zapier_bp
    # api_blueprint = zapier_bp
    # csrf.exempt(api_blueprint)
    app.register_blueprint(zapier_bp)

    return app
