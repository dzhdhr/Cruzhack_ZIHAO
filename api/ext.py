import firebase_admin
import fireo
from firebase_admin import credentials, storage

# cred = credentials.Certificate('./cruzhack-6a851-firebase-adminsdk-y0k9t-837fb3ef13.json')
# firebase_admin.initialize_app(cred)


def init_ext(app):
    pass
    fireo.connection(from_file='./cruzhack-6a851-firebase-adminsdk-y0k9t-837fb3ef13.json')
