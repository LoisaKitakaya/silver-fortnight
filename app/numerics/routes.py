from app.numerics import bp
from flask import request


@bp.route("/numerics/")  # type: ignore
def numerics():
    return "This is the numerics blueprint"
