import os
from flask import Flask
from endpoint import controllers
from endpoint.controllers import index

def create_app():
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='whatevs',
    )

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    controllers.register_all_blueprints(app)
    return app

app = create_app()