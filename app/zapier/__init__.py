from flask import Blueprint

bp = Blueprint('zapier', __name__)

from app.zapier import routes

