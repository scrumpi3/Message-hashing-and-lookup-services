# Challenge #1

Message hashing and lookup services

These services where generated using [Swagger].

## Approach
The service interfaces were defined in Challenge #1 through two endpoints.
1. /messages takes a message (a string) as a POST and returns the SHA256 hash digest of that
message (in hexadecimal format)
2. /messages/<hash> is a GET request that returns the original message. A request to a non-existent
<hash> should return a 404 error.

These service interfaces were enough information to build a YAML file, which is available at [messageToHash.yaml][messageToHash].  
This YAML file was used by [Swagger] to generate a Python Flask server. 
The code for this server is available in the [python-flask-server] subdirectory.  
Additional information on building and running the server is available in the [python-flask-server] subdirectory's [README][README_sub] file.

## Questions
### Scaling
What would the bottleneck(s) be in your implementation as you acquire more users? How you might scale your
microservice?


### Deployment
How would you improve your deployment process if you needed to maintain this application long term?


License
----
[MIT][MIT_lic]


[Swagger]: <https://swagger.io>
[python-flask-server]: <https://github.com/scrumpi3/SOLUTION_BENJAMIN_BECKMANN/tree/master/Challenge_1/python-flask-server>
[MIT_lic]: <https://opensource.org/licenses/MIT>
[README_sub]: <https://github.com/scrumpi3/SOLUTION_BENJAMIN_BECKMANN/blob/master/Challenge_1/python-flask-server/README.md>
[messageToHash]: <https://github.com/scrumpi3/SOLUTION_BENJAMIN_BECKMANN/blob/master/Challenge_1/messageToHash.yaml>
