# City Go Transit Application

## Executive Summary

The purpose of this application is to allow City Go Administrators and City Go Clients the ability to manage transit benefits for qualified employees. Employers will be able to add employees to the application by either uploading from a CSV file or a single entry. Once these employees are in the system, the application will attempt to push out a 31 day pass every month to employees, based on their email address. We assume that employees have already created a CityGo account with their provided work email. Admins have the added ability of managing other admins, employers, and employees.

## Application Architecture Overview
--TODO--

## User: City Go Administrator

A City Go Administrator should have the ability to log on to the application and view Employers that have signed up for City Go transit benefits. Admins need the ability to Add, Remove, and Update Employers as well as their employees. Transit benefits should be distributed to every employee listed under an employer.

## User: City Go Employer

A City Go Employer that wishes to manage their own transit benefits should have the ability to log on to the application and view all of their qualified employees. Employers need the ability to Add, Remove, and Update their employees. Transit benefits should be distributed to every employee listed under an employer.

## Masabi API

The Masabi API is utilized to push transit passes to employees from the application. 

--TODO--
