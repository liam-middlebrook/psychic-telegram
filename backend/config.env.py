import os

DEBUG=False
IP=os.environ.get('MEMEFUL_IP', '0.0.0.0')
PORT=os.environ.get('MEMEFUL_PORT', '8080')
SERVER_NAME=os.environ.get('MEMEFUL_SERVER_NAME', 'memeful.csh.rit.edu')
SECRET_KEY=os.environ.get('MEMEFUL_SECRET_KEY', '')
