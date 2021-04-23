class Config:
    DEBUG = False
    TESTING = False


class DevelopConfig(Config):
    DEBUG = False


envs = {
    'develop': DevelopConfig
}
