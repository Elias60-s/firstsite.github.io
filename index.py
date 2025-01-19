import json
from flask import Flask, request, jsonify

app = Flask(__name__)

# Load student data from JSON file
with open("students.json") as f:
    students_data = json.load(f)

@app.route("/api", methods=["GET"])
def get_student_marks():
    names = request.args.getlist("name")  # Get all "name" parameters from the query
    response = {name: students_data.get(name, "Not found") for name in names}
    return jsonify(response)
