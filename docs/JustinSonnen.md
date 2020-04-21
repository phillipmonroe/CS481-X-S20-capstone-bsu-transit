### WEEK 3

 - Team was introduced to contacts from CityGo.
 - Had pictures taken for badges.

#### Discussed 
 - which development tools to use on this project.
 >Python(flask), angular, mySQL, VScode, pycharm, docker
 - where to deploy
 - demo milestones
 - git repository strategies (front end, back end, interface) 

#### User Stories:

_As an employer/university I want to add passes to employees/students_ <br/>
_As a CityGo employee/Admin I want to administer employers._

#### To Do
- install dependencies
- review the Masabi api
- familiarize myself with new dev tool
- update my schedule into doodle


### WEEK 4

- Met with Jared.  Katie was not available to meet this week.
- Received security badges.

#### Discussed 
- Reviewed Masabi's Recommended Flow graphic for using External Orders API.
- Logged questions to submit to Masabi and CityGo (Katie). 

#### Questions/Comments

- Using an existing UI template may be unnecessary
- We may consider a third party authentication service to manage user login
- Define: "get our stations", "get our stations back", and "get our products"
- Does it make more sense to create a separate userID for users receiving Employee issued tickets vs personal accounts??
- Payments will be handled separately.  If the Employer can access the application, they can add/delete users and issue tickets.
- How often can tickets be issued??  What is the rate limit??
- What ticket products/passes will be available (single day, 31 day)??
- Does it matter if the ticket holders are on different pass renewal schedules??
- Are Employer issued passes different from regular passes??
- What will happen to issued passes if the user is deleted/fired??
- What is a rider??
- What qualifies a rider for a purchase?
- Do we have access/link to user Id's as Masabi has them stored??
- The UI will be used by CityGo admin and Employers, but admin will have additional credentials.  
	- CityGo to have access to replicate the Employers UI flow. 
- Can the Employer create the account themselves from the app or will only admin have this access??

#### To Do
- Concept the UI and LogIn
- Become familiar with the build tools we are using.


### WEEK 5

##### Played the “name game”.

#### Options for the Login build, best to use third-party service:
- Google instant sign-in  https://developers.google.com/identity
- Auth0  https://auth0.com/
- Amazon https://developer.amazon.com/apps-and-games/login-with-amazon

##### Dez has created NG new (angular) in shared repo.

>At the end of our meeting we determined that our initial focus for this application will be to allow employers to push a bundle of passes to all of their employees that are participating under their "wallet".
_(Most of what we had discussed/planned was prior to this understanding and thus became less relevant)_ 


#### What we discussed:

##### Current sign up process for new users:
- CityGo sends an email that contains a link to the employer that will allow them to sign-up on the CityGo website.
- The employer distributes the email to their employees
- Employees follow the link and sign-up using their email (work email preferred but not always what they use)


Currently CityGo issues paper tickets.
Issuing paper tickets will be required in some cases, but the aim is to minimize
the paper ticket process and rather push tickets to the JustRide app.

Much of the current system involves manual data entry in excel.

It is not an issue signing up mid-month.
If an employee leaves the employer, the pass will just expire and not be reissued.


#### To Do:
##### Type up and email a list of questions for Katie, and same for Masabi. <br/>
_What kinds of tickets will be provided?_ <br/>
_What is a rider?_ <br/>
_What qualifies a rider for a purchase?  ..._

### WEEK 6

#### What we discussed:
- Employer should be able to log in and push passes out from masabi to the CityGo app
- CityGo admin will basically have the same functionality so a pass push can also be initiated inhouse
- For now we'll assume that all users have accounts

#### User Stories (bullet points to build tasks from)
 ##### Database
 - employer table and CityGo admin (name, email, cap, created date, etc)
 - record of passes issued out
 - Employees (email address, name, rideID)
 
 ##### Login
 Cognito - 50k users free
 
 ##### Onboarding CityGo Admin
 - CRUD on Employer
 - CRUD on Employee
 
 ##### Onboarding Employer Admin
  - enter list of employees
 - CSV
 - Modify individualy 
 - removed and add in bulk
 
 ##### Job that pushes passes (Jenkins)
- hit endpoint, need credentials
- every 30 days
 
 ##### SysOps
 - Docker
 - puppet
 - flask

### TASKS

- we'll use congnito
- simple CityGo skeleton admin page (visual prototyping)
- skeleton of database backend
- flask hello world + connect to mysql w/python3
- Docker (last)
- Test Post via masabi
- set up tests (personal ownership)
- python mocks
- add to ZenHub

### WEEK 7

#### What we discussed:

##### Desomond – Flask set up
- what kind of info will front end need so we can plan for endpoints
	
##### Colin/me - we got a 200 ok
- we may need some test users in the environment 
- talk to masabi about adding users
- masabi test endpoints

##### Garett – admin view (angular placeholder replaced)
- decide what kind of data each component will request
- admin data requests links to endpoint
- list of employers, ability to add or remove
- connect admin to specific employer page
- visual (google materials) css/design for all

##### Sean -  database schema (relationships)
- needs to transfer it
- once done will create the database
- will host locally for now (sql file)

##### Phillip – employer view of angular front page

##### Trey – login (used Auth0) will be committed to github
- returns an access token and ID token, will need to link to database
- Auth0 holds username/password
- certain set of users will have access
- restrict user creation?
- (check if user exists) 2nd step
- questions about user whitelist

### To Do
- research mcok testing for angular FE and flask BE endpoints

### WEEK 8

##### - To Do

- research testing and AngularCLI
- made pages for add-employer and add-employee

### WEEK 9

##### - To Do

out sick

### WEEK 10

##### - Spring Break

### WEEK 11

##### - To Do

- continue to learn AngularCLI
- add data table and input window for adding employees


### WEEK 12

##### - To Do

- added content to recorded demo


### WEEK 13

##### - To Do

- continue to learn AngularCLI
- add features to data table (sorting, pagination, delete)



