from math import sqrt
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
    
    return 1 # This is a place holder fake return.

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)