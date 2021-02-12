import requests
import json
from flask import Flask, render_template, jsonify

app = Flask(__name__)
app.config["DEBUG"] = True

@app.route('/', methods=['GET'])
def index():

        return render_template('index.html')


        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json").json()

        print(json.dumps(response, indent=3, sort_keys=True))

@app.route('/btcprice', methods=['GET'])
def getPrice():

        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json").json()

        return response

app.run()