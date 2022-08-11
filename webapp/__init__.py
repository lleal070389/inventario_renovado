from flask import Flask

from webapp.models import db

# Se requiere la importación para el uso de referencias
from webapp.models.user import User
from webapp.models.item import Item

from webapp.views.api import api_v1
from webapp.views.customer import customers
from webapp.views.state import states
from webapp.views.people import people
from webapp.views.item import items


app = Flask(__name__)


def create_app(enviroment):
    app.config.from_object(enviroment)

    app.register_blueprint(api_v1)
    app.register_blueprint(customers)
    app.register_blueprint(states)
    app.register_blueprint(people)
    app.register_blueprint(items)

    with app.app_context():
        db.init_app(app)

    return app
