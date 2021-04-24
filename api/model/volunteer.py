from fireo.fields import TextField
from fireo.models import Model


class Volunteer(Model):
    company = TextField()
    reason = TextField(max_length=500)
