from app.logic import bp


@bp.route("/logic/")  # type: ignore
def logic():
    return "This is the logic blueprint"
