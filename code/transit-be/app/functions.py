from flask import jsonify, abort
from sqlalchemy import or_
from datetime import datetime, timedelta
import simplejson as json
from flask import current_app as app
import csv
import uuid
import os

from .models import *
import requests


#   Transit Service Functions

# --Employer CRUD Operations--

def get_employers():
    """Returns all Employers stored in the database

    Returns:
    json
        a json response containing all employers in the database

    Raises:
    Exeption
        Any exception will be logged and the funciton will abort
    """

    try:
        employers = Employer.query.all()
        output = employer_schema.dump(employers, many=True)
        return jsonify(output)
    except Exception as e:
        print(e)
        app.logger.error("an error({}) occurred getting employers".format(e))
        abort(404, "Could not retrieve employers")

#   Add New Admin
def create_admin(json):
    try:
        name = json['name']
        email = json['email']
        admin = Admin(name,email)
        db.session.add(admin)
        db.session.commit()
        output = admin_schema.dump(admin)
        return jsonify(output)
    except Exception as e:
        print(e)
        app.logger.error("an error({}) occurred creating admin with json {}".format(e, json))
        abort(400, "Could not create new admin")

def create_employer(json):
    """Creates an Employer in the database

    Parameters:
    json: json
        json containing the employer you wish to create

    Returns:
    json
        json containing the employer that was created

    Raises:
    Exeption
        Any exception will be logged and the funciton will abort
    """

    try:
        name = json['name']
        email = json['email']
        rider_cap = json['rider_cap']
        employer = Employer(name,
                            email,
                            rider_cap)
        db.session.add(employer)
        db.session.commit()
        output = employer_schema.dump(employer)
        return jsonify(output)
    except Exception as e:
        print(e)
        app.logger.error(
            "an error({}) occurred creating employer with json {}".format(e, json))
        abort(400, "Could not create new employer")


def get_employer(id):
    """Gets the employer with the specified id

    Parameters:
    id: int
        id of the employer you would like to retrieve

    Returns:
    json
        json containing the employer that was requested

    Raises:
    Exeption
        Any exception will be logged and the funciton will abort
    """

    try:
        employer = Employer.query.get(id)
        output = employer_schema.dump(employer)
        return jsonify(output)
    except Exception as e:
        print(e)
        app.logger.error(
            "an error({}) occurred getting employer with id {}".format(e, id))
        abort(404, "Could not retrieve employer")


def update_employer(id, json):
    """updates an employer in the database

    Parameters:
    id: int
        id of the employer you would like to update
    json: json
        json containing the new employer information

    Returns:
    json
        json containing the employer that was updated

    Raises:
    Exeption
        Any exception will be logged and the funciton will abort
    """

    try:
        employer = Employer.query.get(id)
        employer.name = json['name']
        employer.email = json['email']
        employer.rider_cap = json['rider_cap']
        db.session.add(employer)
        db.session.commit()
        output = employer_schema.dump(employer)
        return jsonify(output)
    except Exception as e:
        print(e)
        app.logger.error(
            "an error({}) occurred updating employer with id {}".format(e, id))
        abort(404, "Could not update employer")


def delete_employer(id):
    """Deletes an Employer in the database

    Parameters:
    id: int
        id of the employer to delete

    Returns:
    json
        json containing a message that says the employer was deleted

    Raises:
    Exeption
        Any exception will be logged and the funciton will abort
    """

    try:
        employer = Employer.query.get(id)
        db.session.delete(employer)
        db.session.commit()
        return jsonify({'message': 'Employer deleted'})
    except Exception as e:
        print(e)
        app.logger.error(
            "an error({}) occurred deleting employer with id {}".format(e, id))
        abort(404, "Could not delete employer")


def _get_employer_id(employer_email):
    """
    This is a private helper method that will get the employer id
    from the table based on the employer name associated
    with that account.

    Parameters:
    employer_email
        Email of the employer.

    Returns:
    employer_id
        The id of the employer
    """

    try:
        employer_id = db.session.query(Employer.id).filter(
            employer_email == Employer.email).first()

        return employer_id
    except Exception as e:
        print(e)
        app.logger.error(
            "an error({}) occurred finding employer with the name {}".format(e, employer_name))
        abort(404, 'employer not found')


# -- Employee CRUD Operations


def create_employee(json):
    """Creates an Employee in the database

    Parameters:
    json: json
        json containing the employee you wish to create

    Returns:
    json
        json containing the employee that was created

    Raises:
    Exeption
        Any exception will be logged and the funciton will abort
    """

    try:
        name = json['name']
        email = json['email']
        employer_id = json['employer_id']
        success = json['success']
        employee = Employee(name,
                            email,
                            employer_id,
                            success)
        db.session.add(employee)
        db.session.commit()
        output = employee_schema.dump(employee)
        return jsonify(output)
    except Exception as e:
        print(e)
        app.logger.error(
            "an error({}) occurred creating employee with json {}".format(e, json))
        abort(400, "Could not create new employee")


def get_employees():
    """Returns all Employees stored in the database

    Returns:
    json
        a json response containing all employees in the database

    Raises:
    Exeption
        Any exception will be logged and the funciton will abort
    """

    try:
        employees = Employee.query.all()
        output = employee_schema.dump(employees, many=True)
        return jsonify(output)
    except Exception as e:
        print(e)
        app.logger.error("an error({}) occurred getting employees".format(e))
        abort(404, "Could not retrieve employees")


def get_employee(id):
    """Gets the employee with the specified id

    Parameters:
    id: int
        id of the employee you would like to retrieve

    Returns:
    json
        json containing the employee that was requested

    Raises:
    Exeption
        Any exception will be logged and the funciton will abort
    """

    try:
        employee = Employee.query.get(id)
        output = employee_schema.dump(employee)
        return jsonify(output)
    except Exception as e:
        print(e)
        app.logger.error(
            "an error({}) occurred getting employee with id {}".format(e, id))
        abort(404, "Could not retrieve employee")


def get_employer_employees(id):
    """Gets the employees of the employer with the specified id

    Parameters:
    id: int
        id of the employer's employees you would like to retrieve

    Returns:
    json
        json containing the employees that were requested

    Raises:
    Exeption
        Any exception will be logged and the funciton will abort
    """

    try:
        employees = Employee.query.filter_by(employer_id=id).all()
        output = employee_schema.dump(employees, many=True)
        return jsonify(output)
    except Exception as e:
        print(e)
        app.logger.error(
            "an error({}) occurred deleting employees with employer id {}".format(e, id))
        abort(404, "Could not get employer's employees")


def update_employee(id, json):
    """updates an employee in the database

    Parameters:
    id: int
        id of the employee you would like to update
    json: json
        json containing the new employee information

    Returns:
    json
        json containing the employee that was updated

    Raises:
    Exeption
        Any exception will be logged and the funciton will abort
    """

    try:
        employee = Employee.query.get(id)
        employee.name = json['name']
        employee.email = json['email']
        employee.employer_id = json['employer_id']
        employee.success = json['success']
        db.session.add(employee)
        db.session.commit()
        output = employee_schema.dump(employee)
        return jsonify(output)
    except Exception as e:
        print(e)
        app.logger.error(
            "an error({}) occurred updating employee with id {}".format(e, id))
        abort(404, "Could not update employee")


def delete_employee(id):
    """Deletes an Employee in the database

    Parameters:
    id: int
        id of the employee to delete

    Returns:
    json
        json containing a message that says the employee was deleted

    Raises:
    Exeption
        Any exception will be logged and the funciton will abort
    """

    try:
        employee = Employee.query.get(id)
        db.session.delete(employee)
        db.session.commit()
        return jsonify({'message': 'Employee deleted'})
    except Exception as e:
        print(e)
        app.logger.error(
            "an error({}) occurred deleting employee with id {}".format(e, id))
        abort(404, "Could not delete employee")


def push_tickets(employees):
    """
    This is a method that pushes all of the tickets in the employees list
    from Masabi to the user.

    TODO: Set the MASABI_USER envrionment variable to your masabi username
    TODO: Set the MASABI_PASS environment vairable to your masabi password

    Parameters:
    employees
        A list of employees to push tickets to.
    """

    try:
        username = os.environ.get('MASABI_USER')
        password = os.environ.get('MASABI_PASS')
        credentials = {
            "username": username,
            "password": password
        }
        headers = {'Content-Type': 'application/json'}
        token_request = requests.post(
            "https://uat.justride.systems/auth-webapp/rest/v/1/VRTIDAHO/token",
            headers=headers, data=json.dumps(credentials))
        token = token_request.json()['token']

        headers = {'Authorization': token,
                   'Content-Type': 'application/json'}
        for employee in employees:
            order_request = {
                "userName": employee.email,
                "orderItems": [
                    {
                        "productRef": "31D_L",
                        "journeyId": "DISCRETE",
                        "quantity": 1
                    }
                ]
            }
            # create an order
            order = requests.post("https://uat.justride.systems/broker/api/v2/VRTIDAHO/externalorders",
                                  headers=headers, data=json.dumps(order_request))

            if order.status_code == 200:
                purchase_id = uuid.uuid4().hex

                issue_request = {
                    "userName": employee.email,
                    "purchaseId": "EXcg" + str(purchase_id),
                    "paymentInfos": []
                }

                # issue a ticket
                issued_ticket = requests.post("https://uat.justride.systems/broker/api/v2/VRTIDAHO/externalorders/" +
                                              order.json()['orderId'] + "/issue", headers=headers,
                                              data=json.dumps(issue_request))

                if issued_ticket.status_code == 200:
                    issue_date = datetime.utcnow()
                    issue = Issued(issue_date, employee.id,
                                   employee.employer_id)
                    db.session.add(issue)
                    employee.success = True
                else:
                    insert_error(employee.id, issued_ticket.status_code)
                    app.logger.error("an error({}: {}) occurred issuing a ticket to {}({})".format(
                        issued_ticket.json()['code'], issued_ticket.json()['message'], employee.name, employee.email))
            else:
                app.logger.error("an error({}: {}) occurred creating an order for {}({})".format(
                    order.json()['code'], order.json()['message'], employee.name, employee.email))
                insert_error(employee.id, issued_ticket.status_code)
    except Exception as e:
        print(e)
        app.logger.error(
            "An error({}) happened while pushing a ticket".format(e))


def issue_employer_tickets(employer_id):
    try:
        employees = Employee.query.filter(
            Employee.employer_id == employer_id, Employee.success == False).all()
        push_tickets(employees)
        db.session.commit()
        return jsonify(employee_schema.dump(employees, many=True))
    except Exception as e:
        print(e)
        app.logger.error(
            "an error({}) occurred issuing tickets for employer {}".format(e, employer_id))
        abort(500, "how did we get here")


def get_tickets(employer_id):
    try:
        cutoff_date = datetime.utcnow() - timedelta(days=31)
        issued_tickets = Issued.query.filter(
            Issued.issue_date > cutoff_date).all()

        return jsonify(issued_schema.dump(issued_tickets))
    except Exception as e:
        print(e)
        abort(500, "an exception here is shameful")


def nightly_ticket_issue():
    """
    This is a method to get a list of all the employees that
    have either been unsuccessful or their issued ticket is
    passed 31 days.
    """

    try:
        reissue_date = datetime.utcnow() - timedelta(days=31)
        reissue_list = db.session.query(Employee).join(Issued,
                                                       Employee.id == Issued.employee_id).filter(or_(
                                                           Employee.success == False, Issued.issue_date < reissue_date))
        push_tickets(reissue_list)
        return reissue_list
    except Exception as e:
        print(e)
        # TODO: this needs to be added to a log


def insert_error(employee_id, error_message):
    """
    This method will insert an error into the database for logging.
    If the employee exists in the table currently, then that persons
    error message will be over written keeping the most recent record only.
    """

    error = db.session.query(Error).get(employee_id)
    if error:
        error.error_message = error_message
        db.session.commit()
    else:
        new_error = Error(error_message, employee_id)
        db.session.add(new_error)
        db.session.commit()


def parse_new_csv(csv_file, employer_email):
    """
    A method to parse the new csv file input by the admin or the employer.
    The csv file should have two columns, name and email.
    Parameters:
        csv_file: CSV file to be parsed.
        employer_email: email of the employer that is inputting the data in order to get the id.
    Returns:
        error_list: A list of names that did not get added to the database.
    """

    employer_id = _get_employer_id(employer_email)
    error_list = {'name': []}
    csv_file = csv_file.splitlines()
    for line in csv_file:
        try:
            split_line = line.split(",")
            employee = Employee(
                split_line[0], split_line[1], employer_id, False)
            db.session.add(employee)
            db.session.commit()
        except Exception as e:
            print(e)
            app.logger.error(
                "an error({}) occurred inputting {} into the database".format(e, line[0]))
            error_list['name'].append(line[0])

    return jsonify(error_list)
