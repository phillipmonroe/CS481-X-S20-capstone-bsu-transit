## Auth0 Guide
*by the Transit Boys*

### Auth0 Login
Email: transitauth0@gmail.com

Password: BSU2020vrt!

### Relevant Tutorials
* [Auth0 Setup](https://auth0.com/docs/quickstart/spa/angular2/01-login)
* [Auth0 Roles](https://auth0.com/docs/authorization/concepts/rbac)
* [Auth0 API Endpoints](https://auth0.com/docs/api/management/v2?_ga=2.167096318.1922675776.1587499523-2112901134.1581454515#!/Users/post_users)

### The Basics
When a user logins in, Auth0 returns 3 things

1. *access_token*: authorizes access/permissions
2. *id_token*: caches user profile info
3. *expires_in*: number of seconds till token expires


Through Auth0 dashboard, users can be assigned different roles

- CityGoAdmin
    - Able to perform CRUD operations on ALL Employers and Employees
- Employer
    - Able to perform CRUD operations on their associated Employees
- User
    - No permissions granted, should display contact info for CityGO (with current disabled public sign-up, user without admin or employer role should not exist)

These roles are given certain permissions through the dashboard and attach to an API.
Instructions for setting up the backend API can be found [here](https://auth0.com/docs/quickstart/spa/angular2/02-calling-an-api).


### To Do
1. Admins/Employers need to be  created in Auth0 when they are created in our back-end application. Current implementation requires bulk input through dashboard
   - Public API calls to create users and assign them appropriate roles are blocked by the disabled public sign-ups (Under Dashboard -> Connections -> Username-Password-Auth -> Disable Sign Ups)
   - It appears there are 2 different Auth0 APIs, the one linked above ([here](https://auth0.com/docs/api/management/v2?_ga=2.167096318.1922675776.1587499523-2112901134.1581454515#!/Users/post_users)) or the [Authentication API](https://auth0.com/docs/api/authentication#introduction) (this one is blocked by disabling public sign-up). Use the first API

2. Design a way to display appropriate information for Employers. Currently, an employer has permissions for ANY employer page, instead of just their assigned employees



