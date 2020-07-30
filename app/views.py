from flask import (Blueprint,
                   render_template)

views_blueprint = Blueprint("views", __name__,
                            template_folder="templates",
                            static_folder="static")


@views_blueprint.route("/")
def index(*args, **kwargs):
    return render_template("index.html")


def register_views_blueprint(flask_application):
    flask_application.register_blueprint(views_blueprint)
