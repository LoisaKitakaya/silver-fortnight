from app.calculus import bp
from flask import request


@bp.route("/calculus/")  # type: ignore
def calculus():
    return "This is the calculus blueprint"
