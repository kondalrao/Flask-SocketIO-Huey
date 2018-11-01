from huey.contrib.minimal import MiniHuey

from flask import Flask
from flask_socketio import SocketIO

import logging

huey = MiniHuey()

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)
