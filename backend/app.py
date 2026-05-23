from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')

def home():
    return "Inventory Monitoring API Running"

@app.route('/data')

def data():

    inventory = {
        "level": 76,
        "temperature": 31,
        "status": "Normal"
    }

    return jsonify(inventory)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)