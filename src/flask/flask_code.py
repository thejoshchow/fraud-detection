#import tools
import pandas as pd
import json
from flask import Flask, request
from joblib import dump, load

app = Flask(__name__)

#BELOW IS THE CODE FOR BASIC LAY-OUT OF THE FLASK APP: HOMEPAGE, LINK TO AN ABOUT_US PAGE, LINK TO OUR DETECTION TOOL 

@app.route('/', methods=['GET'])
def home():
    return ''' <p> Welcome to Very Sophisticated Fraud Detection, Inc. Here is 
                   <a href="/information about our technology">information about our technology</a> and here is our very impressive
                   <a href="/Detection Tool!">Detection Tool!</a> </p> '''
          
@app.route('/information about our technology', methods=['GET'])
def hello_world():
    return ''' <h1> ABOUT US </h1> <p>Very Sophisticated Fraud Detection was developed by Opa Towobola, Mary MacCarthy, Aydin Hadlani, and Joshua Chow who are employees of Galvanize DSI consulting.</p>
<p>Our detection tool uses an innovative combination of machine learning models to quickly predict whether or not a transaction is fraudulent, with an accuracy rate much higher than that of our competitors. </p> 
<p>Companies that have adopted our technology say that it has played a major role in dramatically decreasing their annual losses to fraud.</p>'''

@app.route('/Detection Tool!', methods=['GET'])
def form_display():
    return ''' <form action="/string_reverse" method="POST">
                <input type="text" name="some_string" />
                <input type="submit" />
               </form>
             '''

@app.route('/string_reverse', methods=['POST'])
def reverse_string():
    text = str(request.form['some_string'])
    reversed_string = text[-1::-1]
    return ''' output: {}  '''.format(reversed_string)

            <!DOCTYPE html>
            <html>
            
            <center>
            <body  style = "background-image: <img src = {{ url_for('static', filename='fraud_stockphoto.jpg')}}>
                {0}</body></center>
            </html>
             

# BELOW IS THE CODE WHERE WE WILL PLUG IN OUR PREDICTION MODEL(S)
# NEED TO INSERT MODEL NAME HERE, AS WELL AS FILE NAME (WHERE MODEL CODE IS STORED)

# @app.route('/result', methods=['POST', 'GET'])
# (insert prediction model function here)

# from file_name import model_name
# # load model at startup time
# app.model = joblib.load(model_name)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)