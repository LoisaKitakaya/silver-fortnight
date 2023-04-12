from flask import Blueprint

bp = Blueprint("trigonometry", __name__)

from app.trigonometry import routes
