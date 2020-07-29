from flask import Blueprint

apis_blueprint = Blueprint("apis", __name__)


@apis_blueprint.route("/ping/")
def ping():
    return "pong", 200, {}


@apis_blueprint.route("/query/")
def query():
    pass


def delete():
    pass


def register_apis_blueprint(flask_application):
    flask_application.register_blueprint(apis_blueprint)
