# OAuth 2.0 Notes

## Basics
### Roles
1. Users
1. Application
1. Service/Api
	- Authorization Server
	- Data Server

### Process
**Background:** Application registers with Service/API

  - Application gives redirect/callback URI
  - Application is given clientID and clientSecret

1. App requests authorization from authorization server
1. User approves the request
1. App is granted authorization from authorization server
1. App request for access, given access token from authorization server
1. App uses access token to retrieve information from data server 
  - access token is tied to certain permissions



## Links
- [OAuth 2.0 for 9th Graders](http://agileanswer.blogspot.ca/2012/08/oauth-20-for-my-ninth-grader.html)

- [Video Explanation](https://www.youtube.com/watch?v=CPbvxxslDTU)

- [Simple Quora Answer](https://www.quora.com/OAuth-2-0/How-does-OAuth-2-0-work)
