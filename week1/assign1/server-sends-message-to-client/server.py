import socketio
import eventlet

sio = socketio.Server()
app = socketio.WSGIApp(sio)

@sio.on('connect')
def connect(sid, environ):
    print(f"Client {sid} connected")

@sio.on('disconnect')
def disconnect(sid):
    print(f"Client {sid} disconnected")

def send_messages():
    count = 1
    while True:
        message = f"Message {count} from server"
        print("Sending:", message)
        sio.emit('message', message)
        count += 1
        eventlet.sleep(1)  # Send a message every 5 seconds

if __name__ == '__main__':
    eventlet.spawn(send_messages)
    eventlet.wsgi.server(eventlet.listen(('127.0.0.1', 5000)), app)

