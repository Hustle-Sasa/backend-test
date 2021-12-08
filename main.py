
from flask import Flask
from flask_migrate import Migrate
from flask_restx import Api
from api import api_blueprint
from api.models.database import db


api = Api(api_blueprint, security='Bearer Auth', doc='/documentation/')


def create_app(config):
    app = Flask(__name__)
    app.config.from_object(config)

    # register blueprints
    app.register_blueprint(api_blueprint)

    # bind app to db
    db.init_app(app)

    # import models
    import api.models

    # import views
    import api.views

    # initialize migration scripts
    migrate = Migrate(app, db)




    return app