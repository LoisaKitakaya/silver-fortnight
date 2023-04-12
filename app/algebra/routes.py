from app.algebra import bp
from flask import request


@bp.route("/algebra/")  # type: ignore
def algebra():
    return "This is the algebra blueprint"
