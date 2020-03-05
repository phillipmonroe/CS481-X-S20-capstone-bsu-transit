## 1/30 Meeting
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


## 2/6 Meeting at Transit
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

## 2/13
Single sign on options: 
Google - requires google account
Amazon - find out any req
Auth0 - works with any?

Talked general strategy with Jared
Katie got there the last five minutes when the most productive questions got answered
OVERALL DESIGN:
Need capability of pushing tickets to customers (appearing on existing app)
Allow employers to input accounts that they want to connect
  - could be existing or created, still unsure
  - master list of employees 
    - some number of those employees will actually use the service
  - no concern about company pays base rate employee pays for individual combination
CSV Parsing could be helpful
Possible endpoints:
  Import / create many new
  Delete many
  Create single
  Delete single
  Push ticket to Account
    - should have an automated schedule to push monthly passes
  
  ## 2/19 meeting
  Major topics of conversation were possible pitfalls we could run into / how are they doing things now.
  Right now Excel file filled with employee emails
    Each employee on the list gets a paper monthly pass hand delivered by VRT
    Modifications to excel file are manual
  Hopefully we automate the process for VRT to manage the employers (create employer, change max number employees, delete employers)
  Employers should be able to modify the people they have listed as their employees
    input employees, auto link to account? Create account?
  
  
  ## 2/25 meeting
  Had a much better meeting with Katie around the entire time. Learned a lot of what the actual scope of the project is.
  Basically we want to automate the process of employers adding employees, and push monthly passes out automatically to all employees that the employer listed. 
  VRT shouldn't have to do much besides adding employers and changing their max number if it comes to that.
  VRT will still manually take payments and decide on their own what kind of deal the employer will get. 
  
  Employers add and remove employees
  Need some way of seeing if the person is linked to account?
    Did pass successfully send?
  Passes last 31 days *from activatation*
  We will send out every 31 days regardless of activation
  New Employees - send out pass immediately, then on schedule of employer
  Maybe scheduler run every night to send out all passes to failed
    
  Made our first stories, decided on who gets to tackle which
  Me and Justin:
    Send a valid request to Masabi API (validate credentials, figure out endpoints)
    
  ## 3/1 meeting
  Checked in on what we had accomplished the previous week.
  DB is finalized, should be able to start deciding on operations against the database.
  Basic skeletons of pages done, should be able to fill in
  
  Everyone did well on their stories, had pull requests
  Discusses stories for the coming week.
  
  Mine:
  CRUD operations of issued tickets
