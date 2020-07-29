import logging

from flask import Flask
from app.util import configure_logging
from app.apis import register_apis_blueprint
from app.views import register_views_blueprint

logger = logging.getLogger(__name__)

configure_logging()

flask_application = Flask("some application name")

register_views_blueprint(flask_application)
register_apis_blueprint(flask_application)

flask_application.run(port=8080)
