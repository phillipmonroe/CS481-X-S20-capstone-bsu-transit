from flask import Flask, request, Response
import mysql.connector

app = Flask(__name__)

@app.route('/')
def test_service():
    """ 
    Test service is running correctly. This route exposes an endpoint that returns a service is running prompt.
    """
    return "Transit backend service is running."

# For development only, do not deploy into production.
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8655)