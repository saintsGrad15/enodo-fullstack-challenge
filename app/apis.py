import json

from flask import Blueprint
from app.db import (get_properties_by_address_or_description_fragment,
                    get_selected_properties,
                    set_property_selected_true)

apis_blueprint = Blueprint("apis", __name__)


@apis_blueprint.route("/ping/")
def ping():
    return "pong", 200, {}


@apis_blueprint.route("/search/<string>")
def search(string):
    return json.dumps(get_properties_by_address_or_description_fragment(string))


@apis_blueprint.route("/selected/")
def selected():
    return json.dumps(get_selected_properties())


@apis_blueprint.route("/select_property/<int:index>")
def select_property(index):
    set_property_selected_true(index)

    return ""


def register_apis_blueprint(flask_application):
    flask_application.register_blueprint(apis_blueprint)
