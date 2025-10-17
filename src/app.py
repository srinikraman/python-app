# Importing flask module in the project is mandatory
# An object of Flask class is our WSGI application.
from flask import Flask, jsonify
import socket
from datetime import datetime

# Flask constructor takes the name of 
# current module (__name__) as argument.
app = Flask(__name__)

# The route() function of the Flask class is a decorator, 
# which tells the application which URL should call 
# the associated function.
@app.route('/api/v1/systeminfo/')
def sys_info():
    return jsonify(
        {'hostname': socket.gethostname(),
         'ip': socket.gethostbyname(socket.gethostname()),
         'port': 5000,
         'additional_info': 'This is the information endpoint',
         'version': '1.0.0'
        })

@app.route('/api/v1/health/')
def health():
    return jsonify({
         'hostname': socket.gethostname(),
         'status': 'running',
         'additional_info': 'This is health check endpoint',
         'version': '1.0.0',
         'date': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
         'desc': 'health api service!!! - cd self-hosted test-5'
        })


# main driver function
if __name__ == '__main__':

    # run() method of Flask class runs the application 
    # on the local development server.
    app.run(host="0.0.0.0")