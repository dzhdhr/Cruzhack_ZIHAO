from flask import Blueprint, jsonify

from api.model.application import Application

hackers_controller = Blueprint('hacker', __name__)


@hackers_controller.route("/listall", methods=['GET'])
def get_all_hacker():
    h = Application.collection.filter("application_type", "==", "Hacker").fetch()
    ret = []
    for hacker in h:
        hacker.hacker_ref = hacker.hacker_ref.to_dict()
        hacker.hacker_ref.pop('key')
        ret_dict = hacker.to_dict()
        ret_dict.pop('volunteer_ref')
        ret_dict.pop('key')
        ret.append(ret_dict)

    return jsonify({"hacker": ret})
