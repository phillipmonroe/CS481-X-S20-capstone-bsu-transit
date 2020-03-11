from flask import jsonify, abort
from .models import db, ma, Employer, Employee, EmployeeSchema
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
employee_schema = EmployeeSchema()
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
        output = employee_schema.dump(employees,many=True)
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
        output = employee_schema.dump(employees,many=True)
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
        
