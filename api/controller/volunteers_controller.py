from flask import Blueprint, jsonify

from api.model.application import Application

volunteers_controller = Blueprint('volunteer', __name__)


@volunteers_controller.route("/listall", methods=['GET'])
def get_all_volunteer():
    """
        Get all volunteer
        ---
        tags:
          -get_all_volunteer
        description:
           Get all volunteers
        responses:
          200:
              description: get success return json for all volunteer info
          404:
              description: no volunteer
    """

    volunteers = Application.collection.filter("application_type", "==", "Volunteer").fetch()
    ret = []
    for volunteer in volunteers:
        volunteer.volunteer_ref = volunteer.volunteer_ref.to_dict()
        volunteer.volunteer_ref.pop('key')
        ret_dict = volunteer.to_dict()
        ret_dict.pop('hacker_ref')
        ret_dict.pop('key')
        ret.append(ret_dict)
    if len(ret) == 0:
        return {"errorMessage": "not Find"}, 404
    return jsonify({"volunteers": ret})
