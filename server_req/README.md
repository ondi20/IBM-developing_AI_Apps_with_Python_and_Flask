@server.py
task 1:
Create a method called name_search with the @app.route decorator. This method should be called when a client requests for the /name_search URL. The method will not accept any parameter, however, will look for the argument q in the incoming request URL. This argument holds the first_name the client is looking for. The method returns:

Person information with a status of HTTP 400 if the first_name is found in the data
Message of Invalid input parameter with a status of HTTP 422 if the argument q is missing from the request
Message of Person not found with a status code of HTTP 404 if the person is not found in the data
```from flask import request```


@dynamic_urls.py
Your Tasks
You are asked to implement both of these endpoints in this exercise. You will also implement a count method that returns the total number of persons in the data list. This will help confirm that the two methods GET and DELETE work, as required.

Task 1: Create GET /count endpoint
Create /count endpoint.

Add the @app.get() decorator for the /count URL. Define the count function that simply returns the number of items in the data list.

Task 2: Create GET /person/id endpoint
Implement the GET endpoint to ask for a person by id.

Create a new endpoint for http://localhost/person/unique_identifier. The method should be named find_by_uuid. It should take an argument of type UUID and return the person JSON if found. If the person is not found, the method should return a 404 with a message of person not found. Finally, the client (curl) should only be able to call this method by passing a valid UUID type id.

Task 3: Create DELETE /person/id endpoint
Implement the DELETE endpoint to delete a person resource.

Create a new endpoint for DELETE http://localhost/person/unique_identifier. The method should be named delete_by_uuid. It should take in an argument of type UUID and delete the person from the data list with that id. If the person is not found, the method should return a 404 with a message of person not found. Finally, the client (curl) should call this method by passing a valid UUID type id.