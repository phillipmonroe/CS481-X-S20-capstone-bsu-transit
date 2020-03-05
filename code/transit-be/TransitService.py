from flask import Flask, request, Response, jsonify
# import mysql.connector
from flask_mysqldb import MySQL
from flask_cors import CORS
from flask_api import status

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

# EMPLOYEE CREATE

@app.route('/api/employees', methods=['POST'])
def createEmployee():
    try:
        cur = mysql.connection.cursor()
        name = request.get_json()['name']
        email = request.get_json()['email']
        employer_id = request.get_json()['employer_id']
        cur.execute("INSERT INTO employee (name, email, employer_id) VALUES ('" + str(name) + "', '" + str(email) + "', '" + str(employer_id) + "')")
        mysql.connection.commit()
        result = {'name': name, 'email': email, 'employer_id': employer_id}
        return jsonify({'result': result}), status.HTTP_201_CREATED
    except Exception as e:
        return "The new Employee is invalid or null", status.HTTP_400_BAD_REQUEST

# For development only, do not deploy into production.
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8655)