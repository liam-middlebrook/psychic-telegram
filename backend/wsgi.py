from memeful import app
from memeful import socketio

if __name__ == '__main__':
    socketio.run(app, host=app.config['IP'], port=app.config['PORT'])
