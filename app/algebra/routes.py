from app.algebra import bp


@bp.route("/algebra/")  # type: ignore
def algebra():
    return "This is the algebra blueprint"
