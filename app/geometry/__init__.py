from flask import Blueprint

bp = Blueprint("geometry", __name__)

from app.geometry import routes
