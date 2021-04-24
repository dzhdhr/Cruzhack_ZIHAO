from api.model.application import Application
from api.model.hacker import Hacker
from api.model.volunteer import Volunteer


def add_application(data):
    a = Application(first_name=data.get('first_name'), email=data.get('email'), last_name=data.get('last_name'),
                    gender=data.get('gender'), age=data.get('age'), application_type=data.get('application_type'))
    if a.application_type == 0:
        print(data.get('graduation'))
        hacker = Hacker.from_dict(data)
        if data.get('is_ucsc'):
            hacker.school = "ucsc"
        else:
            hacker.school = data.get("school")
        hacker.save()
        try:
            a.hacker_ref = hacker
            a.save()
        except:
            Hacker.collection.delete(hacker.key)
            raise ValueError("Invalid email")
    else:
        # volunteer_data = data.get('volunteer')
        # print(volunteer_data)
        volunteer = Volunteer.from_dict(data)
        volunteer.save()
        try:
            a.volunteer_ref = volunteer
            a.save()
        except:
            Volunteer.collection.delete(volunteer.key)
            raise ValueError("Invalid email")


def delete_application(target):
    if target.application_type == "Volunteer":
        Volunteer.collection.delete(target.volunteer_ref.key)
    else:
        Hacker.collection.delete(target.hacker_ref.key)
    Application.collection.delete(target.key)


def update_application(old_data, new_data):
    if old_data.application_type == "Volunteer":
        volunteer = Volunteer.from_dict(new_data)
        volunteer.update(old_data.volunteer_ref.key)
    else:
        hacker = Hacker.from_dict(new_data)
        hacker.update(old_data.hacker_ref.key)
    application = Application.from_dict(new_data)
    application.email = None
    application.application_type = None
    application.update(old_data.key)
