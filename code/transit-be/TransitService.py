from flask import Flask, request, Response, jsonify, abort
from flask_mysqldb import MySQL
from flask_cors import CORS
from flask_api import status
from TransitServiceFunctions import *

app = Flask(__name__)

# Change these values to reflect your local database setup
app.config['MYSQL_USER'] = 'admin'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'citygodb'

# Don't change this one
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

mysql = MySQL(app)

CORS(app)

@app.route('/')
def test_service():
    """ 
    Test service is running correctly. This route exposes an endpoint that returns a service is running prompt.
    """
    return "Transit backend service is running."

# GET   - returns all employers
# POST  - creates a new employer with the request body data
@app.route('/employers', methods=['GET', 'POST'])
def employers():
    if request.method == 'GET':
        return get_employers(mysql)
    elif request.method == 'POST':
        return create_employer(request.get_json(), mysql)

# GET       - returns employer with id == {id}
# PUT       - updates employer with id == {id}
# DELETE    - removes employer with id == {id}
@app.route('/employers/<id>', methods=['GET', 'PUT', 'DELETE'])
def employers_id(id):
    if request.method == 'GET':
        return get_employer(id, mysql)
    elif request.method == 'PUT':
        return update_employer(id, request.get_json(), mysql)
    elif request.method == 'DELETE':
        return delete_employer(id, mysql)

# EMPLOYEE CREATE

@app.route('/api/employees', methods=['POST'])
def createEmployee():
    try:
        cur = mysql.connection.cursor()
        name = request.get_json()['name']
        email = request.get_json()['email']
        success = request.get_json()['success']
        employer_id = request.get_json()['employer_id']
        cur.execute("INSERT INTO employee (name, email, employer_id, success) VALUES ('" + str(name) + "', '" + str(email) + "', '" + str(employer_id) + "', '" + str(success) + "')")
        mysql.connection.commit()
        result = {'name': name, 'email': email, 'employer_id': employer_id, 'success': success}
        return jsonify({'result': result}), status.HTTP_201_CREATED
    except Exception as e:
        return "The new Employee is invalid or null", status.HTTP_400_BAD_REQUEST

# EMPLOYEE RETURN

@app.route('/api/employees', methods=['GET'])
def getEmployees():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM employee")
    rv = cur.fetchall()
    return jsonify(rv)

@app.route('/api/employees/<id>', methods=['GET'])
def getEmployee(id):
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM employee WHERE employee_id = " + id)
    rv = cur.fetchall()
    if rv:
        return jsonify(rv)
    else:
        return "The Employee with id " + id + " was not found", status.HTTP_404_NOT_FOUND

 # EMPLOYEE UPDATE

@app.route('/api/employees/<id>', methods=['PUT'])
def updateEmployee(id):
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM employee WHERE employee_id = " + id)
    result = cur.fetchone()
    if result:
        cur = mysql.connection.cursor()
    else:
        return "The Employee with id " + id + " was not found", status.HTTP_404_NOT_FOUND 

    try:  
        name = request.get_json()['name']
        email = request.get_json()['email']
        success = request.get_json()['success']
        employer_id = request.get_json()['employer_id']
        cur.execute("UPDATE employee SET name = '" + str(name) + "', email = '" + str(email) + "', success = '" + str(success) + "', employer_id = '" + str(employer_id) + "' WHERE employee_id = " + id)
        mysql.connection.commit()
        result = {'name': name, 'email': email, 'employer_id': employer_id, 'success': success}
        return jsonify({'result': result})
    except Exception as e:
        return "The new Employee is invalid or null", status.HTTP_400_BAD_REQUEST

# EMPLOYEE DELETE

@app.route('/api/employees/<id>', methods=['DELETE'])
def deleteEmployee(id):
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM employee WHERE employee_id = " + id)
    result = cur.fetchone()
    if result:
        cur = mysql.connection.cursor()
    else:
        return "The Employee with id " + id + " was not found", status.HTTP_404_NOT_FOUND 

    cur = mysql.connection.cursor()
    response = cur.execute("DELETE FROM employee WHERE employee_id = " + id)
    mysql.connection.commit()

    if response > 0:
        result = {'message': 'Employee deleted'}

    return jsonify({'result': result})
    

# For development only, do not deploy into production.
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8655)