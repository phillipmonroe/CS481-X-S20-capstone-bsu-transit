# Setup
Install packages needed for the backend service via this command `pip install -r requirements.txt`. Run this command from within the backend directory.
Install the mysqlclient.whl that can be downloaded from the link in requirements.txt

# Run Flask Application
For development, run the Flask application locally via this command `python wsgi.py`.

# Test
Send a request to http://localhost:5000/.  
If the service is running correctly the request will be responded to with a simple "service is running" response.

- **[POST] /upload:** uploads a csv file
<br></br>
- **[GET] /employers:** returns all employers in the database
- **[POST] /employers:** creates a new employer
- **[GET] /employers/{id}:** gets the employer with the specified id
- **[PUT] /employers/{id}:** updates the employer with the specified id
- **[DELETE] /employers/{id}:** deletes the employer with the specified id
<br></br>
- **[GET] /employers/{id}/employees:** gets all employees with the specified employer id
- **[GET] /employees:** gets all employees
- **[POST] /employees:** creates a new employee
- **[GET] /employees/{id}:** gets the employee with the specified id
- **[PUT] /employees/{id}:** updates the employee with the specified id
- **[DELETE] /employees/{id}:** deletes the employee with the specified id
<br></br>
- **[GET] /issued/{employer_id}:** gets issued tickets associated with the employer_id
- **[POST] /issue/{employer_id}:** issues tickets to employees with the specified employer_id
