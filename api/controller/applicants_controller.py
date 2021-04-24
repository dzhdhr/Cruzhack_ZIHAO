from flask import Blueprint, request

from api.application_service import add_application, delete_application, update_application
from api.model.application import Application

applicants_controller = Blueprint('applicant', __name__)


@applicants_controller.route("", methods=['POST'])
def insert_applicants():
    """
            Create an applicant document
            ---
            tags:
              -Create_applicant_by_id
            description:
               Create an applicant document
            parameters:
              - name: body
                in: body
                required: true
                schema:
                  id: create application
                  required:
                    - application_type
                    - email
                  properties:
                    email:
                        type: string
                        description: email
                    application_type:
                      type: integer
                      description: type for application 0 or hacker 1 for volunteer
                    first_name:
                      type: string
                      description: first name.
                    last_name:
                      type: string
                      description: last name.
                    Age:
                      type: integer
                      description: 18-200.
                    gender:
                      type: integer
                      description: index in ['female', 'male', 'trans', 'non-binary', 'other'].
                    graduation:
                      type: integer
                      description: 1900 to 2100. (hacker only)
                    is_ucsc:
                        type: integer
                        description: 1 for ucsc 0 for not ucsc
                    school:
                      type: string
                      description: school (hacker only with 0 for is_ucsc)
                    reason:
                      type: string
                      description: reason to apply
                    company:
                      type: string
                      description: school (volunteer only)
            responses:
              201:
                  description: create success
                  example: success
              400:
                description: duplicate email or incomplete information
            """
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
    """
        Get an applicant document by email
        ---
        tags:
          -get_applicant_by_email
        description:
           Get an applicant document by email
        parameters:
            - name: id
              in: query
              type: string
              required: true
              description: email of applicant
        responses:
          200:
              description: get success
          404:
            description: Application not find.
    """
    email = request.args.get('email')

    result = Application.collection.filter("email", "==", email).get()
    if result is None:
        return {'errorMessage': "Not Found"}, 404
    return result.to_json(), 200


@applicants_controller.route("/<string:application_id>", methods=['GET'])
def get_applicant_by_id(application_id):
    """
        Get an applicant document by id
        ---
        tags:
          -get_applicant_by_id
        description:
           Get an applicant document by id
        parameters:
            - name: id
              in: path
              type: string
              required: true
              description: id of applicant
        responses:
          200:
              description: get success
          404:
            description: Application not find.
    """
    result = Application.collection.get("application/" + application_id)
    if result is None:
        return {'errorMessage': "Not Found"}, 404
    return result.to_json(), 200


@applicants_controller.route("/<string:application_id>", methods=['DELETE'])
def delete_applicant_by_id(application_id):
    """
        Delete an applicant document by id
        ---
        tags:
          -Delete_applicant_by_id
        description:
           Delete an applicant document by email
        parameters:
            - name: id
              in: path
              type: string
              required: true
              description: id of applicant
        responses:
          201:
              description: delete success
              example: {"Message": "success"}
          404:
            description: Application not find.
    """
    result = Application.collection.get("application/" + application_id)
    if result is None:
        return {'errorMessage': "Not Found"}, 404
    delete_application(result)
    return {"Stats": "Success"}, 201


@applicants_controller.route("", methods=['DELETE'])
def delete_applicant_by_email():
    """
        Delete an applicant document by email
        ---
        tags:
          -Delete_applicant_by_email
        description:
           Delete an applicant document by email
        parameters:
            - name: email
              in: query
              type: string
              required: true
              description: email of applicant
        responses:
          201:
              description: delete success
              example: {"Message": "success"}
          404:
            description: Application not find.
    """
    email = request.args.get('email')

    result = Application.collection.filter("email", "==", email).get()
    if result is None:
        return {'errorMessage': "Not Found"}, 404
    delete_application(result)
    return {"Stats": "Success"}, 201


@applicants_controller.route("", methods=['PUT'])
def update_applicant_by_id():
    """
        Update an applicant document
        ---
        tags:
          -update_applicant_by_id
        description:
           Update an applicant document
        parameters:
          - name: body
            in: body
            required: true
            schema:
              id: 用户注册
              required:
                - application_id
              properties:
                application_id:
                  type: string
                  description: id for application
                first_name:
                  type: string
                  description: first name.
                last_name:
                  type: string
                  description: last name.
                Age:
                  type: int
                  description: 18-200.
                gender:
                  type: int
                  description: index in ['female', 'male', 'trans', 'non-binary', 'other'].
                graduation:
                  type: int
                  description: 1900 to 2100. (hacker only)
                school:
                  type: string
                  description: school (hacker only)
                reason:
                  type: string
                  description: school (hacker only)
                company:
                  type: string
                  description: school (volunteer only)
        responses:
          201:
              description: update success
              example: {"Message": "success"}
          404:
            description: Application not find.

        """
    data = request.json
    application_id = data.get("application_id")
    old_data = Application.collection.get("application/" + application_id)
    print(old_data)
    if old_data is None:
        return {'errorMessage': "Not Found"}, 404
    else:
        data.pop('email', True)
        data.pop('application_type', True)
        update_application(old_data, data)
        return {"Message": "success"}, 201
