from flask import Blueprint

bp = Blueprint("arithmetics", __name__)

from app.arithmetics import routes
