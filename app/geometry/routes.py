from app.geometry import bp
from flask import request


@bp.route("/geometry/")  # type: ignore
def geometry():
    return "This is the geometry blueprint"
