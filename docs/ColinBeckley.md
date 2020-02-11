1/30 Meeting
Communication options for collaboration, settled on GroupMe.

CityGo project for Vallery Regional Transit (VRT)
  Currently using "Justride", something provided by Masabi (payment processor)
  
Requirements + user stories outline:
  Employers need to set up employees
    As an employer I need access to employees and ... (still figuring out)
  CityGo employees (not programmers) need to interact for employers (Administer)
    As a CityGo admin I want to administer employers
  employees just log in and have access to ticketss

Flow of information: App (front end to employer+employee+citygo) -> Server (+ DB) -> Masabi
Most likely making parallel app

Language: Options thrown around were Python / C#/ Kotlin 
Settled on Python3 backend Flask for the Http
Angular frontend + Material for design
Docker
Mysql

Things to do:
Me create folder for code
Sean set up github (not needed)
Des send message in groupme for coordinating times


2/6 Meeting at Transit
CityGo admin was unavailable again, have to get quesions answered next week.
Looked at API documentation more closely
  Ask Masabi some questsions
  Ask CityGo some questions
  
 Employer: 
 Add accounts - create accounts for the employees? Employee creates separately - click this link?
 How do we get ID of an existing account (to add tickets onto)
 What kind of things does the employer need to add (monthly tickets? Daily? On schedules?)
 Shouldn't need any kind of payment processing
 Add new product for the emplyers to use? No charge for this one - good validation for no abuse (types of passes)
 Log in employees
  single sign on from google etc.?
 Look up firebase
