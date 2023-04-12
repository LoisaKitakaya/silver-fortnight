from flask import Blueprint

bp = Blueprint("algebra", __name__)

from app.algebra import routes
