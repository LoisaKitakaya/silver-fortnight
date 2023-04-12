from app.trigonometry import bp


@bp.route("/trigonometry/")  # type: ignore
def trigonometry():
    return "This is the trigonometry blueprint"
