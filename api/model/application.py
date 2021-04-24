from fireo.fields import TextField, IDField, NumberField, Field, ReferenceField
from fireo.models import Model

from api.model.hacker import Hacker
from api.model.volunteer import Volunteer


def check_email(feild_val):
    result = Application.collection.filter('email', '==', feild_val).get()
    if result is None:
        return True
    else:
        return False


class Gender(Field):
    genders = ['female', 'male', 'trans', 'non-binary', 'other']

    def db_value(self, val):
        if val is None:
            return None
        return self.genders[val]


class ApplicationType(Field):
    application_types = ['Hacker', 'Volunteer']

    def db_value(self, val):
        if val is None:
            return val
        return self.application_types[val]


class Application(Model):
    application_type = ApplicationType()
    hacker_ref = ReferenceField(Hacker)
    volunteer_ref = ReferenceField(Volunteer)
    first_name = TextField()
    last_name = TextField()
    application_id = IDField()
    email = TextField(required=True, validator=check_email)
    age = NumberField(range=(0, 200), int_only=True)
    gender = Gender()

    def to_json(self):
        if self.application_type == "Volunteer":
            self.volunteer_ref = self.volunteer_ref.to_dict()
        else:
            self.hacker_ref = self.hacker_ref.to_dict()

        return self.to_dict()
