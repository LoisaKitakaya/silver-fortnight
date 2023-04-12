from app.arithmetics import bp
from flask import request


@bp.route("/arithmetics/")  # type: ignore
def arithmetics():
    return "This is the arithmetics blueprint"
