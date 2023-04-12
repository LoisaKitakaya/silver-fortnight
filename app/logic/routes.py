from app.logic import bp
from flask import request


@bp.route("/logic/")  # type: ignore
def logic():
    return "This is the logic blueprint"
