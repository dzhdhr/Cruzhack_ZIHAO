from fireo.fields import NumberField, TextField
from fireo.models import Model


class Hacker(Model):
    graduation = NumberField(range(1900, 2100))
    school = TextField()
    reason = TextField(max_length=500)
