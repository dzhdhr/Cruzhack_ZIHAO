from flask import Flask
from flask_script import Manager

from api import create_app

app = Flask(__name__)


app = create_app()
manager = Manager(app=app)

# app entry point
if __name__ == '__main__':
    manager.run()

