from api.controller.applicants_controller import applicants_controller
from api.controller.hackers_controller import hackers_controller
from api.controller.volunteers_controller import volunteers_controller


def init_blueprint(app):
    app.register_blueprint(blueprint=applicants_controller,url_prefix='/applicant')
    app.register_blueprint(blueprint=hackers_controller, url_prefix='/hacker')
    app.register_blueprint(blueprint=volunteers_controller, url_prefix='/volunteer')
    pass
