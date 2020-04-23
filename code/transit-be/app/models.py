from datetime import datetime, timedelta, date

from . import db, ma


class Employer(db.Model):
    """Model for Employers"""

    __tablename__ = 'employers'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=False, unique=False, nullable=False)
    email = db.Column(db.String(80), index=True, unique=True, nullable=False)
    rider_cap = db.Column(db.Integer, index=False, unique=False, nullable=False)


    employees = db.relationship('Employee', backref='employer', lazy=True)
    employees = db.relationship('Employee', backref='employers', lazy=True)
    issued = db.relationship('Issued', backref='employers', lazy=True)

    def __repr__(self):
        return '<Employer {}>'.format(self.name)

    def __init__(self, name, email, rider_cap):
        self.name = name
        self.email = email
        self.rider_cap = rider_cap

class Admin(db.Model):
    """Model for Admin"""

    __tablename__ = 'admin'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=False, unique=False, nullable=False)
    email = db.Column(db.String(80), index=True, unique=True, nullable=False)


    def __repr__(self):
        return '<Admin {}>'.format(self.name)

    def __init__(self, name, email):
        self.name = name
        self.email = email

class Employee(db.Model):
    """Model for Employees"""

    __tablename__ = 'employees'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=False, unique=False, nullable=False)
    email = db.Column(db.String(64), index=True, unique=True, nullable=False)
    employer_id = db.Column(db.Integer, db.ForeignKey('employers.id'))
    success = db.Column(db.Boolean, index=False, unique=False)

    issued = db.relationship('Issued', backref='employees', lazy=True)

    def __repr__(self):
        return '<Employee {}>'.format(self.name)
    
    def __init__(self, name, email, employer_id, success):
        self.name = name
        self.email = email
        self.employer_id = employer_id
        self.success = success


class Issued(db.Model):
    """Model for Issued Tickets"""

    __tablename__ = 'issued'
    issued_id = db.Column(db.Integer, primary_key=True)
    issue_date = db.Column(db.DateTime(), index=False, unique=False, nullable=False)
    employee_id = db.Column(db.Integer, db.ForeignKey('employees.id'))
    employer_id = db.Column(db.Integer, db.ForeignKey('employers.id'))

    def __repr__(self):
        return '<Issued {}>'.format(self.issued_id)
    
    def __init__(self, issued_date, employee_id, employer_id):
        self.issue_date = issued_date
        self.employee_id = employee_id
        self.employer_id = employer_id


class Error(db.Model):
    """
    Model for error table.
    """

    __tablename__ = 'error'
    error_id = db.Column(db.Integer, primary_key=True)
    error_message = db.Column(db.String(256), index=False, unique=False, nullable=False)
    employee_id = db.Column(db.Integer, db.ForeignKey('employees.id'))

    def __repr__(self):
        return '<Error {}'.format(self.error_id)

    def __init__(self, error_message, employee_id):
        self.error_message = error_message
        self.employee_id = employee_id

class EmployerSchema(ma.ModelSchema):
    class Meta:
        fields = ("id", "name", "email", "rider_cap")
employer_schema = EmployerSchema()

class AdminSchema(ma.ModelSchema):
    class Meta:
        fields = ("id", "name", "email")
admin_schema = AdminSchema()

class EmployeeSchema(ma.ModelSchema):
    class Meta:
        fields = ("id", "name", "email", "employer_id", "success")


employee_schema = EmployeeSchema()


class IssuedSchema(ma.ModelSchema):
    class Meta:
        fields = ("issued_id", "issue_date", "employee_id", "employer_id")


issued_schema = IssuedSchema(many=True)


class ErrorSchema(ma.ModelSchema):
    """
    Class to serilaize the error schema to send to the front end
    from the backend.
    """
    class Meta:
        fields = ("error_id", "error_message", "employee_id")


error_schema = ErrorSchema
