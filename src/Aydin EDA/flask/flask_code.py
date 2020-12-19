from math import sqrt
import pymongo
from pymongo import MongoClient
from flask import Flask, render_template, request, jsonify
app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    return render_template('welcome.html')


@app.route('/detect', methods=['POST'])
def recommend():
    data = request.json
    transaction_id = data['transaction_id']
    result = _predict(transaction_id)
    return jsonify({'result': result})

def _predict(transaction_id):
    client = MongoClient('localhost', 27017)
    db = client['test_database']
    test_collection = db['test_collection']
    myquery = { "sequence_number": transaction_id}
    mydoc = db.test_collection.find(myquery)
    for x in mydoc:
    	x
    return x['fraud_prob'] # This is a place holder fake return.

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
