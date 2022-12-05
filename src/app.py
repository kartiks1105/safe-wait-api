import json

from flask import Flask, request

from database.postgresql import PostgreSQL
from util import Util


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

# @app.route("/getStudentInformation")
# def get_student_information():
#     param = request.args
#     student_id = param.get("studentId")
#     password = param.get("password")
#     student_info = psql.get_student_information(student_id, password)
#     resp = {
#         "StudentInformation": student_info.__dict__ if student_info else None
#     }
#     return json.dumps(resp, indent=4)

# @app.route("/getDriverInformation")
# def get_driver_information():
#     param = request.args
#     student_id = param.get("studentId")
#     password = param.get("password")
#     driver_info = psql.get_driver_information(student_id, password)
#     resp = {
#         "DriverInformation": driver_info.__dict__ if driver_info else None
#     }
#     return json.dumps(resp, indent=4)