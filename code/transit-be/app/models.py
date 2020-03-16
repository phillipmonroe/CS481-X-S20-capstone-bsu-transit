from . import db, ma

class Employer(db.Model):
    """Model for Employers"""

    __tablename__ = 'employers'
    id = db.Column(db.Integer,
                   primary_key=True)
    name = db.Column(db.String(64),
                         index=False,
                         unique=False,
                         nullable=False)
    email = db.Column(db.String(80),
                      index=True,
                      unique=True,
                      nullable=False)
    rider_cap = db.Column(db.Integer,
                        index=False,
                        unique=False,
                        nullable=False)
    employees = db.relationship('Employee', backref='employer', lazy=True)

    employees = db.relationship('Employee', backref='employers', lazy=True)
    issued = db.relationship('Issued', backref='employers', lazy=True)

    def __repr__(self):
        return '<Employer {}>'.format(self.name)


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


class EmployeeSchema(ma.ModelSchema):
    class Meta:
        fields = ("id", "name", "email", "employer_id", "success")
employee_schema = EmployeeSchema()

class IssuedSchema(ma.ModelSchema):
    class Meta:
        fields = ("issued_id", "issue_date", "employee_id", "employer_id")
issued_schema = IssuedSchema(many=True)
