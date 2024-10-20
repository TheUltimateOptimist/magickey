import flask
from flask_socketio import SocketIO
from flask_cors import CORS

app = flask.Flask(__name__)
CORS(app)
socketio = SocketIO(app, cors_allowed_origins="*")

@app.route('/')
def index():
    return "hello world"

skipped_readings = 0

@socketio.on('message')
def handle_message(message):
    global skipped_readings
    value = float(message)
    if value > 1 or value < -1:
        if skipped_readings > 0:
            print(f"--{skipped_readings}")
        skipped_readings = 0
        print(value)
    else:
        skipped_readings += 1

if  __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5000, ssl_context=('certificate.pem', 'privatekey.pem'))
