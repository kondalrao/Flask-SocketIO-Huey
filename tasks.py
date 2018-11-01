from config import huey
from huey import crontab
from gevent import sleep

from config import socketio

@huey.task()
def count_beans(client_id, num):
    print('-- counted %s beans --' % num)
    sleep(5)
    socketio.emit('my_response', {'data': 'beans counted...'}, room=client_id, namespace='/test')
    return 'Counted %s beans' % num

@huey.task(crontab(minute='*/1'))
def ping():
    print("Sending broadcast ping...")
    socketio.emit('my_ping', {'data': 'message'}, namespace='/test', broadcast=True)