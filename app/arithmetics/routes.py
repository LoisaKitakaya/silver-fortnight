from app.arithmetics import bp


@bp.route("/arithmetics/")  # type: ignore
def arithmetics():
    return "This is the arithmetics blueprint"
