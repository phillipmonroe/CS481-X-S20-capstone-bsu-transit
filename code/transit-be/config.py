from os import environ

class Config:
    """Set Flask configuration vars from .env file."""

    # Database
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqldb://admin:CityGoDevDBPasswrd!@citygo-dev-db.cswntfgziuif.us-west-2.rds.amazonaws.com:3306/city-go-db'
    SQLALCHEMY_TRACK_MODIFICATIONS = 'False'