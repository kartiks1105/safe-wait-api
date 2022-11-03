import json

from flask import Flask, request

from database.postgresql import PostgreSQL


app = Flask(__name__)
psql = PostgreSQL()


@app.route("/getStudentInformation")
def get_student_information():
    param = request.args
    student_id = param.get("studentId")
    password = param.get("password")
    student_info = psql.get_student_information(student_id, password)
    resp = {
        "StudentInformation": student_info.__dict__ if student_info else None
    }
    return json.dumps(resp, indent=4)

@app.route("/getDriverInformation")
def get_driver_information():
    param = request.args
    student_id = param.get("studentId")
    driver_info = psql.get_driver_information(student_id)
    resp = {
        "DriverInformation": driver_info.__dict__ if driver_info else None
    }
    return json.dumps(resp, indent=4)