from flasgger import Swagger
from flask import Flask

from api.controller import init_blueprint
from api.ext import init_ext
from api.settings import envs

'''
Create flask app and calling all the initialization function
'''


def create_app():
    app = Flask(__name__)
    app.config.from_object(envs.get('develop'))
    init_ext(app=app)
    init_blueprint(app=app)
    return app
