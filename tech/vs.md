# Comparisons

## Object-Oriented Programming vs Functional Programming

[Relevant Link](https://www.codenewbie.org/blogs/object-oriented-programming-vs-functional-programming)

OOP - brings data and behaviour to one location: the object

FP - data and behaviour should be separate for clarity

- does not create objects, just modifies data sets
- output commands are designed by programmer too because it's a transformation of the data
- tracks state and history due to transformation of data (original data is not altered, we are handed a transformed copy of original data)


## REST vs RPC vs SOAP
Link: <https://www.smashingmagazine.com/2016/09/understanding-rest-and-rpc-for-http-apis/>

### SOAP
- it's a protocol, not an architectural style loool
- but happens to use HTTP too :what:

### REST - Representational State Transfer

- definitive way of CRUD which utilizes HTTP methods (no more `POST <url>/delete/something`)
- stateless (to maintain 'states', the client just pass back ids and etc. that can retrieve from caches or run another call)
- should be one subdomain
- should use hypermedia and HATEOAS (hypermedia as the engine of application state) but no one really does

### RPC (Remote Procedure Call)
- functions are created and associated with each url endpoint (e.g. `/callfoo` means `callfoo()` function exists)
- most only support GET and POST, so no `POST <url>/delete/something`
- good for functions but better than REST for GET/POST commands

