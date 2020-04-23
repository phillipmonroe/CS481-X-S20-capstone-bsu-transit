from flask import request
from flask import current_app as app
from .functions import *


@app.route('/')
def test_service():
    """ 
    Test service is running correctly. This route exposes an endpoint that returns a service is running prompt.
    """

    return "Transit backend service is running."


@app.route('/upload', methods=['POST'])
def add_csv():
    """
    This is a method to get the csv file and the employer name from the
    front end, so we can parse it into the database.
    Returns:
        error_list: If there are any names added to the list, it will return
        that list of names.
    """

    employer_email = request.form['user']
    file = request.files['uploads[]'].stream.read().decode("utf-8", "strict")
    error_list = parse_new_csv(file, employer_email)
    return "Successfully added all employees" if not error_list else error_list


@app.route('/employers', methods=['GET', 'POST'])
def employers():
    """
    GET   - returns all employers
    POST  - creates a new employer with the request body data
    """

    if request.method == 'GET':
        return get_employers()
    elif request.method == 'POST':
        return create_employer(request.get_json())


@app.route('/employers/<id>', methods=['GET', 'PUT', 'DELETE'])
def employers_id(id):
    """
    GET       - returns employer with id == <id>
    PUT       - updates employer with id == <id>
    DELETE    - removes employer with id == <id>
    """

    if request.method == 'GET':
        return get_employer(id)
    elif request.method == 'PUT':
        return update_employer(id, request.get_json())
    elif request.method == 'DELETE':
        return delete_employer(id)


@app.route('/employers/<id>/employees', methods=['GET'])
def employer_employees(id):
    """
    GET       - returns employees with employer_id == <id>
    """

    return get_employer_employees(id)


@app.route('/employees', methods=['GET', 'POST'])
def employees():
    """
    GET       - returns all employees
    POST      - creates a new employee with the request body data
    """

    if request.method == 'GET':
        return get_employees()
    elif request.method == 'POST':
        return create_employee(request.get_json())


@app.route('/employees/<id>', methods=['GET', 'PUT', 'DELETE'])
def employees_id(id):
    """
    GET       - returns employee with id == <id>
    PUT       - updates employee with id == <id>
    DELETE    - removes employee with id == <id>
    """

    if request.method == 'GET':
        return get_employee(id)
    elif request.method == 'PUT':
        return update_employee(id, request.get_json())
    elif request.method == 'DELETE':
        return delete_employee(id)


@app.route('/issue/<employer_id>', methods=['POST'])
def issue(employer_id):
    """
    POST    - pushes out tickets to provided employer_id
    """

    return issue_employer_tickets(employer_id)


@app.route('/issued/<employer_id>', methods=['GET'])
def issued(employer_id):
    """
    GET    - pushes out tickets to provided employer_id
    """

    return get_tickets(employer_id)
