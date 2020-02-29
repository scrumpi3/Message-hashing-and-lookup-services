# Message hashing and lookup services

Message hashing and lookup services

These services where generated using [Swagger].

## Approach
The service interfaces were defined in Challenge #1 through two endpoints.
1. /messages takes a message (a string) as a POST and returns the SHA256 hash digest of that
message (in hexadecimal format)
2. /messages/&lt;hash> is a GET request that returns the original message. A request to a non-existent
&lt;hash> should return a 404 error.

These service interfaces were enough information to build a YAML file, which is available at [messageToHash.yaml][messageToHash].  
This YAML file was used by [Swagger] to generate a Python Flask server. 
The code for this server is available in the [python-flask-server] subdirectory.  
Additional information on building and running the server is available in the [python-flask-server] subdirectory's [README][README_sub] file.

## Questions
### Scaling
What would the bottleneck(s) be in your implementation as you acquire more users? 
> The current implementation uses are single container, to deploy a set of services, to an in-memory Flask server.
> This solution has mutltiple bottlenecks.
> 1. All user requests are handled by a single server instance, limiting the number of requests that can be handled per unit time.
> 2. All user requests are implemented as syncriounious blocking functions, therefore a request must be processed completely before another request can be handled by the same processing unit.
> 3. All stored data is placed in memory within a single server, not in a database.  Therefore, well praticed database connection pooling, data replication, backup and recovery processes would need to be added once a data storage layer was added to the application.


How you might scale your microservice?
> I would optimize my microservices for concurrency and data partitioning to improve performance at scale.
> I would also design in additional layers to support security, identity, load balancing, and data storage. 
> These additional layers would allow for system protections, 
> 1. like DDoS, through white and black listing in the security layer.
> 2. Identification of individuals, using indenties provided by other entities, in the identity layer.
> 3. Increse the number of requests that can be handled through the replication of microservices in multiple containers/servers behind a load balancer.
> 4. Divide the data storage layer into read only data replicas for handling the GET requests, and master writable replicated data stores to handle the POST requests.

### Deployment
How would you improve your deployment process if you needed to maintain this application long term?
> Currently, the deployment process is a single package, all contained in one Docker file.
> To improve the deployment process, I would design a system with multiple layers and spend time defining the interface between each layer.
> A layered abstraction allows for seperation of concerns and a loosly coupled system, where the failure of a single component will not disrupt the entire system.

License
----
[MIT][MIT_lic]


[Swagger]: <https://swagger.io>
[python-flask-server]: <https://github.com/scrumpi3/SOLUTION_BENJAMIN_BECKMANN/tree/master/Challenge_1/python-flask-server>
[MIT_lic]: <https://opensource.org/licenses/MIT>
[README_sub]: <https://github.com/scrumpi3/SOLUTION_BENJAMIN_BECKMANN/blob/master/Challenge_1/python-flask-server/README.md>
[messageToHash]: <https://github.com/scrumpi3/SOLUTION_BENJAMIN_BECKMANN/blob/master/Challenge_1/messageToHash.yaml>
