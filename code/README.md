# City Go Transit Application

## Executive Summary

The purpose of this application is to allow City Go Administrators and City Go Clients the ability to manage transit benefits for qualified employees. Employers will be able to add employees to the application by either uploading from a CSV file or a single entry. Once these employees are in the system, the application will attempt to push out a 31 day pass every month to employees, based on their email address. We assume that employees have already created a CityGo account with their provided work email. Admins have the added ability of managing other admins, employers, and employees.

#### Current Limitations
1. Employers have access to ALL employees, not just their own
2. Admins/employers created in our backend are not created in Auth0 (currently made through dashboard)
3. Front end is missing update and delete functionality for both City-Go-Admin and Employer views
4. Admin/Employer front end doesn't have a button for issuing tickets to Employees.
5. Front end doesn't send information of currently logged in account to backend (to issue ticket to logged in Employer etc.)
6. Current status of Employees (issued ticket vs. not issued ticket) is not being displayed.

## User: City Go Administrator

A City Go Administrator should have the ability to log on to the application and view Employers that have signed up for City Go transit benefits. Admins need the ability to Add, Remove, and Update Employers as well as their employees. Transit benefits should be distributed to every employee listed under an employer.

## User: City Go Employer

A City Go Employer that wishes to manage their own transit benefits should have the ability to log on to the application and view all of their qualified employees. Employers need the ability to Add, Remove, and Update their employees. Transit benefits should be distributed to every employee listed under an employer.

## [Masabi API](https://drive.google.com/file/d/0B2FrAPrczcVFVnRaci1kRjd6X25Uc0FyUG9ObW1PNG9IazFV/view)

The Masabi API is utilized to push transit passes to employees from the application. 

Our workflow is as follows:
Get new Auth token -> Attempt to create order -> Attempt to issue ticket

Endpoint Summary: 
- **/externalorders:** creates an order
- **/externalorders/{orderId}/issue:** issues a ticket
- **/externalorders/{orderId}/delete:** deletes an order
- **/externalorders/cancelTicket:** cancels an issued ticket
- **/externalorders/products:** returns available products (we are currently only using 31D_L)
- **/externalorders/stations:** would return stations, not relevant for our local bus system
- **/externalorders/health/status:** checks health of the API
