import fireo
from flasgger import Swagger


def init_ext(app):
    fireo.connection(from_file=app.config['FIREBASE'])
    swagger_config = Swagger.DEFAULT_CONFIG
    swagger_config['title'] = "Cruzhack API"
    swagger_config['description'] = "API for CRUZHACK"
    swagger_config['description'] = "http://127.0.0.1:5000/"
    Swagger(app, config=swagger_config)

