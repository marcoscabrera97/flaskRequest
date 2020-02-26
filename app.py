from flask import Flask, jsonify, request
import models


DEBUG = True
PORT = 8000
HOST = '0.0.0.0'

app = Flask(__name__)

@app.route('/')
def hello():
    response = jsonify({
        'path': 'respuesta'
    })
    return response

@app.route('/registration/broker', methods=['POST'])
def addBroker():
    json = request.json
    try:
        id = models.Broker.registerBroker(json['path'])
    except models.IntegrityError:
        pass
    response = jsonify({
        'id': id,
        'message_response': 'Registro del broker correcto'
    })
    return response


if __name__ == '__main__':
    models.initialize()
    app.run(debug = DEBUG, host = HOST, port = PORT)