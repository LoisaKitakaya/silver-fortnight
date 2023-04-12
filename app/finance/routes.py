from app.finance import bp


@bp.route("/finance/")  # type: ignore
def finance():
    return "This is the finance blueprint"
