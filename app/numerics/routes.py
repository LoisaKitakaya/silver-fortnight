from app.numerics import bp


@bp.route("/numerics/")  # type: ignore
def numerics():
    return "This is the numerics blueprint"
