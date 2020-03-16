from flask import jsonify, abort
from datetime import datetime, timedelta
from .models import *

#   Transit Service Functions

# --Employer CRUD Operations--
#   Return All Employers
def get_employers():
    try:
        return "reached get_employers"
    except Exception as e:
        print(e)
        abort(404, "Could not retrieve employers")
#   Add New Employer
def create_employer(json):
    try:
        return "reached create_employer"
    except Exception as e:
        print(e)
        abort(400, "Could not create new employer")        
#   Get Specified Employer
def get_employer(id):
    try:
        return "reached get_employer"
    except Exception as e:
        print(e)
        abort(404, "Could not retrieve employer")
        
#   Update Specified Employer
def update_employer(id, json):
    try:
        return "reached update_employers"
    except Exception as e:
        print(e)
        abort(404, "Could not update employer")        
#   Delete Specified Employer
def delete_employer(id):
    try:
        return "reached delete_employers"
    except Exception as e:
        print(e)
        abort(404, "Could not delete employer")

#-- Employee CRUD Operations

#-- VERIFICATION NOTES
# To test run python wsgi.py
# Send requests to the routes defined
# in routes.py that call the functions
# in this file
# Ensure that the databse is updated
# after accessing each end point if it
# should have updated the database

#   Add New Employee
def create_employee(json):
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
        abort(400, "Could not create new employee") 

#   Return All Employees
def get_employees():
    try:
        employees = Employee.query.all()
        output = employee_schema.dump(employees, many=True)
        return jsonify(output)
    except Exception as e:
        print(e)
        abort(404, "Could not retrieve employees")  

#   Get Specified Employee
def get_employee(id):
    try:
        employee = Employee.query.get(id)
        output = employee_schema.dump(employee)
        return jsonify(output)
    except Exception as e:
        print(e)
        abort(404, "Could not retrieve employee")

#   Get Employers Employees
def get_employer_employees(id):
    try:
        employees = Employee.query.filter_by(employer_id=id).all()
        output = employee_schema.dump(employees, many=True)
        return jsonify(output)
    except Exception as e:
        print(e)
        abort(404, "Could not get employer's employees")
       
#   Update Specified Employee
def update_employee(id, json):
    try:
        employee = Employee.query.get(id)
        employee.name = json['name']
        employee.email = json['email']
        employee.employer_id = json['employer_id']
        success = json['success']
        db.session.add(employee)
        db.session.commit()
        output = employee_schema.dump(employee)
        return jsonify(output)
    except Exception as e:
        print(e)
        abort(404, "Could not update employee")  

#   Delete Specified Employee
def delete_employee(id):
    try:
        employee = Employee.query.get(id)
        db.session.delete(employee)
        db.session.commit()
        return jsonify({'message': 'Employee deleted'})
    except Exception as e:
        print(e)
        abort(404, "Could not delete employee")


def issue_tickets(employer_id):
    try:
        #TODO: A masabi call to issue tickets to the employee 
        #we should probably use the issue_date that is returned from the masabi API call(s) that would happen, but for right now I'm using this one datetime
        issue_date = datetime.utcnow()

        employees = Employee.query.filter(Employee.employer_id==employer_id).all()
        for employee in employees:
            if not employee.success:
                #single masabi calls would occur here, if successful then create issued table entry + update employee
                issue = Issued(issue_date, employee.id, employer_id)
                db.session.add(issue)
                if issue:
                    employee.success = True

        db.session.commit()
        return jsonify(employee_schema.dump(employees,many=True))
    except Exception as e:
        print(e)
        abort(500, "how did we get here")


def get_tickets(employer_id):
    try:
        cutoff_date = datetime.utcnow() - timedelta(days=31)
        issued_tickets = Issued.query.filter(Issued.issue_date > cutoff_date).all()
        
        return jsonify(issued_schema.dump(issued_tickets))
    except Exception as e:
        print(e)
        abort(500, "an exception here is shameful")