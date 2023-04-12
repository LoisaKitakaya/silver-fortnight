from app.geometry import bp


@bp.route("/geometry/")  # type: ignore
def geometry():
    return "This is the geometry blueprint"
