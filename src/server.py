# pip install python-socketio && pip install eventlet

import os
import socketio
import eventlet
import http.server
import socketserver
import threading

# Thread for serving static files (html, js)
def serve_static_files():
    PORT = 80
    web_dir = os.path.join(os.path.dirname(__file__), 'static')
    os.chdir(web_dir)
    Handler = http.server.SimpleHTTPRequestHandler
    httpd = socketserver.TCPServer(("", PORT), Handler)
    print("serving at port", PORT)
    httpd.serve_forever()

t1 = threading.Thread(target=serve_static_files)
t1.start() 

# Thread for Socket io server (for Real time communication between client & server)
def serve_socketio():
    sio = socketio.Server(cors_allowed_origins='*') # NOT SECURE!!!! DO NOT USE IN F15i airplanes
    app = socketio.WSGIApp(sio)
    @sio.event
    def connect(sid, environ):
        print('Someone (GUI) logged in ')
    @sio.event
    def number_recv(sid, number):
        print("Number is ", number)
    port = int(os.environ.get('PORT', 3000))
    eventlet.wsgi.server(eventlet.listen(('0.0.0.0', port)), app)

t2 = threading.Thread(target=serve_socketio)
t2.start()

# Run a system command to open google chrome with this
os.system('explorer http://localhost')