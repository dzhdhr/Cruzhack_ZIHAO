class Config:
    DEBUG = False
    TESTING = False
    # FIREBASE = "./cruzhack-6a851-firebase-adminsdk-y0k9t-837fb3ef13.json"


class DevelopConfig(Config):
    DEBUG = False
    FIREBASE = "./cruzhack-6a851-firebase-adminsdk-y0k9t-837fb3ef13.json"


envs = {
    'develop': DevelopConfig
}
