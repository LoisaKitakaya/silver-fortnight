from flask import Blueprint

bp = Blueprint("logic", __name__)

from app.logic import routes
