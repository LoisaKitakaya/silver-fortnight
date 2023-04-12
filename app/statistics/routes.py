from app.statistics import bp
from flask import request


@bp.route("/statistics/")  # type: ignore
def statistics():
    return "This is the statistics blueprint"
