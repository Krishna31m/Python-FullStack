from flask import Flask, jsonify, request
from flask_cors import CORS
from database import get_record, delete_record_by_id, update_record_id, add, get_record_by_id
import sqlite3

app = Flask(__name__)   
CORS(app)

@app.route('/', methods=['POST'])
def add_data():
    data = request.get_json()
    a = data.get("a", 0)
    b = data.get("b", 0)
    result = a + b
    add(a, b, result)
    return jsonify({f"message": "Data added successfully", "result": result})

@app.route('/list', methods=['GET'])
def get_all_data():
    raw_data = get_record()
    result = {
        str(row[0] ): {"num1": row[1], "num2": row[2], "result": row[3]}
        for row in raw_data
    }
    return jsonify(result)

@app.route('/list/<int:id>')
def get_data_by_id(id):
    data = get_record_by_id(id)
    result = {f"{data[0]}": {"num1": data[1], "num2": data[2], "result": data[3]} }
    return jsonify(result)
    # return (data)

@app.route('/delete/<int:id>', methods=['DELETE'])
def delete_by_id(id):  
    status = delete_record_by_id(id)
    if status:
        return jsonify({"message": "Deleted Successfully"})
    else:
        return jsonify({"message": "Record Not Found"}), 404

@app.route('/update/<int:id>', methods=['PUT'])
def update_record_by_id_route(id):  
    data = request.get_json()
    a = data.get('a')
    b = data.get('b')
    result = int(a) + int(b)
    update_record_id(id, a, b, result)
    return jsonify({"message": "Updated", "result": result})
    
if __name__ == '__main__':
    app.run(debug=True)
