from flask import Flask , jsonify 
import requests

app = Flask(__name__)


students = [
    {"id": 1, "name": "Anwar", "age": 22},
    {"id": 2, "name": "Murad", "age": 23}
]

#all students list dekhar jonno
@app.route('/students', methods =['GET'])
def get_students():
    return jsonify(students)

#1 jon students dekhate  
@app.route("/students/<int:student_id>", methods =['GET'])
def get_student(student_id):
    student = next((s for s in students if s["id"]==student_id),None)
    return jsonify(student) if student else jsonify({"error": "Not found"}),404


#post - new student add korbe
@app.route("/students", methods=['POST'])
def add_student():
    data = request.json
    new_student = {
        'id':len(students) + 1,
        'name': data["name"],
        'age': data['age']
    }

    students.append(new_student)
    return jsonify(new_student), 201

#put - student update korbe
@app.route('/students/<int:student_id>', methods =['PUT'])
def update_student(student_id):
    data = request.json
    student = next((s for s in students if s['id'] == student_id), None)
    if student:
        student['name'] = data.get('name', student['name'])
        student['age'] = data.get('age', student['age'])
        return jsonify(student)
    return jsonify({"error": "Not found"}), 404


# delete - student delete korbe
@app.route('/students/<int:student_id>', methods = ['DELETE'])
def delete_student(student_id):
    global students
    students = [s for s in students if s['id'] != student_id]
    return jsonify({"message": "Deleted"})

if __name__ == '__main__':
    app.run(debug=True)