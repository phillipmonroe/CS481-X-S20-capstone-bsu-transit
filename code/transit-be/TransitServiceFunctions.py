from TransitService import jsonify, abort, status
#   Transit Service Functions

# --Employer CRUD Operations--
#   Return All Employers
def getEmployers(mysql):
    try:
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM employer")
        rv = cur.fetchall()
        cur.close()
        return jsonify(rv)
    except Exception as e:
        print(e)
        abort(404, "Could not retrieve employers")
#   Add New Employer
def createEmployer(json, mysql):
    try:
        cur = mysql.connection.cursor()
        name = json['name']
        email = json['email']
        riderCap = json['rider_cap']
        cur.execute("INSERT INTO employer (name, email, rider_cap) VALUES ('" + str(name) + "', '" + str(email) + "', '" + str(riderCap) + "')")
        mysql.connection.commit()
        result = {'name': name, 'email': email, 'rider_cap': riderCap}
        cur.close()
        return jsonify({'result': result}), status.HTTP_201_CREATED
    except Exception as e:
        print(e)
        abort(400, "Could not create new employer")        
#   Get Specified Employer
def getEmployer(id, mysql):
    try:
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM employer WHERE employer_id = " + id)
        rv = cur.fetchall()
        cur.close()
        if rv:
            return jsonify(rv)
        else:
            abort(404, "Employer not found")
    except Exception as e:
        print(e)
        abort(404, "Could not retrieve employer")
        
#   Update Specified Employer
def updateEmployer(id, json, mysql):
    try:
        cur = mysql.connection.cursor()
        name = json['name']
        email = json['email']
        riderCap = json['rider_cap']
        cur.execute("UPDATE employer SET name = " + str(name) + ", email = " + str(email) + ", rider_cap = " + str(riderCap) + " WHERE employer_id = " + id)
        mysql.connection.commit()
        result = {'name': name, 'email': email, 'rider_cap': riderCap}
        cur.close()
        return jsonify({'result': result}), status.HTTP_200_OK
    except Exception as e:
        print(e)
        abort(404, "Could not update employer")        
#   Delete Specified Employer
def deleteEmployer(id, mysql):
    try:
        cur = mysql.connection.cursor()
        cur.execute("DELETE FROM employer WHERE employer_id = " + id)
        mysql.connection.commit()
        cur.close()
        return status.HTTP_200_OK
    except Exception as e:
        print(e)
        abort(404, "Could not delete employer")
        
