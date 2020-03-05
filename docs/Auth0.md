AUTH0 LOGIN
Email: transitauth0@gmail.com
Password: BSU2020vrt!

For more information on how Auth0 is currently setup, go to:
https://auth0.com/docs/quickstart/spa/angular2/01-login
TLDR: When a user logins in, auth0 returns 3 things
1. access_token: authorizes access/permissions
2. id_token: caches user profile info
3. expires_in: number of seconds till token expires


Through Auth0 dashboard, users can be assigned different roles
    - CityGoAdmin
        - Able to perform CRUD operations on ALL Employers and Employees
    - Employer
        - Able to perform CRUD operations on their associated Employees
    - User
        - No permissions granted, should display contact info for CityGO

These roles are given certain permissions through the dashboard and attach to an API.
Instructions for setting up the backend API can be found here:
https://auth0.com/docs/quickstart/spa/angular2/02-calling-an-api

As far as I can tell, Auth0 users are unique between applications. That is, if a user
creates an account on a webapp that uses Auth0, then tries to sign into our app
with the same credentials, they WILL NOT be valid. Auth0 databases are unique
instances for each application.

Further implementation of Auth0 functionality will require discussion of the backend
endpoints that can be permised/denied to certain users. 


