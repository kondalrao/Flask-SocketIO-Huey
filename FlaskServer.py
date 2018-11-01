from gevent import monkey; monkey.patch_all()

from flask import request, render_template
from flask_socketio import emit

from config import huey, app, socketio
from tasks import count_beans, ping


# taskdata = {
#     'socketio': socketio,
#     'client_id': None,
#     'data': {},
#     'namespace': '/test',
#     'is_json': True
# }


@app.route('/')
def index():
    return render_template('index.html')


@socketio.on('my_ping', namespace='/test')
def ping_pong():
    print("Received event {}".format('my_ping'))
    emit('my_pong')


@socketio.on('my_pong', namespace='/test')
def ping_pong():
    print("Received event {}".format('my_pong'))


@socketio.on('my_event', namespace='/test')
def test_message(message):
    print("Received event {} message {}".format('my_event', message))
    result = count_beans(request.sid, 100)
    print result.get()


@socketio.on('my_broadcast_event', namespace='/test')
def test_message(message):
    print("Received event {} message {}".format('my_broadcast_event', message))
    emit('my_response', {'data': message['data']}, broadcast=True)


@socketio.on('connect', namespace='/test')
def test_connect():
    emit('my_response', {'data': 'Connected'})


@socketio.on('disconnect', namespace='/test')
def test_disconnect():
    print('Client disconnected')


if __name__ == '__main__':
    huey.start()
    ping()
    socketio.run(app, debug=True)