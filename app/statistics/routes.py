from app.statistics import bp


@bp.route("/statistics/")  # type: ignore
def statistics():
    return "This is the statistics blueprint"
