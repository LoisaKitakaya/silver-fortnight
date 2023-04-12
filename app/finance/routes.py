from app.finance import bp
from flask import request


@bp.route("/finance/")  # type: ignore
def finance():
    return "This is the finance blueprint"
