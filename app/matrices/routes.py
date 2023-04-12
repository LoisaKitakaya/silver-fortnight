from app.matrices import bp
from flask import request


@bp.route("/matrices/")  # type: ignore
def matrices():
    return "This is the matrices blueprint"
