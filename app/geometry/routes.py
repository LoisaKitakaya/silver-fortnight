from app.geometry import bp
from flask import request, jsonify
from app.geometry.geometry import *


@bp.route("/geometry/")  # type: ignore
def geometry():
    return "This is the geometry blueprint"


@bp.route("/geometry/rectangle_perimeter/", methods=["POST"])  # type: ignore
def get_rectangle_perimeter():
    data_dict = request.get_json()

    length = data_dict["data"]["length"]
    width = data_dict["data"]["width"]

    result = rectangle_perimeter(length, width)

    return jsonify({"result": result})


@bp.route("/geometry/circle_perimeter/", methods=["POST"])  # type: ignore
def get_circle_perimeter():
    data_dict = request.get_json()

    radius = data_dict["data"]["radius"]

    result = circle_perimeter(radius)

    return jsonify({"result": result})


@bp.route("/geometry/triangle_perimeter/", methods=["POST"])  # type: ignore
def get_triangle_perimeter():
    data_dict = request.get_json()

    side_1 = data_dict["data"]["side_1"]
    side_2 = data_dict["data"]["side_2"]
    side_3 = data_dict["data"]["side_3"]

    result = triangle_perimeter(side_1, side_2, side_3)

    return jsonify({"result": result})


@bp.route("/geometry/rectangle_area/", methods=["POST"])  # type: ignore
def get_rectangle_area():
    data_dict = request.get_json()

    length = data_dict["data"]["length"]
    width = data_dict["data"]["width"]

    result = rectangle_area(length, width)

    return jsonify({"result": result})


@bp.route("/geometry/circle_area/", methods=["POST"])  # type: ignore
def get_circle_area():
    data_dict = request.get_json()

    radius = data_dict["data"]["radius"]

    result = circle_area(radius)

    return jsonify({"result": result})


@bp.route("/geometry/triangle_area/", methods=["POST"])  # type: ignore
def get_triangle_area():
    data_dict = request.get_json()

    base = data_dict["data"]["base"]
    height = data_dict["data"]["height"]

    result = triangle_area(base, height)

    return jsonify({"result": result})


@bp.route("/geometry/sphere_area/", methods=["POST"])  # type: ignore
def get_sphere_area():
    data_dict = request.get_json()

    radius = data_dict["data"]["radius"]

    result = sphere_area(radius)

    return jsonify({"result": result})


@bp.route("/geometry/cube_volume/", methods=["POST"])  # type: ignore
def get_cube_volume():
    data_dict = request.get_json()

    side = data_dict["data"]["side"]

    result = cube_volume(side)

    return jsonify({"result": result})


@bp.route("/geometry/cylinder_volume/", methods=["POST"])  # type: ignore
def get_cylinder_volume():
    data_dict = request.get_json()

    radius = data_dict["data"]["radius"]
    height = data_dict["data"]["height"]

    result = cylinder_volume(radius, height)

    return jsonify({"result": result})


@bp.route("/geometry/sphere_volume/", methods=["POST"])  # type: ignore
def get_sphere_volume():
    data_dict = request.get_json()

    radius = data_dict["data"]["radius"]

    result = sphere_volume(radius)

    return jsonify({"result": result})
