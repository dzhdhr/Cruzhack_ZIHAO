import fireo
from flask import Blueprint, request

from api.application_service import add_application, delete_application
from api.model.application import Application
from api.model.hacker import Hacker
from api.model.volunteer import Volunteer

applicants_controller = Blueprint('applicant', __name__)


@applicants_controller.route("", methods=['POST'])
def insert_applicants():
    data = request.json
    if data.get("email") is None:
        return {"ErrorMessage": "no Email find"}, 400
    try:
        add_application(data)
    except ValueError:
        return {"ErrorMessage": "duplicated Email"}, 400
    except Exception:
        return {"ErrorMessage": "Bad Request"}, 400
    return 'success', 201


@applicants_controller.route("", methods=['GET'])
def get_applicant_by_email():
    email = request.args.get('email')

    result = Application.collection.filter("email", "==", email).get()
    if result is None:
        return {'errorMessage': "Not Found"}, 404
    return result.to_json(), 200


@applicants_controller.route("/<string:application_id>", methods=['GET'])
def get_applicant_by_id(application_id):
    result = Application.collection.get("application/" + application_id)
    if result is None:
        return {'errorMessage': "Not Found"}, 404
    return result.to_json(), 200


@applicants_controller.route("/<string:application_id>", methods=['DELETE'])
def delete_applicant_by_id(application_id):
    result = Application.collection.get("application/" + application_id)
    if result is None:
        return {'errorMessage': "Not Found"}, 404
    delete_application(result)
    return {"Stats": "Success"}, 201


@applicants_controller.route("", methods=['DELETE'])
def delete_applicant_by_email():
    email = request.args.get('email')

    result = Application.collection.filter("email", "==", email).get()
    if result is None:
        return {'errorMessage': "Not Found"}, 404
    delete_application(result)
    return {"Stats": "Success"}, 201
