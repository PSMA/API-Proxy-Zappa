from flask import Flask, request, current_app
import os
import json
import requests

app = Flask(__name__)

api_key = "apikey" # change me
@app.route("/")      
def index():
    return "Welcome to your Zappa deployment of a proxy for Geoscape APIs"

@app.route("/suggest")
def suggest():
    addressString = request.args.get('addressString')
    url = "https://api.psma.com.au/v1/predictive/address/"
    headers = {'authorization': api_key}
    params = {
        'query' : addressString,
        'maxNumberOfResults': 10,
        'dataset': 'gnaf'
    }
    response = requests.request("GET", url, headers=headers, params=params)
    return response.text
        

@app.route("/getBuilding")
def getBuilding():
    addressId = request.args.get('addressId')
    url = "https://api.psma.com.au/v1/buildings"
    headers = {'authorization': api_key}
    params = {
        'addressId': addressId,
        'include': 'footprint2d,maximumRoofHeight'
    }
    response = requests.request("GET", url, headers=headers, params=params)
    return response.text

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
    