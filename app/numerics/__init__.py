from flask import Blueprint

bp = Blueprint("numerics", __name__)

from app.numerics import routes
