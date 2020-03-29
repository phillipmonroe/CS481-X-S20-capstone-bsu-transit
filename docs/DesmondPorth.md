# Work Log
## Week 3
## 1/28/2020
Met with Shane Panter in class. Had no updates for him because we had not met with our project sponsor yet.  

## 1/30/2020
Met with sponsor Jared. Had our picture taken for the ID badge. Started to discuss the scope/semantics of our project with sponsors.  
Meeting notes:  
&nbsp;&nbsp;Development stack  
&nbsp;&nbsp;&nbsp;- Angular - Frontend  
&nbsp;&nbsp;&nbsp;- Python Flask web service - Backend  
&nbsp;&nbsp;&nbsp;- MySQL database - Backend  
&nbsp;&nbsp;&nbsp;- Docker  
&nbsp;&nbsp;Using Docker to virtualize frontend and backend  
&nbsp;&nbsp;Homework specific for myself  
&nbsp;&nbsp;&nbsp;&nbsp;- Review Masabi API documentation  
&nbsp;&nbsp;&nbsp;&nbsp;- Create Doodle poll for group member availability for extra (outside of class) meetings  
&nbsp;&nbsp;&nbsp;&nbsp;- Set up my machine with the tools/software listed in development stack  

## Week 4
## 2/1/2020
Completed Doodle poll for my availability  
Set up my local machine with the development stack  
Reviewed Masabi API documentation  

## 2/4/2020
Met with Shane Panter in class. Had no updates for him. We discussed the conversation our team had with the sponsors.

## 2/6/2020
Met with sponsor. Started to plan the design around the two user stories we came up with during our first meeting. Those being:  
&nbsp;&nbsp; - As an Employer/Staff I want to add passes to an Employee/Student  
&nbsp;&nbsp; - As a CityGo admin I want to adminster Employees  
Questions for Masabi:  
&nbsp;&nbsp;- What identifies an account (Rider object in API diagram)?  
&nbsp;&nbsp;- Can we get that information for an existing account?  
Questions for Katie:  
&nbsp;&nbsp;- What type of passes are we going to adminster to Employees? 31 day pass, permanent pass?  
Homework specific for myself  
&nbsp;&nbsp;- Add initial Angular files to our project code base  
&nbsp;&nbsp;&nbsp;&nbsp; Accomplished with ng new  
&nbsp;&nbsp;- Look into using a third party to manage logins to our front end  

## Week 5
## 2/13/2020  
Use Google single sign in to manage login authentication.  
Developed more clear questions for Katie:  
&nbsp;&nbsp;What type of ticket do we provision?  
&nbsp;&nbsp;Login system would we be limited to  
&nbsp;&nbsp;&nbsp;&nbsp;Google SSO  
&nbsp;&nbsp;&nbsp;&nbsp;Amazon  
&nbsp;&nbsp;&nbsp;&nbsp;Auth0  
&nbsp;&nbsp;Will users be able to buy other passes using CityGo account  
Developed more clear questions for Masabi:  
&nbsp;&nbsp;What identifies a rider?  
&nbsp;&nbsp;Do we have access to that Resource?  
&nbsp;&nbsp;Access to product?  
Upon termination grace period is remaining employee pass 
Employer pays CityGo base membership, pushing passes
Employer pays CityGo base membership, not pushing passes
Unaffiliated, city go manages pushing passes  

## 2/18/2020
Met with Shane. Updated him on the meeting our team had with Transit last week.  

## Week 7
## 2/20/2020
Developed a clear path of development for our team to follow. Decided we will only deal with 31 day passes.  
Homework specific for myself  
&nbsp;&nbsp;- Create Flask application with a MySQL connector library imported.
&nbsp;&nbsp;- Track development using an Agile Development workflow with Zenhub.

## 2/25/2020
Met with Shane. Expressed that our team finally has a clear path to follow. Katie attended the meeting last week and cleared up the waters.

## Week 8
## 2/27/2020
Met with Jared, gave the status of our work during sprint 1, discussed future work and outlined below:  
| Stories               | Task                                             |
|-----------------------|--------------------------------------------------|
| Flask                 | Create endpoints as needed                       |
| Angular Admin View    | Admin data request                               |
| CityGo                | Setup test users                                 |
| Masabi                | Use POST/PUT data changing requests to their api |
| Angular Employer View | Employer data request                            |
| Auth0                 | Questions about login whitelist                  |

## 3/2/2020
Out of class sick. Continued to work on Angular frontend development. Finished a dynamic front end table for city go admin view

## Week 9
Assigned to work on backend security. Researching Python Flask JWT as a method to accomplish protecting the backend endpoints. Also need to look into using Auth0 in conjunction with JWT to protect backend endpoints.
