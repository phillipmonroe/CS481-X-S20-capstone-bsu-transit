from flask import jsonify, abort
from .models import db, Employer
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
        
