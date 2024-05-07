from flask import Blueprint, jsonify, app, request

bp = Blueprint("api", __name__)

@bp.route("/api/", methods=("GET",))
def index():
    return jsonify({"status": 200, "message": "API da Gabriela da Costa"})


@bp.route("/api/aleatorios", methods=("GET",))
def aleatorios():
    import random
    a = random.randint(49, 100)
    return jsonify({"status": 200, "data": a})

@bp.route("/api/argumentos/<string:nome>", methods=("GET",))
def argumentos(nome: str):
    return jsonify({"status": 200, "data": nome})

@bp.route("/api/argumentos", methods=("GET",))
def arg_implicito():
    return jsonify({"status": 200, "data": request.args["nome"]})

@bp.route("/api/idades", methods=("GET",))
def idades():
    from random_data import pessoas
    import funcoes
    num = funcoes.maior_de_50(pessoas)
    return jsonify({"status": 200, "data": num})

@bp.route("/api/salario", methods=("GET",))
def salario():
    from random_data import pessoas
    import funcoes
    num = funcoes.mais_2000(pessoas)
    return jsonify({"status": 200, "data": num})


