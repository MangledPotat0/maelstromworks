"-*- coding: utf-8 -*-"

from flask import Flask, send_from_directory
from flask_socketio import SocketIO
from flask_cors import CORS

app = Flask(__name__, static_folder="site")
CORS(app)
socketio = SocketIO(app, cors_allowed_origins="*")

# Serve the main page
@app.route('/')
def serve_index():
    return send_from_directory(app.static_folder, 'index.html')

# Handle static pages
@app.route("/<path:path>")
def serve_file(path):
    return send_from_directory(app.static_folder, path)

# Handle client connection
@socketio.on("connect")
def connect():
    print("Client connected")
    socketio.emit("Connected", {"message": "Welcome"}, to=request.sid)

# Handle client disconnection
@socketio.on("disconnect")
def disconnect():
    print("Client disconnected")
    socketio.emit("Disconnected", {"message": "Goodbye"}, to=request.sid)

if __name__ == "__main__":
    socketio.run(app, debug=True, host="0.0.0.0", port=5000)

# EOF
