#CRUD operations
'''The CRUD operations represent the four basic functions that 
you require to interact with any persistent storage, such as a database. 
In web development, the CRUD operations often correspond to HTTP methods.
'''

#Create operation
'''Creating data often involves presenting a form to the user to gather the
 information that you want to store in the database as a new record. In Flask, 
 this data is accessed using flask.request.form.

HTML form for creating data:
'''
```<form method="POST" action="/create">
    `<input type="text" name="name">
    `<input type="submit" value="Create">
`</form>``

#Python code:

@app.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        # Access form data
        name = request.form['name']
        # Create a new record with the name
        record = create_new_record(name)  # Assuming you have this function defined
        # Redirect user to the new record
        return redirect(url_for('read', id=record.id))
    # Render the form for GET request
    return render_template('create.html')

#Read operation
'''
Reading data involves accessing the data and presenting it to the user. 
To access specific entries, the request needs to go with specific IDs. 
Therefore, you will need to pass the ID as an argument to the function. 
The following example shows that the ID can be accessed from the route.
'''

@app.route('/read/<int:id>', methods=['GET'])
def read(id):
    # Get the record by id
    record = get_record(id)  # Assuming you have this function defined
    # Render a template with the record
    return render_template('read.html', record=record)

#Update operation
'''Updating data requires the process of accessing specific entries, 
like the Read operation, and involves giving new data to the concerned parameter, 
like the Create operation. Therefore, 
the route should access the ID and contain both access methods.

'''
```<form method="POST" action="/update/{{record.id}}">
    `<input type="text" name="name" value="{{record.name}}">
    `<input type="submit" value="Update">
`</form>```



@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    if request.method == 'POST':
        # Access form data
        name = request.form['name']
        # Update the record with the new name
        update_record(id, name)  # Assuming you have this function defined
        # Redirect user to the updated record
        return redirect(url_for('read', id=id))
    
    # Render the form for GET request with current data
    record = get_record(id)  # Assuming you have this function defined
    return render_template('update.html', record=record)

#Delete operation
'''Deleting data involves removing a record based on its ID. 
The Delete operation will typically require the ID to be passed, 
as reported by the HTML page, in the form of an argument to the function.
'''
#Sample HTML form for deleting data:

```<form method="POST" action="/delete/{{record.id}}">
   `<input type="submit" value="Delete">
`</form>``

@app.route('/delete/<int:id>', methods=['POST'])
def delete(id):
    # Delete the record
    delete_record(id)  # Assuming you have this function defined
    # Redirect user to the homepage
    return redirect(url_for('home'))
