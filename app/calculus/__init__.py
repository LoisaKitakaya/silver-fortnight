from flask import Blueprint

bp = Blueprint("calculus", __name__)

from app.calculus import routes
