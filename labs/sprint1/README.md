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
