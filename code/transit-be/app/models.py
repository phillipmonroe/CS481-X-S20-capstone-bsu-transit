from . import db

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

    def __repr__(self):
        return '<Employer {}>'.format(self.name)