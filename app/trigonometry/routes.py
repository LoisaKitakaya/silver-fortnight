from app.trigonometry import bp
from flask import request


@bp.route("/trigonometry/")  # type: ignore
def trigonometry():
    return "This is the trigonometry blueprint"
