from app.matrices import bp


@bp.route("/matrices/")  # type: ignore
def matrices():
    return "This is the matrices blueprint"
