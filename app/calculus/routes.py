from app.calculus import bp


@bp.route("/calculus/")  # type: ignore
def calculus():
    return "This is the calculus blueprint"
