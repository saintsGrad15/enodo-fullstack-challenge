import json

from flask import Blueprint
from app.db import (get_database_connection,
                    get_properties_by_address_or_description_fragment,
                    get_selected_properties,
                    set_property_selected_true,
                    set_property_selected_false)

apis_blueprint = Blueprint("apis", __name__)


@apis_blueprint.route("/ping/")
def ping():
    return "pong", 200, {}


@apis_blueprint.route("/search/<string>/")
def search(string):
    connection = get_database_connection()

    with connection:
        return json.dumps(get_properties_by_address_or_description_fragment(connection, string))


@apis_blueprint.route("/selected/")
def selected():
    connection = get_database_connection()

    with connection:
        return json.dumps(get_selected_properties(connection))


@apis_blueprint.route("/select_property/<int:index>/", methods=["POST"])
def select_property(index):
    connection = get_database_connection()

    with connection:
        set_property_selected_true(connection, index)

    return ""


@apis_blueprint.route("/deselect_property/<int:index>/", methods=["POST"])
def deselect_property(index):
    connection = get_database_connection()

    with connection:
        set_property_selected_false(connection, index)

    return ""


def register_apis_blueprint(flask_application):
    flask_application.register_blueprint(apis_blueprint)
