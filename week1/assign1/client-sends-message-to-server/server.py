import socketio

sio = socketio.Server()
app = socketio.WSGIApp(sio)

@sio.event
def connect(sid, environ):
    print(f"Client {sid} connected")

@sio.event
def disconnect(sid):
    print(f"Client {sid} disconnected")

@sio.on('message')
def handle_message(sid, data):
    print(f"Received message from {sid}: {data}")
    sio.emit('message', f"Server received: {data}", room=sid)

if __name__ == '__main__':
    import eventlet
    eventlet.wsgi.server(eventlet.listen(('127.0.0.1', 5000)), app)

