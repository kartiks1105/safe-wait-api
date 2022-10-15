import json

from flask import Flask, request

from database.postgresql import PostgreSQL


app = Flask(__name__)
psql = PostgreSQL()


@app.route("/getStudentInformation")
def hello_world():
    param = request.args
    student_id = param.get("studentId")
    student_info = psql.get_student_information(student_id)
    resp = {
        "StudentInformation": student_info.__dict__ if student_info else None
    }
    return json.dumps(resp, indent=4)