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
    

    def __repr__(self):
        return '<Employee {}>'.format(self.name)
    
    def __init__(self, name, email, employer_id, success):
        self.name = name
        self.email = email
        self.employer_id = employer_id
        self.success = success

class EmployeeSchema(ma.ModelSchema):
    class Meta:
        model = Employee