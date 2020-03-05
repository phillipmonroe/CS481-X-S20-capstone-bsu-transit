from flask import Flask, request, Response
from TransitServiceFunctions import *
import mysql.connector

app = Flask(__name__)

@app.route('/')
def test_service():
    """ 
    Test service is running correctly. This route exposes an endpoint that returns a service is running prompt.
    """
    return "Transit backend service is running."

# GET returns all employers
# POST creates a new employer with the request body data
@app.route('/employers', methods=['GET', 'POST'])
def employers():
    if request.method == 'GET':
        return getEmployers()
    elif request.method == 'POST':
        return createEmployer()

# GET returns employer with id == {id}
# PUT updates employer with id == {id}
# DELETE removes employer with id == {id}
@app.route('/employers/{id}', methods=['GET', 'PUT', 'DELETE'])
def employersId():
    if request.method == 'GET':
        return getEmployer()
    elif request.method == 'PUT':
        return updateEmployer()
    elif request.method == 'DELETE':
        return deleteEmployer()


# For development only, do not deploy into production.
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8655)