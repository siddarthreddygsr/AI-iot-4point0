import socketio

sio = socketio.Client()

@sio.on('connect')
def on_connect():
    print("Connected to server")

@sio.on('disconnect')
def on_disconnect():
    print("Disconnected from server")

@sio.on('message')
def handle_message(data):
    print(f"Received from server: {data}")

if __name__ == '__main__':
    sio.connect('http://127.0.0.1:5000')
    
    while True:
        message = input("Enter a message to send to the server (or type 'exit' to quit): ")
        if message.lower() == 'exit':
            break
        sio.emit('message', message)

    sio.disconnect()

