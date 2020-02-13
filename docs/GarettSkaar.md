# Garett Skaar - Transit Notes

[Week 2](#week-2)

[Week 3](#week-3)

[Week 4](#week-4)

## Week 2

We meet with Jared today and he walked us down to the City Go/Valley Regional Transit Office. We had our pictures taken for security access badges.

We then began to discuss the project at very high level. The basic idea is to allow a portal, for employers, to grant their employees some form of transportation pass using the existing Masabi API. This portal will also be used by City Go employees to administer and manage employers capable of distributing these passes. We are expecting to recieve User stories from City Go that will explain these needs in more detail.

#### Potential User Story
* As an employer I want to add passes to my employees account so that they can utilize their transit benefits.
* As a City Go admin, I want to administer city employers, so that they can distribute transit passes to their employees

| Potential Users 	   |
| :-------------------:|
| Downtown Employers   | 
| Downtown Employees   |
| BSU Students/Faculty |
| City Go Staff 	   |

#### Tasks

* Setup our repository with zenhub
* Complete Doodle form to determine time outside of class schedule to meet
* Research the Masabi API and understand it
* Install agreed upon technology stack for personal development enviroment
  * python3(Flask)
  * MySQL
  * Angular with Angular Material
  * Docker

## Week 3

We were able to get our security badges for the VRT office. Our main City Go contact was out of town this week, so we are still waiting on more concrete User Stories for the application. We used our time in the office to talk about how we may implement certain aspects of the application, but it was difficult because we still don't know exactly what we are developing. At a very high level, we discussed Employer needs, Admin needs, and Rider needs. Again, these are all expected to change, but it did produce some good questions for us to ask both our sponser and Masabi.

Once we find out how City Go will deal transit passes to Employers, we can then discuss in detail, how to build our application and handle transactions with Masabi. In the mean time, we plan on emailing Masabi questions and studying their API, to see what flexibility we have with these transit passes. Our City Go sponser will be at the next meeting and I believe we will then be able to formulate actual User Stories and begin prototyping our application.

## Week 4

Today we met hoping that Katie would be there to answer some of our questions about what it is we are trying to achieve. She did, however, have a sales pitch that hour and couldn't make it until the end. During our meeting, we did make some good work discussing what we would do given circumstance A, B, or C. Once Katie made it in, she explained that the primary focus should be on the distribution of passes from an Employer to an Employee.

#### The System in Place

There is still some confusion about how this is currently being done. It sounds as though Employers will recieve an email with a link from City Go. This Email will then be sent to all Employees that qualify for the transit pass. The Employee will then click the link, which will take them to a City Go sign up page. The form is completed and then City Go is notified that a new user has been created. The new user is then cross checked with the list of employees that are on the valid list. If the employee is found on the list, they are then given the benefits provided and they can then use them through their ride app.That is my take away from what we discussed, but there is plenty of room for error.

#### The New System to be Built

Ideally, if an employer chooses to pay for any form of transit for their employees, they will use our application to distribute these passes to their individual employees and automatically upload their Rider app with the transit pass. Instead of emails chained down with a link and a sign up, the Employee will just open their Ride app and use the pass. It is required that we still keep the physical paper passes in play. 

We may need to create City Go accounts on the fly, or even Ride accounts on the fly as well. We have alot more to discuss, but we are getting close to a goal and some concrete user stories.
