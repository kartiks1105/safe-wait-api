import json

from flask import Flask, request

from database.postgresql import PostgreSQL
from util import Util
import itertools
import requests
import sys


app = Flask(__name__)
psql = PostgreSQL()
util = Util()

@app.route("/getStudentInformation", methods=['POST'])
def getStudentInformation():
    data = request.get_json()
    resp = psql.getStudentInformation(data['student_id'], data['password'])
    return {'studentInformation': resp}

@app.route("/getDriverInformation", methods=['POST'])
def getDriverInformation():
    data = request.get_json()
    resp = psql.getDriverInformation(data['student_id'], data['password'])
    return {'driverInformation': resp}

@app.route("/getPredictions", methods=['POST'])
def getPredictions():
    data = request.get_json()
    resp = util.getPredictions(data['place'])
    return {'predictions': resp}

@app.route("/getDurationBetweenTwoLocations", methods=['POST'])
def getDurationBetweenTwoLocations():
    data = request.get_json()
    seconds = util.durationBetweenTwoLocations(data['origin'], data['destination'])
    return {'seconds': seconds}

@app.route("/getBestRoute", methods=['POST'])
def getBestRoute():
    data = request.get_json()
    addresses = data['addresses']
    addresses = list(itertools.permutations(addresses))
    duration = sys.maxsize

    for address in addresses:
        sequence = list(address)
        sequence.insert(0, "Head Hall, Fredericton")
        sequence.append("Head Hall, Fredericton")

        time = 0

        for i in range(len(sequence)):
            body = {
                "origin": sequence[i - 1],
                "destination": sequence[i]
            }
            resp = requests.post("http://127.0.0.1:5000/getDurationBetweenTwoLocations", json=body)
            resp = resp.json()
            time += resp['seconds']
        
        if time < duration:
            duration = time
            route = sequence
        


    return {
        "duration": duration,
        "route": route
    }