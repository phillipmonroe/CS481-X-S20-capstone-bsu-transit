CREATE TABLE IF NOT EXISTS admin(
	admin_id INTEGER NOT NULL  PRIMARY KEY auto_increment,
    name varchar(50) NOT NULL,
    email varchar(64) UNIQUE NOT NULL);
    
CREATE TABLE IF NOT EXISTS employer(
		employer_id INTEGER NOT NULL PRIMARY KEY auto_increment,
        name varchar(50) NOT NULL,
        email varchar(64) UNIQUE NOT NULL,
        rider_cap INTEGER NOT NULL);
        
CREATE TABLE IF NOT EXISTS employee(
	employee_id INTEGER NOT NULL PRIMARY KEY auto_increment,
    name varchar(50) NOT NULL,
    email varchar(64) UNIQUE NOT NULL,
    employer_id INTEGER,
    success BOOLEAN,
    foreign key(employer_id) references employer(employer_id)
    on delete cascade);
    
    CREATE TABLE IF NOT EXISTS issued(
		issued_id INTEGER NOT NULL PRIMARY KEY auto_increment,
		date_issued DATETIME DEFAULT NOW(),
        next_issue_date DATETIME NOT NULL,
        employee_id INTEGER,
	 employer_id INTEGER,
        foreign key(employer_id) references employer(employer_id),
        foreign key(employee_id) references employee(employee_id));
        
	CREATE TABLE IF NOT EXISTS errors(
    error_id INTEGER NOT NULL PRIMARY KEY auto_increment,
    error_messsage varchar(256) NOT NULL,
    employee_id INTEGER,
    foreign key(employee_id) references employee(employee_id)
    on delete cascade);
        
        
