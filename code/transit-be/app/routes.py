from flask import Flask, request, Response, jsonify, abort
from flask import current_app as app
from .functions import *

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
        return get_employers()
    elif request.method == 'POST':
        return create_employer(request.get_json())

# GET       - returns employer with id == {id}
# PUT       - updates employer with id == {id}
# DELETE    - removes employer with id == {id}
@app.route('/employers/<id>', methods=['GET', 'PUT', 'DELETE'])
def employers_id(id):
    if request.method == 'GET':
        return get_employer(id)
    elif request.method == 'PUT':
        return update_employer(id, request.get_json())
    elif request.method == 'DELETE':
        return delete_employer(id)

# GET       - returns employees with employer_id == <id>
@app.route('/employers/<id>/employees', methods=['GET'])
def employer_employees(id):
    return get_employer_employees(id)

# GET       - returns all employees
# POST      - creates a new employee with the request body data
@app.route('/employees', methods=['GET', 'POST'])
def employees():
    if request.method == 'GET':
        return get_employees()
    elif request.method == 'POST':
        return create_employee(request.get_json())

# GET       - returns employee with id == <id>
# PUT       - updates employee with id == <id>
# DELETE    - removes employee with id == <id>
@app.route('/employees/<id>', methods=['GET', 'PUT', 'DELETE'])
def employees_id(id):
    if request.method == 'GET':
        return get_employee(id)
    elif request.method == 'PUT':
        return update_employee(id, request.get_json())
    elif request.method == 'DELETE':
        return delete_employee(id)
