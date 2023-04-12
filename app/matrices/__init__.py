from flask import Blueprint

bp = Blueprint("matrices", __name__)

from app.matrices import routes
