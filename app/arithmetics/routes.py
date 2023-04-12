from app.arithmetics import bp
from flask import request, jsonify
from app.arithmetics.arithmetic import *


@bp.route("/arithmetic/")  # type: ignore
def arithmetics():
    return "This is the arithmetics blueprint"


@bp.route("/arithmetic/addition/", methods=["POST"])  # type: ignore
def addition():
    if request.method == "POST":
        data_dict = request.get_json()

        data = tuple(data_dict["data"])

        result = arithmetic_sum(*data)

        return jsonify({"result": result})


@bp.route("/arithmetic/subtraction/", methods=["POST"])  # type: ignore
def subtraction():
    if request.method == "POST":
        data_dict = request.get_json()

        data = tuple(data_dict["data"])

        result = arithmetic_difference(*data)

        return jsonify({"result": result})


@bp.route("/arithmetic/multiplication/", methods=["POST"])  # type: ignore
def multiplication():
    if request.method == "POST":
        data_dict = request.get_json()

        data = tuple(data_dict["data"])

        result = arithmetic_multiplication(*data)

        return jsonify({"result": result})


@bp.route("/arithmetic/division/", methods=["POST"])  # type: ignore
def division():
    if request.method == "POST":
        data_dict = request.get_json()

        data = tuple(data_dict["data"])

        result = arithmetic_division(*data)

        return jsonify({"result": result})


@bp.route("/arithmetic/exponent/", methods=["POST"])  # type: ignore
def exponent():
    if request.method == "POST":
        data_dict = request.get_json()

        data = tuple(data_dict["data"])

        result = arithmetic_exponent(*data)

        return jsonify({"result": result})


@bp.route("/arithmetic/floor/", methods=["POST"])  # type: ignore
def floor():
    if request.method == "POST":
        data_dict = request.get_json()

        data = tuple(data_dict["data"])

        result = arithmetic_floor(*data)

        return jsonify({"result": result})


@bp.route("/arithmetic/modulo/", methods=["POST"])  # type: ignore
def modulo():
    if request.method == "POST":
        data_dict = request.get_json()

        data = tuple(data_dict["data"])

        result = arithmetic_modulo(*data)

        return jsonify({"result": result})
