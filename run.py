import logging

from flask import Flask
from app.util import configure_logging
from app.apis import register_apis_blueprint
from app.views import register_views_blueprint
from app.db import create_database

logger = logging.getLogger(__name__)

configure_logging()

flask_application = Flask("enodo", static_folder="app/static")

create_database()

register_views_blueprint(flask_application)
register_apis_blueprint(flask_application)

flask_application.run(port=8080, debug=True)
